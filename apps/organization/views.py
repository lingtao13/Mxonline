from django.core.paginator import PageNotAnInteger, Paginator
from django.shortcuts import render

# Create your views here.
from django.views import View

from organization.models import CourseOrg, CityDict


from django.views.generic.base import View
# 处理课程机构列表的view
class OrgView(View):
    def get(self,request):
        # 查找到所有的课程机构
        all_orgs = CourseOrg.objects.all()
        org_nums = all_orgs.count()

        #城市
        all_citys = CityDict.objects.all()

        return render(request, "org-list.html", {
            "all_orgs":all_orgs,
            "all_citys": all_citys,
            "org_nums":org_nums
        })


