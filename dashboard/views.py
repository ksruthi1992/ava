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
from dashboard.models import Command, SmallTalk, Recipe


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

