from django.shortcuts import render
from django.views import View
# Create your views here.


class ContractView(View):
    """
    显示联系我们
    """
    def get(self,request):
        return render(request, "other/contract.html")

class MessageBoardView(View):
    """
    显示留言板
    """
    def get(self,request):
        return render(request, "other/message.html")

# class PersonalView(View):
#     """
#     显示个人中心
#     """
#     def get(self,request):
#         return render(request, "other/personal.html")