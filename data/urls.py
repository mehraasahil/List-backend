from django.urls import path

from. import views


urlpatterns = [
   path('',views.getRoutes,name='routes'),
   path('data/',views.getEdata,name='edata'),
   path('data/<str:pk>',views.getEdata,name='edata')
]