from .base import *

DEBUG = True
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "{{ lookup('vault', 'secret/dolphinattacks_superstage', 'secret_key', 'vault_OTSJZqTCO1caL8ftKC3i.json') }}"

ALLOWED_HOSTS = ["107.170.109.21", ]
