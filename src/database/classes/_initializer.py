from database.queries.q_role_system import init_base_role_system
from database.utils.u_db_sess import BASE, get_db_engine


def init_local_db() -> None:
    """
    Initializes the local database for handling contents, such as:
    >>> Users
    >>> Role System

    If the database does not exist, it will be created. If the default Role System is not initialized, it will be initialized.
    """
    ENGINE = get_db_engine()
    BASE.metadata.create_all(ENGINE)
    init_base_role_system()
