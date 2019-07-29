from django.urls import path
from . import views

app_name = "member"

urlpatterns = [
    path("",views.MemberView.as_view(),name='member'),
    path("member_1/",views.Member1View.as_view(),name='member_1'),
    path("member_2/",views.Member2View.as_view(),name='member_2'),
    path("member_3/",views.Member3View.as_view(),name='member_3'),
    path("detail/<int:new_id>",views.MemberDatailView.as_view(),name='detail'),
]