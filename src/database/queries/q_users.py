from datetime import datetime
from typing import Optional, Tuple

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from database.classes.cls_users import Roles, UserProfile, Users
from database.constants.c_role_system import DFLT_ROLE_NAMES
from database.utils.u_db_sess import create_session
from database.utils.u_pwd import hash_pwd
from database.utils.u_queries import create_rshp


def update_db_user(
    usr: Optional[str] = None,
    pwd: Optional[str] = None,
    name: Optional[str] = None,
    family_name: Optional[str] = None,
) -> Tuple[bool, bool]:
    """
    Creates or updates a user in the database with the given username, password,
    first name, and family name. If the user already exists, the password is updated.
    If the user does not exist, a new entry is created with the provided details and
    an appropriate role is assigned. A user profile is created for each user, even if
    no specific details are provided.

    :param usr: The username of the user to be updated or created.
    :type usr: Optional[str]
    :param pwd: The password to be set for the user.
    :type pwd: Optional[str]
    :param name: The first name of the user. (optional)
    :type name: Optional[str]
    :param family_name: The family name of the user. (optional)
    :type family_name: Optional[str]
    :return: A tuple with two boolean values. The first value usr_existed indicates whether
             the user already existed in the database. The second value usr_created indicates
             whether a new user was successfully created.
    :rtype: Tuple[bool, bool]
    """

    sess: sessionmaker = create_session()
    usr_existed: bool = False
    usr_created: bool = False

    try:
        # Check if the user already exists
        exstg_usr: Users = sess.query(Users).filter(Users.username == usr).first()

        if exstg_usr:
            usr_existed = True
            usr_created = False
            # Update the user's password if provided
            if pwd:
                password_hashed, hex_encoded_salt = hash_pwd(pwd)
                exstg_usr.password_hashed = password_hashed
                exstg_usr.hex_encoded_salt = hex_encoded_salt
                sess.commit()
        else:
            # Create a new user
            password_hashed, hex_encoded_salt = hash_pwd(pwd)
            date_created = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

            # Determine if the new user should get "admin" or "user" role
            if not sess.query(Users).count():  # Check if this is the first user
                role_name = DFLT_ROLE_NAMES[0]
            else:
                role_name = DFLT_ROLE_NAMES[1]

            role: Roles = sess.query(Roles).filter(Roles.role_name == role_name).first()
            if not role:
                raise ValueError(f"Role '{role_name}' does not exist in the database.")

            user_attrs: dict = {
                "username": usr,
                "password_hashed": password_hashed,
                "hex_encoded_salt": hex_encoded_salt,
                "date_created": date_created,
                "is_active": False,
                "is_enabled": True,
            }

            # Assign the role to the user
            new_usr, role = create_rshp(
                sess,
                m1=Users,
                m1_attrs=user_attrs,
                m2=Roles,
                m2_attrs={"id": role.id},
            )

            # Create a user profile for the user, even if no details are provided
            user_profile_attrs = {
                "user_id": new_usr.id,
                "name": name,
                "family_name": family_name,
            }
            create_rshp(
                sess, Users, {"id": new_usr.id}, UserProfile, user_profile_attrs
            )
            # Save objects to the database
            sess.commit()
            usr_existed = False
            usr_created = True

    except SQLAlchemyError as e:
        if sess:
            sess.rollback()
        raise e
    finally:
        sess.close()

    return usr_existed, usr_created
