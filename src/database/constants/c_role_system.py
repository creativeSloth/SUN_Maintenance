DFLT_ROLES = ["admin", "user"]

DFLT_PERMISSION_NAMES = ["can_give_permissions", "can_read", "can_write_everything"]

DFLT_ROLE_PERMISSIONS = {
    DFLT_ROLES[0]: {  # "admin"
        DFLT_PERMISSION_NAMES[0]: True,  # "can_give_permissions"
        DFLT_PERMISSION_NAMES[1]: True,  # "can_read"
        DFLT_PERMISSION_NAMES[2]: True,  # "can_write_everything"
    },
    DFLT_ROLES[1]: {  # "user"
        DFLT_PERMISSION_NAMES[0]: False,  # "can_give_permissions"
        DFLT_PERMISSION_NAMES[1]: True,  # "can_read"
        DFLT_PERMISSION_NAMES[2]: False,  # "can_write_everything"
    },
}
