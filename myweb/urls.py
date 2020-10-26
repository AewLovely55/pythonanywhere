from django.urls import path, include
from django.contrib.auth import views as aunt_views
from . import views

urlpatterns = [
   path('', aunt_views.LoginView.as_view(template_name='myweb/login.html'), name='login'),
   #path('', aunt_views.LogoutView.as_view(template_name='myweb/logout.html'), name='logout'),
   path('login',views.login, name='login'),
   path('index', views.index, name='index'),
   path('signup', views.signup, name='signup'),
   #path('logout',views.logout, name='logout'),
   path('mulan', views.mulan , name='mulan'),
   path('tenet', views.tenet , name='tenet'),
   path('pmak', views.pmak , name='pmak'),
   path('jom', views.jom , name='jom'),
   path('bad', views.bad , name='bad'),
   path('onward', views.onward , name='onward'),
   path('bwa', views.bwa , name='bwa'),
   path('alive', views.alive , name='alive'),
   path('extr', views.extr , name='extr'),
   path('ct', views.ct , name='ct'),
   path('eng', views.eng , name='eng'),
   path('th', views.th , name='th'),
   path('ka', views.ka , name='ka'),
]