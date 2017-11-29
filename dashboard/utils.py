from django.contrib import messages
from django.contrib.sessions.backends.db import SessionStore
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework import status
from rest_framework.response import Response

from constants import *
from dashboard.models import User

def prepare_res(ava_response, request_count, elements):
    response = {"ava_response":ava_response,
                "request_count":request_count,
                "element":elements }
    return response

def prepare_response(query=None, mode=AVA_MODES[DEFAULT_MODE], intent=INTENT_DEFAULT, action=ACTION_DEFAULT, context=None, response=DEFAULT_RESPONSE):

    result = {"query":query,
              "mode":mode,
              "intent":intent,
              "action":action,
              "context":context,
              "response":response}
    print result
    return result


def start_new_session_and_get_key(user):
    s = SessionStore()
    s.create()

    # insert session variables
    s["user_id"] = user.id
    s.save()

    return s.session_key

def email_validation(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

def login(email, password):
    try:
        User.objects.get(email=email,password=password)
        return True
    except:
        return False

def registration(email, password, first_name, username):
    try:
        User.objects.create(email=email, password=password, first_name=first_name, username=username)

        return True
    except:
        return False