from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


def func(request):
    return render(request, 'func_templates.html')


# class Class_temp(TemplateView):
#     template_name = 'class_templates.html'