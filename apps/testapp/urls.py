
from django.urls import path
from apps.testapp import views
app_name = '[testapp]'
urlpatterns = [
 path('current_datatime/', views.current_datetime, name='current_datatime'),

 path('test_template/', views.test_template, name='test_template'),
]


