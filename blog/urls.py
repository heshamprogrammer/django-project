from django.urls import path,include
from . import views

urlpatterns = [
    # path('hi', views.add),
    path('index' , views.index, name='index'),
    path('add', views.addition , name='add'),
    path('Subtract', views.Subtract , name='Subtract'),
    path('hit', views.hit , name='hit'),
    path('portion', views.portion , name='portion'),
]
