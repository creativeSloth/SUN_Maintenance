from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from database.classes.cls_users import Users
from database.utils.u_db_sess import create_session
from database.utils.u_pwd import hash_pwd
from database.utils.u_queries import commit_new_entry


def update_db_user(
    usr: str = None,
    pwd: str = None,
) -> bool:
    r"""
    Creates or updates a user in the database with the given username and password.
    If the user already exists, the password is updated.
    If the user does not exist, a new entry is created.

    :param ``user``: The user to be updated
    :type ``user``: str
    :param ``pwd``: The password to be updated
    :type ``pwd``: str
    :return: A boolean ``usr_existed`` indicating whether the user already existed in the database
    :rtype: bool
    """

    sess: sessionmaker = create_session()
    usr_existed: bool = None
    usr_created: bool = None
    try:

        # Überprüfen, ob article_no bereits in der Blacklists-Tabelle existiert
        exstg_usr = sess.query(Users).filter(username=usr).first()

        if exstg_usr:
            usr_existed = True
            usr_created = False

        else:

            password_hashed, hex_encoded_salt = hash_pwd(pwd)
            date_created = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

            new_usr_entry = commit_new_entry(
                cls=Users,
                sess=sess,
                username=usr,
                password_hashed=password_hashed,
                hex_encoded_salt=hex_encoded_salt,  # Speichere das Salt in der Datenbank
                date_created=date_created,
                is_active=False,
                is_enabled=True,
                date_last_login=None,
            )

            usr_existed = False
            usr_created = True

            count = sess.query(Users).filter(is_enabled=True).count()
            if count == 1:
                new_usr_entry
                #!
                #! CONTINUE HERE
                #!
                #!

    except SQLAlchemyError as e:
        if sess:
            sess.rollback()
        raise e
    finally:
        sess.close()
        return usr_existed, usr_created
