from django.shortcuts import render
from django.views import View
from news.models import News
# Create your views here.


class IndexView(View):
    """
    显示主页页码
    """
    def get(self,request):
        news = News.objects.only("id",'title','created_time').filter(new_type=1).order_by("-created_time")[0:4]
        gold_news = News.objects.only("id",'title','created_time').filter(new_type=2)[0:4]
        news_info = News.objects.only("id",'title','created_time').filter(new_type=3)[0:4]
        return render(request, "index/index.html",locals())
