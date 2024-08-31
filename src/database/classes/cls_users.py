from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.constants.c_db_classes import *
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
    user_roles = relationship("UserRoles", backref="role")
    role_permission = relationship("RolePermissions", backref="role")


class RolePermissions(BASE):
    """
    A table to store the permissions for each role.
    `KEY_TABLE`
    """

    __tablename__ = DB_TABLENAME_ROLE_PERMISSIONS
    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.id"))
    permission_id = Column(Integer, ForeignKey("permissions.id"))
    is_allowed = Column(Boolean, nullable=False)


class Permissions(BASE):
    __tablename__ = DB_TABLENAME_PERMISSIONS
    id = Column(Integer, primary_key=True)
    permission_name = Column(String, nullable=False)
    role_permission = relationship("RolePermissions", backref="permission")


class LoginDates(BASE):
    __tablename__ = DB_TABLENAME_LOGIN_DATES
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    login_date = Column(String, nullable=False)
