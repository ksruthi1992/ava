from django.contrib import messages
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.sessions.backends.db import SessionStore
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.core.validators import validate_email
from django.template.loader import get_template
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from ava import settings
from constants import *
from dashboard.models import User, Recipe, Pantry, Ingredient


def prepare_res(ava_response, request_count, elements):
    response = {"ava_response":ava_response,
                "request_count":request_count,
                "element":elements }
    return response

def get_token_user_from_request(request):

    token = request.META['HTTP_AUTHORIZATION'].split()[1]
    user_token = Token.objects.get(key=token)
    user = User.objects.get(id = user_token.user_id)
    return user

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

def send_reset_mail(user, key):
    url_body = "http://theback.space:8000/users/%s/password_reset/confirm/%s" % (
        user.id, key)
    html_template = get_template('password_reset_email_template.html')
    content_passed_to_template = ({'url_body': url_body})
    html_content = html_template.render(content_passed_to_template)
    send_email = EmailMessage(
        'Ava Password Reset',
        html_content,
        settings.EMAIL_HOST_USER,
        [user.email]
    )
    send_email.content_subtype = "html"
    send_email.send()

def fetch_recipes(request, user_query, request_count):
    try:
        token_user = get_token_user_from_request(request)
        if not token_user:
            raise Exception
        user_type = USER_INFO_REGISTERED
        user_id = token_user.id

    except:
        # guest user
        user_type = USER_INFO_GUEST
        pass

    message = "How about these-"

    # if guest_user
    if user_type == USER_INFO_GUEST:
        print 'fse'
        try:
            # search algorithm
            vector = SearchVector('ingredients_display', weight='C') + SearchVector('title',
                                                                                    weight='A') + SearchVector(
                'description', weight='B')
            query = SearchQuery(user_query, 'A')

            recipes = Recipe.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')[:5]

            # recipes = Recipe.objects.filter(recipe_ingredients__search=user_ingredients)
            recipe_results = []
            rank_count = 1
            for recipe in recipes:
                print str(recipe.rank) + "    " + recipe.title

                recipe_results.append(
                    {"title": recipe.title, "recipe_image": recipe.featured_image, "recipe_id": recipe.id,
                     "rank": recipe.rank})
                rank_count += 1

            elements = {
                "action": "search_result",
                "user-query": user_query,
                "options": recipe_results
            }
        except Exception as e:
            message = "Oops! " + e.message
            elements = {}

    else:
        # if user_logged_in
        try:
            # user_ingredients = Pantry.objects.filter(user_id=user_id)
            user_ingredients_string = Pantry.objects.get(user_id=user_id).pantry_ingredients
            user_ingredients = eval(user_ingredients_string)
            # user_ingredients_string = str(user_ingredients)
            ingredients = []
            ingredients_string = ""
            for i in user_ingredients:
                ingredient = Ingredient.objects.get(id=i)
                ingredients_string += " "
                ingredients_string += ingredient.name
                ingredients.append(ingredient.name)

            # search algorithm
            vector = SearchVector('ingredients_display', weight='C') + SearchVector('title',
                                                                                    weight='A') + SearchVector(
                'description', weight='B')
            query = SearchQuery(user_query, 'A') | SearchQuery(ingredients_string, 'C')

            recipes = Recipe.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')[:5]

            # recipes = Recipe.objects.filter(recipe_ingredients__search=user_ingredients)
            recipe_results = []

            for recipe in recipes:
                print recipe.rank
                recipe_results.append({"title": recipe.title, "recipe_image": recipe.featured_image, "recipe_id":recipe.id, "rank":recipe.rank})

            message = "How about these-"
            elements = {
                "action":"search_result",
                "user-query":user_query,
                "options": recipe_results
            }
        except Exception as e:
            message = "Oops! " + e.message
            elements = {}
    response = prepare_res(ava_response=message, request_count=request_count, elements=elements)
    return Response(response, status=status.HTTP_200_OK)

def send_welcome_mail(user):

    html_template = get_template('welcome_mail_template.html')
    content_passed_to_template = ({'username': user.username})
    html_content = html_template.render(content_passed_to_template)
    send_email = EmailMessage(
        'Welcome to Ava!',
        html_content,
        settings.EMAIL_HOST_USER,
        [user.email]
    )
    send_email.content_subtype = "html"
    send_email.send()

def check_parameters(req_parameters, request_data):
    message = "Good to go!"
    element = {}

    for i in req_parameters:
        if i not in request_data:
            message = "parameter "+i+" missing!"
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