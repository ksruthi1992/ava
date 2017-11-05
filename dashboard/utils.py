from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework import status
from rest_framework.response import Response

from constants import *
from dashboard.models import User


def prepare_response(query=None, mode=AVA_MODES[DEFAULT_MODE], intent=INTENT_DEFAULT, parameters=None, context=None, response=DEFAULT_RESPONSE):

    result = {"query":query,
              "mode":mode,
              "intent":intent,
              "parameters":parameters,
              "context":context,
              "response":response}

    return result

def perform_intent_function_and_get_response(intent, parameters, context):
    # response object to be sent to controller
    # will have objects for message, error and data object for the controller
    response = {}

    if intent == INTENT_DEFAULT:
        response = "This response is by default intent"

    elif intent == INTENT_LOGIN:
        email = parameters.get('email')
        password = parameters.get('password')
        if login(email, password):
            user = User.objects.get(email=email, password=password)
            response="Hey "+user.firstname+"! How are you doing today?"
        else:
            response = "Oh dear! I don't remember user by that username/password."

    elif intent == INTENT_REGISTER:
        email = parameters.get('email')
        password = parameters.get('password')
        first_name = parameters.get('first_name')
        try:
            if not email_validation(email):
                response = "Invalid email."
            else:
                User.objects.create(email=email ,password=password, first_name=first_name)
                user = User.objects.get(email=email, password=password)
                response = "Signed up!"
        except:
            response = "User registration not successful"

    return response

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