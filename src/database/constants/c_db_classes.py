################################################################
###################  USER ROLE SYSTEM ##########################
################################################################
from typing import List

DB_TABLENAME_USERS: str = "users"
DB_TABLENAME_USER_PROFILES: str = "user_profile"
DB_TABLENAME_USER_POLICIES: str = "user_policies"
DB_TABLENAME_USER_ROLES: str = "user_roles"
DB_TABLENAME_ROLES: str = "roles"
DB_TABLENAME_ROLE_PERMISSIONS: str = "role_permissions"
DB_TABLENAME_LOGIN_DATES: str = "login_dates"
DB_TABLENAME_PERMISSIONS: str = "permissions"
################################################################
###################  ARTICLE DATA  ##############################
################################################################
DB_TABLENAME_MANUFACTURERS: str = "manufacturers"
DB_TABLENAME_SPECIALIZED_FIELDS: str = "specialized_fields"
DB_TABLENAME_ARTICLES: str = "articles"
DB_TABLENAME_ARTICLE_TYPES: str = "article_types"
DB_TABLENAME_MODULE_DETAILS: str = "module_details"
DB_TABLENAME_INVERTERS_DETAILS = "inverters_details"
DB_TABLENAME_MPP_TRACKERS: str = "MPP-trackers"
################################################################
###################  PROJECT DATA  ##############################
################################################################
DB_TABLENAME_PROJECTS: str = "project"
DB_TABLENAME_PARTIAL_SYSTEMS: str = "partial_systems"
DB_TABLENAME_PV_GENERATORS: str = "PV_generators"
DB_TABLENAME_SYSTEM_INVERTERS: str = "system_inverters"

RSHIP_TYPES: List[str] = ["1:1", "1:n", "n:m"]
