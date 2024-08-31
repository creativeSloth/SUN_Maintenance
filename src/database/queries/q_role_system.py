from sqlalchemy.exc import SQLAlchemyError

from database.constants.c_role_system import *
from database.utils.u_db_sess import create_session


def init_base_role_system() -> None:
    """
    Initializes the base role system. Creates the default role system within the first launch to make default roles available.
    """
    from database.classes.cls_users import Permissions, RolePermissions, Roles

    sess = create_session()

    try:
        # Check if roles already exist and create them if they don't
        roles_dict = {}
        for role_name in DFLT_ROLES:
            role = sess.query(Roles).filter_by(role_name=role_name).first()
            if not role:
                role = Roles(role_name=role_name)
                sess.add(role)
            roles_dict[role_name] = role

        sess.commit()

        # Check if permissions already exist and create them if they don't
        permissions_dict = {}
        for perm_name in DFLT_PERMISSION_NAMES:
            perm = sess.query(Permissions).filter_by(permission_name=perm_name).first()
            if not perm:
                perm = Permissions(permission_name=perm_name)
                sess.add(perm)
            permissions_dict[perm_name] = perm

        sess.commit()

        # Generate role permissions based on configuration
        role_permissions = [
            RolePermissions(
                role_id=roles_dict[role_name].id,
                permission_id=permissions_dict[perm_name].id,
                is_allowed=is_allowed,
            )
            for role_name, permissions in DFLT_ROLE_PERMISSIONS.items()
            for perm_name, is_allowed in permissions.items()
        ]

        # Add new role permissions only if they don't already exist
        for rp in role_permissions:
            existing_rp = (
                sess.query(RolePermissions)
                .filter_by(role_id=rp.role_id, permission_id=rp.permission_id)
                .first()
            )
            if not existing_rp:
                sess.add(rp)
        sess.commit()

    except SQLAlchemyError as e:
        if sess:
            sess.rollback()
        raise e
    finally:
        sess.close()
