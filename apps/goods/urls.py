from django.urls import path, re_path
from apps.goods import views
app_name = '[goods]'
urlpatterns = [
 path('goods_info/', views.goods_info, name='goods_info'),

 path('goods_list/',views.goods_list,name = 'goods_list'),

 path('goods_detail/<str:pk>',views.goods_detail,name = 'goods_detail'),
]