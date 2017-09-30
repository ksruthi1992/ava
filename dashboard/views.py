# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from dashboard.models import Command, SmallTalk


class Dashboard(TemplateView):
    def post(self, request, *args, **kwargs):
        template_name = "dashboard.html"
        to_remember = {}
        query = ""
        action_to_be_taken = ""
        response = ""
        mode = ""
        done_flag = 0
        print request.POST
        try:
            if 'query' in request.POST:
                query = request.POST['query']
                print query
            else:
                response = "Hey there!"
                raise Exception(response)

            params = ['response', 'mode', 'action_to_be_taken', 'to_remember']

            for param in params:
                if param not in request.POST:
                    response = param + " not found"
                    raise Exception(response)
                else:
                    response = str(request.POST['response'])
                    mode = str(request.POST['mode'])
                    action_to_be_taken = str(request.POST['action_to_be_taken'])
                    temp = request.POST['to_remember']
                    print type(temp)
                    to_remember = json.loads(str(temp))
                    print type(to_remember)

            if query == 'command':
                mode = 'command_mode'
                action_to_be_taken = 'command_input'
                response = "--*--*--"
                to_remember = {}
            else:
                if action_to_be_taken == 'command_input':
                    command = str(query)

                    try:
                        cmd = Command.objects.get(command=command)
                    except Exception as e:
                        raise Exception('Command not found'+e)
                    mode = 'learn_mode'
                    response = "Mode changed to " + mode + "."
                    response += " User query: "
                    action_to_be_taken = 'learn_input'
                    done_flag = 1

                if mode == 'learn_mode' and done_flag == 0:
                    if action_to_be_taken == 'learn_input' or (action_to_be_taken == "ask_if_continue" and
                                                                       query == "yes") :
                        response = "ava response to query :"
                        action_to_be_taken = "save_dialogue"
                        to_remember = {"query":query}
                        done_flag = 1

                    if action_to_be_taken == "save_dialogue" and done_flag == 0:
                        print "fafsas"
                        query_to_save = to_remember["query"]
                        response_to_save = query
                        print "sada"
                        small_talk_object = SmallTalk.objects.create(query=query_to_save, response= response_to_save)
                        small_talk_object.save()
                        response = "Noted! Continue with "+ mode +" mode ?"
                        action_to_be_taken = "ask_if_to_continue"

                    if query == 'exit' and done_flag == 0:
                        response = "okay then! back to business..."
                        mode = 'dialogue_mode'

            context = {'query': query,
                       'response': response,
                       'mode': mode,
                       'action_to_be_taken': action_to_be_taken,
                       'to_remember': to_remember}

            return render(request, template_name, context={'context':context})

        except Exception as e:

            context = {'query': query,
                       'response': e,
                       'mode': mode,
                       'action_to_be_taken': action_to_be_taken,
                       'to_remember': to_remember}

            return render(request, template_name, context={'context':context})

    template_name = "dashboard.html"

