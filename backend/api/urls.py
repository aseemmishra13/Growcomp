from django.urls import path
from . import views

urlpatterns=[
    path('',views.getRoutes,name="routes"),
    path('result/walmart/<str:pk>/',views.getResultWalmart,name='walmartresult'),
    path('result/amazon/<str:pk>/',views.getResultAmazon,name='amazonresult'),
    path('result/harris/<str:pk>/',views.getResultHarris,name='harrisresult'),
    path('result/target/<str:pk>/',views.getResultTarget,name='targetresult')

]
