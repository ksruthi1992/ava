# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import ast
import json
import re
from django.shortcuts import render
from django.db import connection

# Create your views here.
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from requests import get
from dashboard.constants import *



from rest_framework.authtoken.models import Token

from dashboard.controller import perform_intent_function_and_get_response
from dashboard.models import Command, SmallTalk, Recipe, User, Pantry, Ingredient, Recipe_Direction, Direction, \
    Recipe_Ingredient

from dashboard.utils import prepare_response, prepare_res, check_parameters, check_and_get_req_count, \
    prepare_response_not_auth


class Dashboard(TemplateView):
    def post(self, request, *args, **kwargs):
        template_name = "dashboard.html"
        query = "No query"
        response = "Sorry, i do not understand"
        context = {'query': query, 'response': response}

        if request.POST['query']:
            query = request.POST['query'].lower().strip()
            print query
            try:
                response = SmallTalk.objects.get(query=query).response
            except:
                response = "Sorry, i do not understand..."

            context = {'query':query, 'response':response, '':''}
        return render(request, template_name, context={'context':context})

    template_name = "dashboard_v2.html"

# class TemplateLoader(APIView):
#     def get(self, request, *args, **kwargs):
#         return Response(render(kwargs[]))

class RecipeAdmin(TemplateView):
    template_name = "recipe-admin.html"


class UserProfile(APIView):

    def get(self, request, *args, **kwargs):
        user_id = int(self.kwargs['user_id'])
        user = User.objects.get(id=user_id)
        message = "user "+user.id
        request_count = 1
        elements = {
            "username":user.username,
            "email":user.email,
            "first_name":user.first_name,
            "last_name":user.last_name,
        }

        response = prepare_res(ava_response=message,request_count=request_count ,elements=elements )
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user_id = int(self.kwargs['user_id'])

        try:
            user_id_token = request.auth
            print user_id_token
        except Exception as e:
            response = prepare_response_not_auth(request.data)
            print e
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        if user_id != user_id_token:
            print user_id
            print 'url!=token_id'
            print user_id_token
            response = prepare_response_not_auth(request.data)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        req_parameters = ['username', 'email', 'first_name','last_name']

        parameter_check = check_parameters(req_parameters, request.data)

        if parameter_check.status_code != 200:
            return parameter_check

        request_count = check_and_get_req_count(request.data)

        user = User.objects.get(id= user_id)
        user.username = request.data['username']
        user.username = request.data['email']
        user.username = request.data['first_name']
        user.username = request.data['last_name']
        user.save()
        message = "User profile updated successfully!"

        response = prepare_res(ava_response=message, request_count=request_count, elements={})
        return Response(response, status=status.HTTP_200_OK)

class AvaRecipe(APIView):
    def get(self, request, *args, **kwargs):
        message = ""
        request_count = 1
        user_ingredients = []

        # user_ingredients = Pantry.objects.filter(user_id=user_id)

        elements = {
            "ingredients": user_ingredients
        }

        response = prepare_res(ava_response=message,request_count=request_count,elements=elements)
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        message = ""
        # request_count =
        elements = {

        }

        response = prepare_res(ava_response=message, request_count=request_count, elements=elements)
        return Response(response, status=status.HTTP_200_OK)

class MainController(APIView):
    def post(self, request, *args, **kwargs):
        # request keys
        # request_count
        # user_info: guest, registered
        print request.data
        try:
            request_count = int(request.data["request_count"]) + 1
            user_info = request.data["user_info"]
        except:
            request_count = 1
            user_info = 0
            pass
        response = {}

        if "user_query" in request.data:
            #     perform search
            user_query = request.data["user_query"]

            if user_query == 'signup':
                ava_response = "I assure, it'll be our little secret! "
                element = {
                    "action": "signup",
                }
                response = prepare_res(ava_response, request_count, element)
                return Response(response, status=status.HTTP_200_OK)

            if user_query == 'login':
                if user_info == 1:
                    ava_response = "You are already logged! Do you want to logout ? "
                    element = {
                        "action": "login",
                    }
                else:
                    ava_response = "Hmmm...<br> Do i know you ?! "
                    element = {
                        "action": "login",
                    }
                response = prepare_res(ava_response, request_count, element)
                return Response(response, status=status.HTTP_200_OK)

            ava_response = " How about these -"
            element = {
                "action":"search_result",
                "user_query": "We are looking for: "+ user_query,
                "options":[
                    {"title":"Lasagne"},
                    {"title":"Pastaawdawd"},
                    {"title":"Pizza"}
                ]
            }
            response =  prepare_res(ava_response, request_count,element)
            return Response(response, status=status.HTTP_200_OK)

        if request_count == 1 :
            ava_response = "Hello!<br> What are you hungry for, today? "
            element = {
                    "action":"search"
                        }

            response = prepare_res(ava_response, request_count, element)
            print response
            return Response(response, status=status.HTTP_200_OK)
        else:
            ava_response = "Hello again!<br> What are you hungry for, today? "
            element = {
                "action":"search"
            }

            response = prepare_res(ava_response, request_count, element)
            print response
            return Response(response, status=status.HTTP_200_OK)

    # template_name = "dashboard_v2.html"

class Login(APIView) :
    def post(self,request, *args, **kwargs):
        try:
            email = request.data["email"]
            password = request.data["password"]
            request_count = request.data["request_count"]
        except:
            message = "Oops! parameter missing at the server"
            elements = {"action":"search"}
            response = prepare_res(ava_response=message, request_count=1, elements=elements)
            return Response(response, status=status.HTTP_200_OK)

        try:
            user = User.objects.get(email=email , password = password)
            token = Token.objects.get(user_id=user.id)
            print token.key
            message = "Hey there, "+ user.username + "!<br> What are you hungry for today? "
            elements = {"action": "search",
                        "user_id":user.id,
                        "user_token":token.key,
                        "user_image":user.profile_pic}
        except:
            message = "Sorry, invalid username/password! Try again ?"
            elements = {
                "action":"ack",
                "ack":
                    {"action":"login",
                     "response":"There you go!"},
                "nack":
                    {"action":"search",
                     "response":"Anyway, what delicacy were we looking for then ? "}
                       }
        response = prepare_res(ava_response=message, request_count= request_count, elements=elements)
        return Response(response, status=status.HTTP_200_OK)

class UserSignup(APIView):
    def post(self,request, *args, **kwargs):

        try:
            email = request.data["email"]
            username = request.data["username"]
            password = request.data["password"]
            request_count = int (request.data["request_count"]) + 1
        except:
            message = "Oops! There seems to be a problem getting a parameter at the server. My bad! "
            element = {
                "action": "search"
                }
            response = prepare_res(ava_response=message, request_count=1, elements=element)
            return Response(response, status=status.HTTP_200_OK)

        flag = 0
        try:
            User.objects.get(username=username)
            flag = 1
        except:
            pass

        try:
            User.objects.get(email=email)
            flag = 1
        except:
            pass

        if flag != 0:
            message = "email/username already exists, do you want to try login instead? "
            element = {
                "action":"ack",
                "ack":
                    {"action":"login",
                     "response":"There you go!"},
                "nack":
                    {"action":"signup",
                     "response":"Okay then, Try again!"}
                       }
            response  = prepare_res(ava_response=message,request_count=request_count,elements=element)
            return Response(response, status=status.HTTP_200_OK)

        else:

            User.objects.create(username = username, email= email, password= password)
            user = user = User.objects.get(username=username, password=password)
            token = Token.objects.create(user=user)
            message = "Registration  complete!<br> So what are you hungry for today, "+ user.username + " ?"
            element = {
                "action":"search",
                "user_token": token.key,
                "user_id": user.id,
                "user_name": user.username,
                "user_image": user.profile_pic
            }
            response = prepare_res(ava_response=message, request_count = request_count, elements=element)
            return Response(response, status= status.HTTP_200_OK)

class UserProfileView(APIView):
    def get(self, request):
        self.user = request.user
        self.userdetails = User.objects.get(username=self.user)
        if (self.userdetails):
            for details in self.userdetails:
                print details.firstname
                print details.lastname
                print details.email
                print details.username
                print details.password
                print details.dob

class ContactView(APIView) :
    def post(self,request, *args, **kwargs):
        Email = request.data["email"]
        Username = request.data["username"]
        Recipe = request.data ["recipe"]
        Message = request.data ["message"]
        flag = 0
        try:
            User.objects.get(username = username)
            res = "username does not exists"
        except:
            res = "username exist"
            flag += 1
        try:
            User.objects.get(email = email)
            res = "email already exists"
        except:
            res = "email does not exist"
            flag += 1
        if flag == 2 :
            User.objects.create(Email = email, Username = username, Recipe = recipe, Message = message).save()
            token = Token.objects.create(user= user)
            res = "Feedback Sent"

        res = {"message":res}
        return Response (res)

class UserProfileView(APIView):
    def get(self, request):
        self.user = request.user
        self.userdetails = User.objects.get(username=self.user)
        if (self.userdetails):
            for details in self.userdetails:
                print details.firstname
                print details.lastname
                print details.email
                print details.username
                print details.password
                print details.dob

class Contact(APIView) :
    def post(self,request, *args, **kwargs):
        Username = request.data["Username"]
        Email = request.data["email"]
        Message = request.data["message"]
        Recipe = request.data["recipe"]

        flag = 0
        try:
            User.objects.get(username = username)
            res = "Username does not exist"
        except:
            res = "Correct Username"
            flag += 1
        try:
            User.objects.get(email = email)
            res = "email already exists"
        except:
            res = "email does not exist"
            flag += 1
        if flag == 2 :
            User.objects.create(Email = email, Username = username, Message = message, Recipe = recipe).save()
            user = User.objects.get(username=username, Email = email)
            token = Token.objects.create(user= user)
            res = "Feedback Sent"

        res = {"message":res}
        return Response (res)



class Pantry(APIView):
    def get(self,request):
        try:
            #self.user_id = request.session(session_key)
            #self.user = request.user
            #self.user_item_list = Pantry.objects.filter(user_id=self.user_id)
            #user_item_list = Pantry.objects.filter(user_id=self.user_id).exclude(is_removed=True)
            user_item_list = Pantry.objects.all().exclude(is_removed=True)
            name = []
            for e in user_item_list:
                name.append(e["ingredient_id"])

            return Response({"ingredients": name})


        except:
            print 'No pantry items added by this user'
        return Response({"ingredients":["tomatoes", "potatoes"]})


    def post(self,request):
        count_ingredient = Ingredient.objects.raw('SELECT 1 id , COUNT(*) AS total_count from dashboard_ingredient')
        for obj in count_ingredient:
            count_ingredient =  obj.total_count
        print count_ingredient
        myDict = dict((request.data).iterlists())


        # Require session key to test the code

        # user_id = request.session(session_key)



        user_id=1;
        user = User.objects.get(id=user_id)
        for key, values in myDict.items():
            #for loop checks for each ingredient if its present or absent in both dashboard_pantry and dashboard_ingredient
            for v in values:
                if count_ingredient == 0 and request.session[user_id]==user.id:    #***
                    #used request.session for logged in users and to maintain their pantry
                    #this is used to check if both tables are empty and create selected pantry entries
                    new_ingredient = Ingredient.objects.create(name=v).save()
                    new_in_pantry = Pantry.objects.create(ingredient_id=new_ingredient.id, user_id=user.id, is_removed=False)
                elif request.session[user_id]==user.id:
                    try:
                        #if_present try block will  not throw an exception
                        #if absent exception block will execute
                        ingredient_obj = Ingredient.objects.get(name=v)

                        if Pantry.objects.get(id=ingredient_obj.id):
                            update_field = Pantry.objects.get(id=ingredient_obj.id)
                            update_field.is_removed = False
                            update_field.save()

                        else:
                            Pantry.objects.create(ingredient_id = ingredient_obj.id,user_id=user.id,is_removed=False)
                            msg = "already existed ingredient"

                    except:
                        msg = "ingredient doesnot exist"
                        new_ingredient = Ingredient.objects.create(name=v).save()
                        new_in_pantry = Pantry.objects.create(ingredient_id=new_ingredient.id, user_id=user.id, is_removed=False)

        #below code to update pantry items which are removed my user in user pantry i.e Pantry







        return Response("Pantry Saved", status=status.HTTP_200_OK)

class getRecipe(APIView) :
    def get(self, request, *args, **kwargs):
        template_name = "recipe.html"
        recipe_id = 1
        print recipe_id
        recipe = Recipe.objects.get(id = recipe_id)
        title = recipe.title
        print title
        image = recipe.featured_image
        description = recipe.description
        print description
        time = recipe.time
        print time
        serves = recipe.serves
        print serves
        keywords = recipe.keywords
        print keywords

        recipe_directions = Recipe_Direction.objects.filter(recipe_id = recipe_id)
#        print type(recipe_directions)
#       print recipe_directions.direction_id
        steps = []
        for dir in recipe_directions:
            print dir.__dict__
            directionid = dir.direction_id
            print directionid
            direction = Direction.objects.get(id=directionid)
            print direction.description
            steps +=direction.description
        # direction_list = Direction.objects.get(id=directionid)
        ingredient_id = Recipe_Ingredient.objects.filter(recipe_id=recipe_id)
        for ingredient_name in ingredient_id:
            print ingredient_name.__dict__
            ingredients = ingredient_name.ingredient_id
            print ingredients
            ingredients_list = Ingredient.objects.get(id=ingredients)
            print ingredients_list.name

        res = "created successfully"

        res = {"message": res}
        return Response(res)

# class Controller(APIView):
#     def get(self,request, *args, **kwargs):
#         return Response("hey",status=status.HTTP_200_OK)
#
#     def post(self,request, *args, **kwargs):
#
#         response = {}
#         response["mode"] = AVA_MODES[DEFAULT_MODE]
#         response["data"] = {}
#         context = {}
#         print request.data
#         print request.data
#         from ava.settings import STATIC_URL
#         if request.data["query"] in ["italian pasta","pasta", "italian", "white pasta", "pasta"]:
#             response = prepare_response(response=" Here are some : <a href='http://localhost:63342/ava/dashboard/templates/recipe.html?_ijt=vv33bkmao9s33hp2ndmfniajru'>White Pasta</a>, <a href='http://localhost:63342/ava/dashboard/templates/recipe.html?_ijt=vv33bkmao9s33hp2ndmfniajru'>Chicken pasta</a>")
#             return Response(response)
#
#         if request.data["query"] in ["spicy", "something spicy"]:
#             response = prepare_response(response=" Okay! I narrowed them down to these : <a href='http://localhost:63342/ava/dashboard/templates/recipe.html?_ijt=vv33bkmao9s33hp2ndmfniajru'>White Pasta</a>")
#             return Response(response)
#
#         try:
#             query = str(request.data["query"]).lower()
#             mode = int(request.data["mode"])
#         except:
#             response["response"] = API_PARAMETERS_MISSING_RESPONSE
#             return Response(prepare_response(response=response))
#
#         if "context" not in request.data:
#             context = {}
#         else:
#             if type(request.data["context"]) == 'str':
#                 context = ast.literal_eval(request.data["context"])
#             else:
#                 context = request.data["context"]
#
#         if "intent" not in request.data or "action" not in request.data:
#             intent = INTENT_DEFAULT
#             action = ACTION_DEFAULT
#
#             prev_intent = INTENT_DEFAULT
#             prev_action = ACTION_DEFAULT
#
#         else:
#
#             intent = str(request.data["intent"])
#             action = str(request.data["action"])
#
#
#
#         commands = {"login": {"intent": INTENT_LOGIN, "action": ASK_FOR_EMAIL},
#                     "register": {"intent": INTENT_REGISTER, "action": ASK_FOR_EMAIL}}
#
#         if query in commands:
#             intent = commands[query]["intent"]
#             action = commands[query]["action"]
#
#         response["intent"] = intent
#         response["action"] = action
#         response["context"] = context
#         response["error"] = False
#         response["message"] = ""
#
#         response["data"]["response"] = "Hey there!"
#
#         if "context" in request.data:
#                 if "user" in request.data["context"] or "session_key" in request.data["context"]:
#                     response["data"]["session_key"] = request.data["context"]["session_key"]
#                     response["data"]["user"] = request.data["context"]["user"]
#
#         # switch mode intent
#         if intent == INTENT_SWITCH_MODE:
#             if query in AVA_MODES:
#                 response["mode"] = AVA_MODES.get(query)
#
#                 response["data"]["response"] = "Mode changed to " + mode
#                 return Response(response)
#             else:
#                 response["data"]["response"] = "Hmmm...no such mode exits"
#                 return Response(response)
#
#         # study intent and perform action if required [that can be performed with or without params]
#         response = perform_intent_function_and_get_response(request, response, query, intent, action, context)
#         response = prepare_response(query=query, mode=response["mode"], intent=response["intent"], action = response["action"],context=response["context"], response=response["data"]["response"])
#         return Response(response)