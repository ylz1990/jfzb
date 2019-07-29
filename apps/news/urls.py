from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path("",views.NewsView.as_view(),name='news'),
    path("gold_news",views.News2View.as_view(),name='gold_news'),
    path("news_info",views.News3View.as_view(),name='news_info'),
    path("new_detail/<int:new_id>",views.NewDetailView.as_view(),name='new_detail')
]