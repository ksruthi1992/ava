# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from requests import get
from dashboard.constants import *
from dashboard.models import Command, SmallTalk, Recipe, User


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
        query = request.data["query"]

        if "mode" in request.data:
            mode = int(request.data["mode"])
        else:
            mode = MODE_DEFAULT


        if query == "mode?":
            response = str(mode)
        elif query == "blade":
                mode = MODE_BLADE
                response = "mode changed to " + str(mode)
        elif query == "default":
                mode = MODE_DEFAULT
                response = "mode changed to " + str(mode)
        elif mode == MODE_BLADE:
            print mode
            api_url = "http://api.wolframalpha.com/v2/result"
            api_key = "57H75L-P7L8U2J9HP"
            response = get(url=api_url,params={"appid":api_key, "i":query} )
        else:
            try:
                response = SmallTalk.objects.get(query=query).response
            except:
                response = "Sorry, i do not understand..."

        print response
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
        frstname = request.data["firstname"]
        lstname = request.data["lastname"]
        email = request.data["email"]
        uname = request.data["uname"]
        pwd = request.data["pwd"]
        flag = 0
        try:
            User.objects.get(Username = uname)
        except:
            res = "username does not exist"
            flag += 1
        try:
            User.objects.get(email = email)
        except:
            res = "email does not exist"
            flag += 1
        if flag == 2 :
            User.objects.create(firstname = frstname, lastname = lstname, email = email, username = uname, password = pwd)
            res = "created successfully"
        return Response (res)

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
