from django.shortcuts import render
from django.views import View
from .models import News
from django.core.paginator import Paginator
# Create your views here.


class NewsView(View):
    """
    显示君枫财经
    """
    def get(self,request):
        news_all_list = News.objects.only("id","title","created_time","new_type").filter(new_type=1).order_by("-created_time")
        paginator = Paginator(news_all_list,15)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request, "news/xinwenzhongxin.html",locals())



class News2View(View):
    """
    显示黄金头条
    """
    def get(self,request):
        news_all_list = News.objects.only("id","title","created_time","new_type").filter(new_type=2).order_by("-created_time")
        paginator = Paginator(news_all_list,15)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request, "news/xinwenzhongxin_2.html",locals())

class News3View(View):
    """
    显示最新资讯
    """
    def get(self,request):
        news_all_list = News.objects.only("id","title","created_time","new_type").filter(new_type=3).order_by("-created_time")
        paginator = Paginator(news_all_list,15)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request, "news/xinwenzhongxin_3.html",locals())

class NewDetailView(View):
    """
    显示新闻详情页
    """
    def get(self,request,new_id):
        new = News.objects.get(id=new_id)
        # 上一篇
        previoud_new = News.objects.filter(created_time__lt=new.created_time).last()
        # 下一篇
        next_new = News.objects.filter(created_time__gt=new.created_time).first()
        new.read_num += 1
        new.save()
        return render(request, "news/xinwenzhongxin_xqy.html",locals())