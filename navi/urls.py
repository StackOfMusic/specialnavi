from django.urls import path
from navi.views import *

app_name = 'navi'

urlpatterns = [
    path('', Navi_view.as_view(), name='home'),
    path('chart/', ChartView.as_view(), name='chart')
]
