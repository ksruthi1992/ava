
import os, django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ava.settings")
django.setup()
from dashboard.models import Command
import simplejson as json
h = "{u'query': u'hey'}"
h.replace("\'","\"")
print h
j = json.loads(h)
print j
print type(j)
# j = json.loads(h,"utf-8")
# print type(h)
# print json.dumps(h)
