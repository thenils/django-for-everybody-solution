from django.urls import path
from . import views


urlpatterns = [
    #path('',views.index, name='index'),
    path('owner/', views.owner, name='owner'),
    # path('', views.detail, name='detail'),
]