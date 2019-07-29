from django.shortcuts import render
from django.views import View
from .models import GoldCollege
from django.core.paginator import Paginator
# Create your views here.


class GoldCollegeView(View):
    """
    显示黄金学院
    """
    def get(self,request):
        return render(request, "gold/goldcollege.html")



class CollegeView(View):
    """
    显示黄金T+D
    """
    def get(self,request):
        news_all_list = GoldCollege.objects.only("id", "title", "created_time").filter(gold_type=1).order_by(
            "-created_time")
        paginator = Paginator(news_all_list, 15)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request, "gold/college.html",locals())


class College2View(View):
    """
    显示纸黄金
    """
    def get(self,request):
        news_all_list = GoldCollege.objects.only("id", "title", "created_time").filter(gold_type=2).order_by(
            "-created_time")
        paginator = Paginator(news_all_list, 15)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request, "gold/college2.html",locals())

class College3View(View):
    """
    显示纸黄金
    """
    def get(self,request):
        news_all_list = GoldCollege.objects.only("id", "title", "created_time").filter(gold_type=3).order_by(
            "-created_time")
        paginator = Paginator(news_all_list, 15)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request, "gold/college3.html",locals())

class College4View(View):
    """
    显示纸黄金
    """
    def get(self,request):
        news_all_list = GoldCollege.objects.only("id", "title", "created_time").filter(gold_type=4).order_by(
            "-created_time")
        paginator = Paginator(news_all_list, 15)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request, "gold/college4.html",locals())

class College5View(View):
    """
    显示纸黄金
    """
    def get(self,request):
        news_all_list = GoldCollege.objects.only("id", "title", "created_time").filter(gold_type=5).order_by(
            "-created_time")
        paginator = Paginator(news_all_list, 15)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request, "gold/college5.html",locals())

class College6View(View):
    """
    显示纸黄金
    """
    def get(self,request):
        news_all_list = GoldCollege.objects.only("id", "title", "created_time").filter(gold_type=6).order_by(
            "-created_time")
        paginator = Paginator(news_all_list, 15)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request, "gold/college6.html",locals())

class College7View(View):
    """
    显示纸黄金
    """
    def get(self,request):
        news_all_list = GoldCollege.objects.only("id", "title", "created_time").filter(gold_type=7).order_by(
            "-created_time")
        paginator = Paginator(news_all_list, 15)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request, "gold/college7.html",locals())

class CollegeInfoView(View):
    """
    显示黄金学院
    """
    def get(self,request,new_id):
        new = GoldCollege.objects.get(id=new_id)
        # 上一篇
        previoud_new = GoldCollege.objects.filter(created_time__lt=new.created_time).last()
        # 下一篇
        next_new = GoldCollege.objects.filter(created_time__gt=new.created_time).first()
        new.read_num += 1
        new.save()
        return render(request, "gold/college_xqy.html",locals())