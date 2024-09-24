from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from database.classes.cls_user_role_system import Roles
from database.constants.c_role_system import List
from database.utils.u_db_sess import create_session


def get_all_roles() -> List[Roles]:
    r"""
    Retrieves all roles from the database.

    Args:
        None

    Raises:
        e: SQLAlchemyError

    Returns:
        List[Roles]: All roles from the database
    """
    sess: sessionmaker = create_session()
    try:
        all_roles: List[Roles] = sess.query(Roles).all()

        return all_roles
    except SQLAlchemyError as e:
        if sess:
            sess.rollback()
        raise e
    finally:
        sess.close()
