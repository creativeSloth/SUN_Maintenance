from faulthandler import is_enabled

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.constants.c_db_classes import *
from database.utils.u_db_sess import BASE


def init_local_db() -> None:
    """
    Initialisiert eine lokale Datenbank in der Zusätzliche Informationen gespeichert werden können,
    welche durch den Nutzer der Software selbst angelegt und geupdated werden.
    """
    from database.utils.u_db_sess import get_db_engine

    ENGINE = get_db_engine()
    BASE.metadata.create_all(ENGINE)


class Users(BASE):
    __tablename__ = DB_TABLENAME_USERS
    id = Column(Integer, primary_key=True)

    username = Column(String, nullable=True)
    password_hashed = Column(String, nullable=True)
    hex_encoded_salt = Column(String, nullable=False)
    date_created = Column(String, nullable=True)
    is_active = Column(Boolean, default=False)
    is_enabled = Column(Boolean, default=True)
    roles = relationship("UserRoles", backref="user")
    login_dates = relationship("LoginDates", backref="user")


class UserRoles(BASE):
    __tablename__ = DB_TABLENAME_USER_ROLES
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    role_id = Column(Integer, ForeignKey("roles.id"))


class Roles(BASE):
    __tablename__ = DB_TABLENAME_ROLES
    id = Column(Integer, primary_key=True)
    role_name = Column(String, nullable=False)
    permissions = relationship("RolePermissions", backref="role")


class RolePermissions(BASE):
    __tablename__ = DB_TABLENAME_ROLE_PERMISSIONS
    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.id"))
    permission_name = Column(String, nullable=False)
    is_allowed = Column(Boolean, nullable=False)


class LoginDates(BASE):
    __tablename__ = DB_TABLENAME_LOGIN_DATES
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    login_date = Column(String, nullable=True)
