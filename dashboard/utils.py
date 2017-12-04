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

def prepare_response_not_auth(req_data):
    message = "Not Authorized"
    elements = {}
    request_count = check_and_get_req_count(req_data)
    response = prepare_res(ava_response=message, request_count=request_count, elements=elements)
    return response

def check_and_get_req_count(req_data):
    if 'request_count' in req_data:
        request_count = req_data['request_data']
    else:
        request_count = 1
    return request_count

def check_parameters(req_parameters, request_data):
    message = "Good to go!"
    element = {}

    for i in req_parameters:
        if i not in request_data:
            message = i+" missing!"
            response = prepare_res(ava_response=message, request_count=1, elements=element)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    response = prepare_res(ava_response=message, request_count=1, elements=element)
    return Response(response, status=status.HTTP_200_OK)

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