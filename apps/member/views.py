from django.shortcuts import render
from django.views import View
from .models import Member
from django.core.paginator import Paginator
# Create your views here.



class MemberView(View):
    """
    会员尊享
    """
    def get(self,request):
        news_all_list = Member.objects.only("id", "content", "image_url").filter(member_type=1).order_by(
            "-created_time")
        paginator = Paginator(news_all_list, 5)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request,"member/member.html",locals())

class Member1View(View):
    """
    会员尊享
    """
    def get(self,request):
        news_all_list = Member.objects.only("id", "content", "image_url").filter(member_type=2).order_by(
            "-created_time")
        paginator = Paginator(news_all_list, 5)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request,"member/member_1.html",locals())

class Member2View(View):
    """
    会员尊享
    """
    def get(self,request):
        news_all_list = Member.objects.only("id", "content", "image_url").filter(member_type=3).order_by(
            "-created_time")
        paginator = Paginator(news_all_list, 5)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request,"member/member_2.html",locals())

class Member3View(View):
    """
    会员尊享
    """
    def get(self,request):
        news_all_list = Member.objects.only("id", "content", "image_url").filter(member_type=4).order_by(
            "-created_time")
        paginator = Paginator(news_all_list, 5)
        page_num = request.GET.get('page', 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request,"member/member_3.html",locals())


class MemberDatailView(View):

    def get(self,request,new_id):
        new = Member.objects.get(id=new_id)
        # 上一篇
        previoud_new = Member.objects.filter(created_time__lt=new.created_time).last()
        # 下一篇
        next_new = Member.objects.filter(created_time__gt=new.created_time).first()
        new.read_num += 1
        new.save()
        return render(request,"member/member_detail.html",locals())