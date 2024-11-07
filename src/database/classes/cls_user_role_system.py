from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.classes.cls_article_data import Manufacturers
from database.classes.cls_project_data import Projects
from database.constants.c_db_classes import *
from database.utils.u_db_sess import BASE


class Users(BASE):
    r"""
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
    date_created = Column(
        String,
        default=lambda: datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        nullable=False,
    )
    date_changed = Column(String)
    date_deleted = Column(String)
    is_active = Column(Boolean, default=False)
    is_enabled = Column(Boolean, default=True)

    # Define the one-to-one relationship
    user_profile = relationship("UserProfile", back_populates="user", uselist=False)

    # Define one-to-many relationships
    login_dates = relationship("LoginDates", back_populates="user")
    manufacturers = relationship("Manufacturers", back_populates="user")
    articles = relationship("Articles", back_populates="user")
    projects = relationship("Projects", back_populates="user")

    # Define many-to-many relationships
    roles = relationship(
        "Roles",
        secondary=DB_TABLENAME_USER_ROLES,
        back_populates=DB_TABLENAME_USERS,
    )


class UserProfile(BASE):
    r"""
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
    user_id = Column(Integer, ForeignKey(DB_TABLENAME_USERS + ".id"), nullable=False)
    name = Column(String, nullable=True)
    family_name = Column(String, nullable=True)

    date_created = Column(
        String,
        default=lambda: datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        nullable=False,
    )
    date_changed = Column(String)
    date_deleted = Column(String)

    # Define the one-to-one relationship
    user = relationship(
        "Users", back_populates=DB_TABLENAME_USER_PROFILES, uselist=False
    )


class UserRoles(BASE):
    r"""
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
    user_id = Column(
        Integer,
        ForeignKey(DB_TABLENAME_USERS + ".id"),
        primary_key=True,
        nullable=False,
    )
    role_id = Column(
        Integer,
        ForeignKey(DB_TABLENAME_ROLES + ".id"),
        primary_key=True,
        nullable=False,
    )

    date_created = Column(
        String,
        default=lambda: datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        nullable=False,
    )
    date_changed = Column(String)
    date_deleted = Column(String)


class Roles(BASE):
    r"""
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

    date_created = Column(
        String,
        default=lambda: datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        nullable=False,
    )
    date_changed = Column(String)
    date_deleted = Column(String)

    # Define many-to-many relationships
    users = relationship(
        "Users", secondary=DB_TABLENAME_USER_ROLES, back_populates=DB_TABLENAME_ROLES
    )
    permissions = relationship(
        "Permissions",
        secondary=DB_TABLENAME_ROLE_PERMISSIONS,
        back_populates=DB_TABLENAME_ROLES,
    )


class RolePermissions(BASE):
    r"""
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
    role_id = Column(
        Integer,
        ForeignKey(DB_TABLENAME_ROLES + ".id"),
        primary_key=True,
        nullable=False,
    )
    permission_id = Column(
        Integer,
        ForeignKey(DB_TABLENAME_PERMISSIONS + ".id"),
        primary_key=True,
        nullable=False,
    )
    is_allowed = Column(Boolean, nullable=False)

    date_created = Column(
        String,
        default=lambda: datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        nullable=False,
    )
    date_changed = Column(String)
    date_deleted = Column(String)


class Permissions(BASE):
    r"""
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

    date_created = Column(
        String,
        default=lambda: datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        nullable=False,
    )
    date_changed = Column(String)
    date_deleted = Column(String)

    # Define the many-to-many relationship
    roles = relationship(
        "Roles",
        secondary=DB_TABLENAME_ROLE_PERMISSIONS,
        back_populates=DB_TABLENAME_PERMISSIONS,
    )


class LoginDates(BASE):
    r"""
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
    user_id = Column(Integer, ForeignKey(DB_TABLENAME_USERS + ".id"), nullable=False)
    login_date = Column(
        String,
        default=lambda: datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        nullable=False,
    )

    # Define the relationship to Users
    user = relationship("Users", back_populates=DB_TABLENAME_LOGIN_DATES)
