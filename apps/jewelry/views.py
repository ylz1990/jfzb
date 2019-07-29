from django.shortcuts import render
from django.views import View
from .models import Jewelry
from django.core.paginator import Paginator
# Create your views here.

class JewelryView(View):
    """
    显示品牌活动
    """
    def get(self,request):
        news_all_list = Jewelry.objects.only("id", "content", "image_url").filter(jewelry_type=1).order_by("-created_time")
        paginator = Paginator(news_all_list, 5)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request,"jewelry/jewelry.html",locals())


class Jewelry_2View(View):
    """
    显示品牌资讯
    """
    def get(self,request):
        news_all_list = Jewelry.objects.only("id", "content", "image_url").filter(jewelry_type=2).order_by("-created_time")
        paginator = Paginator(news_all_list, 5)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request,"jewelry/jewelry_2.html",locals())


class Jewelry_3View(View):
    """
    显示品牌价格
    """
    def get(self,request):
        news_all_list = Jewelry.objects.only("id", "content", "image_url").filter(jewelry_type=3).order_by("-created_time")
        paginator = Paginator(news_all_list, 5)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request,"jewelry/jewelry_3.html",locals())


class Jewelry_4View(View):
    """
    显示知识拓展
    """
    def get(self,request):
        news_all_list = Jewelry.objects.only("id", "content", "image_url").filter(jewelry_type=4).order_by("-created_time")
        paginator = Paginator(news_all_list, 5)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request,"jewelry/jewelry_4.html",locals())


class JewelryDatailView(View):

    def get(self,request,new_id):
        new = Jewelry.objects.get(id=new_id)
        # 上一篇
        previoud_new = Jewelry.objects.filter(created_time__lt=new.created_time).last()
        # 下一篇
        next_new = Jewelry.objects.filter(created_time__gt=new.created_time).first()
        new.read_num += 1
        new.save()
        return render(request,"jewelry/jewelry_detail.html",locals())