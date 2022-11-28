from django.urls import path
from . import views


urlpatterns = [

    path('chasma/', views.changechasma),
]