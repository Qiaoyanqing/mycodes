"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from apps.users import views
app_name = '[users]'
urlpatterns = [
 path('get_user/', views.get_user, name='get_user'),

 path('get_userinfo/<int:id>', views.get_userinfo, name='get_userinfo'),

 path('add2num', views.add2num, name='add2num'),

 path('login', views.login, name='login'),

 path('login_register', views.login_register, name='login_register'),

 path('register', views.register, name='register'),

 path('current_time/', views.current_datetime, name='current_time'),

 path('login_index', views.login_index, name='login_index'),
]

