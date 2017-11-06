# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

from dashboard.models import Command, SmallTalk, Recipe, User, Pantry, Ingredient, Recipe_Direction, Direction, \
    Recipe_Ingredient

from dashboard.utils import prepare_response, perform_intent_function_and_get_response



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

    template_name = "dashboard.html"

class Controller(APIView):
    def get(self,request, *args, **kwargs):
        return Response("hey",status=status.HTTP_200_OK)

    def post(self,request, *args, **kwargs):

        try:
            query = str(request.data["query"]).lower()
            mode = int(request.data["mode"])
            intent = str(request.data["intent"])
            parameters = str(request.data["parameters"])
            context = str(request.data["context"])

        except:
            return Response("API parameters missing.", status=status.HTTP_400_BAD_REQUEST)

        # switch mode intent
        if intent == INTENT_SWITCH_MODE:
            if query in AVA_MODES:
                mode = AVA_MODES.get(query)
                response = "Mode changed to " + mode
            else:
                response = "Hmmm...no such mode exits"
                pass

        # study intent and perform action if required [that can be performed with or without params]
        response = perform_intent_function_and_get_response(intent, parameters, context)

        response = prepare_response(query=query, mode=mode, intent=intent, parameters=parameters, context=context, response=response)
        return Response(response)


class Register(APIView) :
    def post(self,request, *args, **kwargs):
        firstname = request.data["firstname"]
        lastname = request.data["lastname"]
        email = request.data["email"]
        username = request.data["username"]
        password = request.data["password"]
        dob = request.data["dob"]
        profile_pic = request.data["pro_pic"]
        flag = 0
        try:
            User.objects.get(username = username)
            res = "username already exists"
        except:
            res = "username does not exist"
            flag += 1
        try:
            User.objects.get(email = email)
            res = "email already exists"
        except:
            res = "email does not exist"
            flag += 1
        if flag == 2 :
            User.objects.create(first_name = firstname, last_name = lastname, email = email, username = username, password = password, profile_pic = profile_pic).save()
            user = User.objects.get(username=username, password=password)
            token = Token.objects.create(user= user)
            res = "created successfully"

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

# class Feedback(APIView):
#     def post(self,request, *args, **kwargs):
#         Username = models.Charfield(max_length=50)
#         email = models.EmailField()
#         title = models.Charfield(max_length=120)
#         message = models.Textfield()
#         happy = models.Booleanfield()
#
#     def feedback_form(request):
#         if request.method == 'POST':
#             form = Feedback_form(request.POST)
#
#             if form.is_valid():
#                 form.save()
#                 return render(request, 'form/thanks.html')
#  else:
#         form = FeedbackForm()
#      return render(request,'form/feedback_form.html',{'form': form})



class Login(APIView) :
    def post(self,request, *args, **kwargs):
        username = request.data["username"]
        password = request.data["password"]
        try:
            User.objects.get(username = username , password = password)
            res = "Authentication Successful"
        except:
            res = "Username or password is invalid"
        res = {"message": res}
        return Response(res)


class Pantry(APIView):


    form_class = Pantry;
    template_name = "dashboard.html"
    def post(self,request):
        count_ingredient = Ingredient.objects.raw('SELECT 1 id , COUNT(*) AS total_count from dashboard_ingredient')
        for obj in count_ingredient:
            count_ingredient =  obj.total_count
        print count_ingredient
        myDict = dict((request.data).iterlists())


        # Require session key to test the code
        user_id = request.session(session_key)




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

