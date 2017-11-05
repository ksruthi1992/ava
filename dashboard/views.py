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

from dashboard.models import Command, SmallTalk, Recipe, User , Pantry , Ingredient




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

class Respond(APIView):

    def get(self,request, *args, **kwargs):
        return Response("hey",status=status.HTTP_200_OK)

    def post(self,request, *args, **kwargs):
        query = str(request.data["query"]).lower()

        if "mode" in request.data:
            mode = int(request.data["mode"])
        else:
            mode = MODE_DEFAULT_CODE

        if query == "mode?":
            response = str(mode)
        elif query == MODE_ROOT:
                mode = MODE_ROOT_CODE
                response = "mode changed to " + str(mode)
        elif query == MODE_DEFAULT:
                mode = MODE_DEFAULT_CODE
                response = "mode changed to " + str(mode)
        elif mode == MODE_ROOT_CODE:
            api_url = "http://api.wolframalpha.com/v2/result"
            api_key = "57H75L-P7L8U2J9HP"
            response = get(url=api_url,params={"appid":api_key, "i":query} )
        else:
            try:
                response = SmallTalk.objects.get(query=query).response
            except:
                response = "Sorry, i do not understand..."

        res = {"query":query, "response": response, "mode": mode}

        return Response(res)

class Sruthi(APIView):
    def get(self,request, *args, **kwargs):
        return Response("hey",status=status.HTTP_200_OK)
    def post(self,request, *args, **kwargs):
        query = request.data["query"]
        res = {"query":query, "response": "hey"}

        return Response(res)

class Neha(APIView):
    def get(self,request, *args, **kwargs):
        return Response("Hello!",status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        query = request.data["query"]
        res = {"query":query, "response": "heyy"}

        return Response(res)

class Vidhya(APIView):
    def get(self, request, *args, **kwargs):
        return Response("Hi!", status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        query = request.data["query"]
        res = {"query": query, "response": "heyy"}

        return Response(res)

class Angelica(APIView):
    def get(self,request, *args, **kwargs):
        return Response("hey",status=status.HTTP_200_OK)
    def post(self,request, *args, **kwargs):
        query = request.data["query"]
        res = {"query":query, "response": "hey"}

        return Response(res)

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
        self.userdetails = Users.objects.get(username=self.user)
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
        form = self.form_class(request.POST)
        #vegie = request.data["onion"]
        #list1 = []
        count = Ingredient.objects.raw('SELECT 1 id , COUNT(*) AS total_count from dashboard_ingredient')
        for obj in count:
            count =  obj.total_count
        print count
        myDict = dict((request.data).iterlists())
        for key, values in myDict.items():
            for v in values:
                if count == 0:
                    Ingredient.objects.create(name=v).save()
                else:
                    try:
                        Ingredient.objects.get(name=v)
                        msg = "already existed ingredient"
                    except:
                        msg = "ingredient doesnot exist"





        return Response("Pantry Saved", status=status.HTTP_200_OK)