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
    """
    Represents a user in the system.

    Attributes:
        id (int): Primary key for the user.
        username (str): Username of the user.
        password_hashed (str): Hashed password of the user.
        hex_encoded_salt (str): Salt used for hashing the password.
        date_created (str): Date when the user was created.
        is_active (bool): Indicates if the user is active.
        is_enabled (bool): Indicates if the user is enabled.

    Relationships:
        roles (relationship): One-to-many relationship with UserRoles.
        login_dates (relationship): One-to-many relationship with LoginDates.
        profile (relationship): One-to-one relationship with UserProfile.
    """

    __tablename__ = DB_TABLENAME_USERS
    id = Column(Integer, primary_key=True)

    username = Column(String, nullable=True)
    password_hashed = Column(String, nullable=True)
    hex_encoded_salt = Column(String, nullable=False)
    date_created = Column(String, nullable=True)
    is_active = Column(Boolean, default=False)
    is_enabled = Column(Boolean, default=True)

    # Define one-to-many relationships
    user_roles = relationship("UserRoles", back_populates="user")
    login_dates = relationship("LoginDates", back_populates="user")
    user_profile = relationship("UserProfile", back_populates="user", uselist=False)


class UserProfile(BASE):
    """
    Represents a user's profile, including additional information about the user.

    Attributes:
        id (int): Primary key for the user profile.
        user_id (int): Foreign key referencing the user.
        bio (str): Biography or additional information about the user.

    Relationships:
        user (relationship): One-to-one relationship with Users.
    """

    __tablename__ = DB_TABLENAME_USER_PROFILES
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(DB_TABLENAME_USERS + ".id"))
    bio = Column(String)

    # Define the one-to-one relationship
    user = relationship("Users", back_populates="user_profile", uselist=False)


class UserRoles(BASE):
    """
    Represents a user's role in the system, linking users to roles.

    Attributes:
        id (int): Primary key for the user-role association.
        user_id (int): Foreign key referencing the user.
        role_id (int): Foreign key referencing the role.

    Relationships:
        user (relationship): Many-to-one relationship with Users.
        role (relationship): Many-to-one relationship with Roles.
    """

    __tablename__ = DB_TABLENAME_USER_ROLES
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(DB_TABLENAME_USERS + ".id"))
    role_id = Column(Integer, ForeignKey(DB_TABLENAME_ROLES + ".id"))

    # Define the relationships
    user = relationship("Users", back_populates="user_roles")
    role = relationship("Roles", back_populates="role_users")


class Roles(BASE):
    """
    Represents a role in the system.

    Attributes:
        id (int): Primary key for the role.
        role_name (str): Name of the role.

    Relationships:
        user_roles (relationship): One-to-many relationship with UserRoles.
        role_permission (relationship): One-to-many relationship with RolePermissions.
    """

    __tablename__ = DB_TABLENAME_ROLES
    id = Column(Integer, primary_key=True)
    role_name = Column(String, nullable=False)

    # Define the many-to-many relationship
    role_users = relationship("UserRoles", back_populates="role")
    role_permissions = relationship("RolePermissions", back_populates="role")


class RolePermissions(BASE):
    """
    Represents the permissions associated with a role.

    Attributes:
        id (int): Primary key for the role-permission association.
        role_id (int): Foreign key referencing the role.
        permission_id (int): Foreign key referencing the permission.
        is_allowed (bool): Indicates if the permission is granted for the role.

    Relationships:
        role (relationship): Many-to-one relationship with Roles.
        permission (relationship): Many-to-one relationship with Permissions.
    """

    __tablename__ = DB_TABLENAME_ROLE_PERMISSIONS
    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey(DB_TABLENAME_ROLES + ".id"))
    permission_id = Column(Integer, ForeignKey(DB_TABLENAME_PERMISSIONS + ".id"))
    is_allowed = Column(Boolean, nullable=False)

    # Define the relationships
    role = relationship("Roles", back_populates="role_permissions")
    permission = relationship("Permissions", back_populates="permission_roles")


class Permissions(BASE):
    """
    Represents a permission in the system.

    Attributes:
        id (int): Primary key for the permission.
        permission_name (str): Name of the permission.

    Relationships:
        role_permission (relationship): One-to-many relationship with RolePermissions.
    """

    __tablename__ = DB_TABLENAME_PERMISSIONS
    id = Column(Integer, primary_key=True)
    permission_name = Column(String, nullable=False)

    # Define the many-to-many relationship
    permission_roles = relationship("RolePermissions", back_populates="permission")


class LoginDates(BASE):
    """
    Represents a user's login dates.

    Attributes:
        id (int): Primary key for the login date entry.
        user_id (int): Foreign key referencing the user.
        login_date (str): Date and time of the login.

    Relationships:
        user (relationship): Many-to-one relationship with Users.
    """

    __tablename__ = DB_TABLENAME_LOGIN_DATES
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(DB_TABLENAME_USERS + ".id"))
    login_date = Column(String, nullable=False)

    # Define the relationship to Users
    user = relationship("Users", back_populates="login_dates")
