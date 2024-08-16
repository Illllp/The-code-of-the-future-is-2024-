from django.shortcuts import render
import random
from django.http import HttpResponse

# Create your views here.


def random_gameeee(request):

    num_1 = random.randint(0, 3)
    num_2 = random.randint(0, 3)
    num_3 = random.randint(0, 3)

    if num_1 == num_2 == num_3:
        response = 'Победа, все 3 числа равны!'

    else:
        response = 'Повезет в следующий раз!'

    return HttpResponse(response)
