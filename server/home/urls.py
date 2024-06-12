from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [path("", views.home), path("get_image", views.get_image)]
