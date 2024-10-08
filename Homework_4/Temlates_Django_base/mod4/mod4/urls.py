"""
URL configuration for mod4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from temlates_base.views import page1, page2, page3

urlpatterns = [

    path('admin/', admin.site.urls),
    path('page1/', page1, name='page_1'),
    path('page2/', page2, name='page_2'),
    path('page3/', page3, name='page_3'),

]
