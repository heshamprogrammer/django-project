from django.urls import path,include
from . import views

urlpatterns = [
    path('index' , views.index, name='protfolio'),
    path('courses' , views.courses, name='courses'),
    path('files' , views.files, name='files'),
    path('plans' , views.plans, name='plans'),
    path('friends' , views.friends, name='friends'),
    path('profilepage' , views.profile, name='profile'),
    path('projects' , views.projects, name='projects'),
    path('settings' , views.settings, name='settings'),
    path('test' , views.test, name='test'),
] 
