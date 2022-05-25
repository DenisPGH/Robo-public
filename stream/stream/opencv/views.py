from django.shortcuts import render
from  django.views import generic as view_dj
# Create your views here.

class IndexView(view_dj.TemplateView):
    template_name = 'index.html'