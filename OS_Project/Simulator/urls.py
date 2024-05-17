from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('SRTN',views.SRTN, name="srtn"),
    path('SRTN/result',views.SRTN_result, name="SRTN-result"),
    path('producer-consumer',views.Producer_consumer, name="producer-consumer"),
    path('sstf',views.SSTF, name="sstf"),
    path('page-replacement',views.PageReplacement, name="page-replacement"),
]