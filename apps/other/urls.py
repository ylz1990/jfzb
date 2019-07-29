from django.urls import path
from . import views

app_name = "other"

urlpatterns = [
    path("",views.MessageBoardView.as_view(),name='message'),
]