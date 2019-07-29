from django.urls import path
from . import views


app_name = 'cases'

urlpatterns = [
    path("",views.CaseView.as_view(),name="cases"),
    path("cases_2",views.Case2View.as_view(),name="cases_2"),
    path("cases_3",views.Case3View.as_view(),name="cases_3"),
    path("cases_4",views.Case4View.as_view(),name="cases_4"),
    path("case_info/<int:new_id>",views.CaseInfoView.as_view(),name="case_info"),
]