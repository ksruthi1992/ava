import os
from datetime import datetime

from elasticsearch import Elasticsearch

if __name__ == '__main__' and __package__ is None:
    os.sys.path.append(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ava.settings")

import django

from django.contrib.sessions.backends.db import SessionStore
django.setup()

from dashboard.models import User
session_key = 'ei4npjnrlqwewxedox5a991vtaor2bfh'

# s = SessionStore()
# key = s.create()
# print s.session_key
# user = User.objects.create(email="asd@fsd.com", password="sad", first_name="asd").save()

es = Elasticsearch()
# es.indices.create(index='my-index', ignore=400)
es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})

print es.get(index="my-index", doc_type="test-type", id=42)['_source']['any']
