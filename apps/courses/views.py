# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class CourseListView(View):
    def get(self, request):
        all_course = Course.objects.all()
        return render(request, "course-list.html", {
            "all_course": all_course,

        })


