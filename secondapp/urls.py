from django.urls import path

from secondapp import views

urlpatterns = [
    path('apphome', views.app_home),
    path('work',views.work_fun)
]