from django.shortcuts import render
from django.views import View
from .models import Company
# Create your views here.


class CompanyView(View):
    """
    显示公司详情
    """
    def get(self,request):
        new = Company.objects.get(company_type=1)
        return render(request, "company/company.html", locals())


class Company_2View(View):
    """
    显示公司详情
    """
    def get(self,request):
        new = Company.objects.get(company_type=2)
        return render(request, "company/company_2.html", locals())

class Company_3View(View):
    """
    显示公司详情
    """
    def get(self,request):
        new = Company.objects.get(company_type=3)
        return render(request, "company/company_3.html", locals())