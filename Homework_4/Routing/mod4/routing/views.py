# from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def page1(request):

    phrase = [
            '''My first phrase for pages/page1/
            "You shouldn't feed a shark from your hand."''',
            '''My second phrase for pages/page1/
            "If a shark is looking at you, don\'t get excited"''',
            ]

    phrase_random = random.choice(phrase)
    return HttpResponse(phrase_random)


def page2(request):

    phrase = [
            '''My first phrase for pages/page2/ "Art is a blast."''',
            '''My second phrase for pages/page2/ "Art is beauty."''',
            ]

    phrase_random = random.choice(phrase)
    return HttpResponse(phrase_random)
