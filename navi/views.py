from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class Navi_view(TemplateView):
    template_name = 'home.html'


class ChartView(TemplateView):
    template_name = 'charts.html'


class TableView(TemplateView):
    template_name = 'tables.html'
