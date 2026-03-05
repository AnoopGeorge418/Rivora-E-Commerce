from enum import Enum

class AuthProviders(str, Enum):
    PHONE ="PHONE"
    EMAIL ="EMAIL"
    GOOGLE = "GOOGLE"
    APPLE = "APPLE"
    GITHUB = "GITHUB"
    SUPERBASE = "SUPERBASE"
