# Django Random

This project presents a simple game developed using the Django framework.

## Project Overview

The following steps were completed during the development:

1. **Adding the Application**  
   In the file `Django_Random/mod4/mod4/settings.py`, the custom application `random_game` was added to the list of installed apps:

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       
       'random_game',
   ]
   ```

2. **Creating Game Logic**  
   The game logic was implemented in the file `Django_Random/mod4/random_game/views.py`. The game randomly generates three numbers between 0 and 3. If all three numbers are equal, the player wins; otherwise, they are encouraged to try again. Here is the code:

   ```python
   import random
   from django.http import HttpResponse

   def random_gameeee(request):
       num_1 = random.randint(0, 3)
       num_2 = random.randint(0, 3)
       num_3 = random.randint(0, 3)

       if num_1 == num_2 == num_3:
           response = 'Congratulations, all 3 numbers are equal!'

       else:
           response = 'Better luck next time!'

       return HttpResponse(response)
   ```

3. **Configuring Routes**  
   In the file `Django_Random/mod4/mod4/urls.py`, the path to the application was specified as follows:

   ```python
   from django.contrib import admin
   from django.urls import path
   from random_game.views import random_gameeee 

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('game/', random_gameeee),
   ]
   ```

## Game Purpose

The purpose of this mini-game is to provide a simple and engaging experience where players can test their luck by generating random numbers. It encourages players to keep trying until they achieve a winning combination.

# Screenshot of the mini-game
## Winning
![photo](photo/screen_2.png)

## Loss
![photo](photo/screen_1.png)