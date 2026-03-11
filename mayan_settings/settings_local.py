from mayan.settings.production import

import ldap
from django_auth_ldap.config import LDAPSearch
import logging
# ===============================
# AUTH BACKENDS
# ===============================
AUTHENTICATION_BACKENDS = [
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
]

# ===============================
# LDAP SERVER
# ===============================
AUTH_LDAP_SERVER_URI = "ldap://dc1.ad.agson.co.id:389"
LDAP_URL = 'ldap://dc1.ad.agson.co.id:389'
AUTH_LDAP_START_TLS = False

# ===============================
# SERVICE ACCOUNT (BIND)
# ===============================
AUTH_LDAP_BIND_DN = "mayed@ad.agson.co.id"
AUTH_LDAP_BIND_PASSWORD = "v#H6MJyq9M"

# setelah user ditemukan, bind ulang menggunakan credential user
AUTH_LDAP_BIND_AS_AUTHENTICATING_USER = True

# ===============================
# USER SEARCH
# ===============================
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "DC=ad,DC=agson,DC=co,DC=id",
    ldap.SCOPE_SUBTREE,
    "(sAMAccountName=%(user)s)"
)

# ===============================
# ATTRIBUTE MAPPING
# ===============================
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}

# ===============================
# USER FLAGS
# ===============================
AUTH_LDAP_USER_IS_ACTIVE = True
AUTH_LDAP_USER_IS_STAFF = True

# ===============================
# LDAP OPTIONS
# ===============================
AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_REFERRALS: 0
}

# ===============================
# UPDATE USER
# ===============================
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# ===============================
# DEBUG LDAP
# ===============================
ldap_logger = logging.getLogger("django_auth_ldap")
ldap_logger.setLevel(logging.DEBUG)
ldap_logger.addHandler(logging.StreamHandler())
