import os

if __name__ == '__main__' and __package__ is None:
    os.sys.path.append(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ava.settings")

import django
from django.contrib.sessions.backends.db import SessionStore
django.setup()
session_key = 'ei4npjnrlqwewxedox5a991vtaor2bfh'

s = SessionStore()
key = s.create()
print s.session_key