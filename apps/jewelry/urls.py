from django.urls import path
from . import views

app_name = "jewelry"

urlpatterns = [
    path("",views.JewelryView.as_view(),name="jewelry"),
    path("jewelry_2",views.Jewelry_2View.as_view(),name="jewelry_2"),
    path("jewelry_3",views.Jewelry_3View.as_view(),name="jewelry_3"),
    path("jewelry_4",views.Jewelry_4View.as_view(),name="jewelry_4"),
    path("jewelry_info/<int:new_id>",views.JewelryDatailView.as_view(),name="jewelry_info"),
]