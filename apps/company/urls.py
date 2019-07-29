from django.urls import path
from . import views

app_name = "company"

urlpatterns = [
    path("",views.CompanyView.as_view(),name="company"),
    path("company_2/",views.Company_2View.as_view(),name="company_2"),
    path("company_3/",views.Company_3View.as_view(),name="company_3"),
]