from django.shortcuts import render
from django.views import View
from .models import Case
from django.core.paginator import Paginator
# Create your views here.

# http://www.dyhjw.com/mjcenter/710.html
class CaseView(View):
    """
    显示专家解读
    """
    def get(self,request):
        news_all_list = Case.objects.only("id","content","image_url").filter(case_type=1).order_by("-created_time")
        paginator = Paginator(news_all_list, 5)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request, "cases/case.html",locals())

class Case2View(View):
    """
    显示专家解读
    """
    def get(self,request):
        news_all_list = Case.objects.only("id","content","image_url").filter(case_type=2).order_by("-created_time")
        paginator = Paginator(news_all_list, 5)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request, "cases/case_2.html",locals())


class Case3View(View):
    """
    显示专家解读
    """
    def get(self,request):
        news_all_list = Case.objects.only("id","content","image_url").filter(case_type=3).order_by("-created_time")
        paginator = Paginator(news_all_list, 5)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request, "cases/case_3.html",locals())

class Case4View(View):
    """
    显示专家解读
    """
    def get(self,request):
        news_all_list = Case.objects.only("id","content","image_url").filter(case_type=4).order_by("-created_time")
        paginator = Paginator(news_all_list, 5)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request, "cases/case_4.html",locals())

class CaseInfoView(View):
    """
    显示大咖论道详情
    """
    def get(self,request,new_id):
        new = Case.objects.get(id=new_id)
        previoud_new = Case.objects.filter(created_time__lt=new.created_time).last()
        next_new = Case.objects.filter(created_time__gt=new.created_time).first()
        new.read_num += 1
        new.save()
        return render(request, "cases/case_info.html",locals())