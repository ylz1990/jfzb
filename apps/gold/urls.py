from django.urls import path
from . import views


app_name = 'gold'

urlpatterns = [
    path("",views.GoldCollegeView.as_view(),name="gold"),
    path("college/",views.CollegeView.as_view(),name="college"),
    path("college2/",views.College2View.as_view(),name="college2"),
    path("college3/",views.College3View.as_view(),name="college3"),
    path("college4/",views.College4View.as_view(),name="college4"),
    path("college5/",views.College5View.as_view(),name="college5"),
    path("college6/",views.College6View.as_view(),name="college6"),
    path("college7/",views.College7View.as_view(),name="college7"),
    path("college_info/<int:new_id>",views.CollegeInfoView.as_view(),name="college_info"),
]