from django.urls import path
from .views_api import *

urlpatterns = [
    path('access/', LoginView),

    path('register/', RegisterView),
]