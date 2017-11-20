import json

import jsonpickle

from dashboard.constants import *
from dashboard.models import User
from dashboard.utils import login, start_new_session_and_get_key, email_validation


def perform_intent_function_and_get_response(request, response, query, intent, action, context):
    # response object to be sent to controller
    # will have objects for message, error and data object for the controller

    if intent == INTENT_DEFAULT:
        response["message"] = "This response is by default intent"
        return response

    elif intent == INTENT_LOGIN:
        # LOGIN_INTENT_ACTION_FLOW :
        # ask for email
        # check email and ask for password | email again
        # try login and start session | ask if to retry > ask for email | prev intent, action

        if action == ASK_FOR_EMAIL:
            # ask for email
            response["data"]["response"] = ASK_FOR_EMAIL_RESPONSE
            # next action
            response["action"] = EMAIL_INPUT
            return response

        if action == EMAIL_INPUT:
            # check email and return if invalid, else store in context params
            email = query
            try:
                if not email_validation(email):
                    raise Exception
                response["data"]["response"] = ASK_FOR_PASSWORD_RESPONSE
                response["context"]["email"] = email

                # next action
                response["action"] = PASSWORD_INPUT
            except:
                response["data"]["response"] = INCORRECT_EMAIL_RESPONSE
            return response

        if action == PASSWORD_INPUT:
            # try login
            try:
                email = context["email"]
                password = query
            except:
                response["error"] = True
                response["message"] = "email,password not available at "+ PASSWORD_INPUT
                response["data"]["response"] = "something went wrong."
                return response

            if not login(email, password):
                response["data"]["response"] = INVALID_LOGIN
                response["action"] = ASK_IF_TO_RETRY_LOGIN
                perform_intent_function_and_get_response(request, response, query, intent, response["action"], context)

            else:
                user = User.objects.get(email=email, password=password)
                session_key = start_new_session_and_get_key(user)
                response["data"]["response"] = "Welcome " + user.first_name
                response["context"]["user"] = jsonpickle.encode(user)
                response["context"]["session_key"] = session_key
                return response

        if action == ASK_IF_TO_RETRY_LOGIN:
            # ask if to retry
            response["data"]["response"] += " Do you want to retry login?"
            # next action
            response["action"] = USER_ACK
            return response

        if action == USER_ACK:
            if query in AFFIRMATIONS:
                response["data"]["response"] = "Alrighty! email please?"
                # next action
                response["action"] = EMAIL_INPUT
                return response
            else:
                try:
                    prev_intent = context["prev_intent"]
                    prev_action = context["prev_action"]
                except:
                    response["data"]["response"] = "...So, what are you looking for today ?"
                    return response

                response = perform_intent_function_and_get_response(request, response, query, prev_intent, prev_action ,context)
                return response

    elif intent == INTENT_REGISTER:
        # actions:
        # ask fo email
        # check email and ask for password
        # ask for firstname
        # register
        # start session
        response = ""
        # if context["action"] == ASK_FOR_EMAIL:
        #     # ask for email
        #     response["data"]["response"] = ASK_FOR_EMAIL_RESPONSE
        #     # next action
        #     context["action"] = EMAIL_INPUT
        #     return response
        #
        # if context["action"] == EMAIL_INPUT:
        #     # check email and return if invalid, else store in context params
        #     try:
        #         if not email_validation(context["parameters"]["email"]):
        #             raise Exception
        #         response["data"]["response"] = ASK_FOR_PASSWORD_RESPONSE
        #         # next action
        #         context["action"] = PASSWORD_INPUT
        #     except:
        #         response["data"]["response"] = INCORRECT_EMAIL_RESPONSE
        #     return response
        #
        # if context["action"] == PASSWORD_INPUT:
        #     # try login
        #     email = context["data"]["email"]
        #     password = context["data"]["password"]
        #     if not login(email, password):
        #         response["data"]["response"] = INVALID_LOGIN
        #         context["action"] = ASK_IF_TO_RETRY
        #         return response
        #     else:
        #         user = User.objects.get(email=email, password=password)
        #         session_key = start_new_session_and_get_key(user)
        #         response["data"]["response"] = "Welcome "+user.first_name
        #         response["data"]["user"] = user
        #         response["data"]["session_key"] = session_key
        #         return response
        #
        # if context["action"] == "GET_EMAIL":
        #     email = parameters.get('email')
        # password = parameters.get('password')
        # first_name = parameters.get('first_name')
        #
        # try:
        #     if not email_validation(email):
        #         response = "Invalid email."
        #     else:
        #         User.objects.create(email=email, password=password, first_name=first_name)
        #         user = User.objects.get(email=email, password=password)
        #         response = "Signed up!"
        # except:
        #     response = "User registration not successful"

    return response
