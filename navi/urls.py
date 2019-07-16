from django.urls import path
from navi.views import Navi_view

app_name = 'navi'

urlpatterns = [
    path('', Navi_view.as_view(), name='home')

]
