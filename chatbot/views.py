import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ListTrainer


class ChatterBotAppView(TemplateView):
    template_name = 'app.html'


class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)
    trainer = ListTrainer(chatterbot)
    i = 0
    while i < 10:
        trainer.train([
        "Hi there!",
        "Hello! How's it going?",
        "It's going great, thanks for asking.",
        "Of course! So what's up?"
        ])
        trainer.train([
        "How are you?",
        "Oh you know. About the same as normal.",
        "Glad to hear you're hanging in there.",
        "For sure dude. So what's up?"
        ])
        trainer.train([
        "I've been working on some stuff lately.",
        "Like what?"
        ])
        trainer.train([
        "So what do you like to do?",
        "I'm a big video game guy, I enjoy all sorts of games."
        ])
        i += 1
    
    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.
        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })