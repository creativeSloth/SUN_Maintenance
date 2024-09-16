from ast import Dict
from typing import List, Optional, Tuple

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload, sessionmaker

from database.classes.cls_users import LoginDates, Roles, UserProfile, Users
from database.constants.c_role_system import DFLT_ROLE_NAMES
from database.utils.u_db_sess import create_session
from database.utils.u_pwd import hash_pwd, verify_password
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


def login_user(
    usr: Optional[str] = None, pwd: Optional[str] = None
) -> Tuple[bool, bool, Users]:
    r"""
    Validates the provided username and password against the database.
    :param usr: The username to be validated.
    :type usr: Optional[str]
    :param pwd: The password to be validated.
    :type pwd: Optional[str]
    :return: A tuple with two boolean values. The first value user_existed indicates whether
             the user already exists in the database. The second value pwd_verified indicates
             whether the provided password is correct for the user.
    :rtype: Tuple[bool, bool]
    """
    user_existed = False
    pwd_verified = False
    sess = None
    try:
        sess: sessionmaker = create_session()
        # Check if the user already exists
        exstg_usr: Users = sess.query(Users).filter(Users.username == usr).first()

        if exstg_usr:
            user_existed = True

            stored_salt = exstg_usr.hex_encoded_salt
            stored_pwd = exstg_usr.password_hashed

            # Verify the password
            pwd_verified = verify_password(
                stored_pwd=stored_pwd, stored_salt=stored_salt, provided_pwd=pwd
            )

            login_date = LoginDates(user_id=exstg_usr.id)
            sess.add(login_date)

        sess.commit()

    except SQLAlchemyError as e:
        if sess:
            sess.rollback()
        raise e
    finally:
        sess.close()

    return user_existed, pwd_verified, exstg_usr


def get_all_usrs_infos() -> List[Users]:
    sess: sessionmaker = create_session()
    try:
        usrs_infos: List[Users] = (
            sess.query(Users)
            .options(
                joinedload(Users.user_profile),
                joinedload(Users.login_dates),
                joinedload(Users.roles),
            )
            .all()
        )
        return usrs_infos
    finally:
        sess.close()


def get_mapped_usr_infos() -> List[Dict]:
    usrs_infs: List[Users] = get_all_usrs_infos()

    ############################### KNOPF ################################

    # checkbox = QCheckBox()
    # checkbox.setChecked(True)
    # checkbox.setObjectName(f"CheckBox_{table.objectName()}_{tw_row}_0")

    # layout = QHBoxLayout()
    # layout.setObjectName(f"Layout_{table.objectName()}_{tw_row}_0")
    # layout.setContentsMargins(5, 0, 5, 0)
    # layout.setSpacing(2)

    # cell_widget = QWidget()
    # cell_widget.setLayout(layout)
    # create_and_set_obj_property(
    #     obj=cell_widget,
    #     property_type="cell_widget",
    #     property_value="contains_checkbox",
    # )

    # layout.addWidget(checkbox)

    # # Spalte 1 mit der CheckBox
    # table.setCellWidget(tw_row, 0, cell_widget)

    unpacked_usrs_inf = []
    for usr_inf in usrs_infs:
        unpacked_user_info = {
            "Profil bearbeiten": "KNOPF",
            "Username": usr_inf.username,
            "Vorname": usr_inf.user_profile.name,
            "Familienname": usr_inf.user_profile.family_name,
            "Rollen": (
                ", ".join(role.role_name for role in usr_inf.roles)
                if usr_inf.roles
                else "N/A"
            ),
            "Erstelldatum": usr_inf.date_created,
            "Letzter Login": sorted(
                [itm.login_date for itm in usr_inf.login_dates][-1]
                if usr_inf.login_dates
                else "N/A"
            ),
        }

        unpacked_usrs_inf.append(unpacked_user_info)
    return unpacked_usrs_inf
