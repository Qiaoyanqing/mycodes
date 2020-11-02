from django.shortcuts import render

# Create your views here.

from apps.goods.models import Goods
from apps.sorts.models import SortType


def goods_info(request):
 goods = Goods.objects.all()[0]
 context = {
 'goods_info': goods
 }
 return render(request, 'myshop/goods_info.html', context=context)

def goods_list(request):
 goods = Goods.objects.all()
 sort = SortType.objects.filter(show_flag=1).order_by('-priority','-sort_id')
 context = {
  'goods':goods,
  'sort':sort,
 }
 return render(request,'myshop/shop.html',context)

def goods_detail(request,pk):
 good = Goods.objects.get(goods_id=pk)
 sort = SortType.objects.filter(show_flag=1).order_by('-priority','-sort_id')
 context = {
  'good':good,
  'sort':sort,
 }
 return render(request,'myshop/single-product.html',context)