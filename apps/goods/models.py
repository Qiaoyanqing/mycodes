from django.db import models

# Create your models here.
from django.shortcuts import reverse
from django.utils import timezone
import uuid
from tinymce.models import HTMLField
from apps.sorts.models import SortType

class Goods(models.Model):
 goods_id = models.UUIDField(primary_key=True, auto_created=True,default=uuid.uuid4, verbose_name='uuid', editable=False)
 goods_name = models.CharField(max_length=30, verbose_name='商品名称', blank=True,unique=True)
 goods_brief = models.CharField(max_length=255, verbose_name='商品简介', blank=True,unique=True)
 goods_detail = HTMLField(verbose_name='商品详情', blank=True)
 goods_image = models.ImageField(verbose_name='商品图⽚',upload_to='goods_image/%Y/%m/%d', default="goods_image/default.png", blank=True)
 goods_type = models.ForeignKey(SortType, related_name='SortType',on_delete=models.CASCADE, verbose_name='商品类别',default=1)
 goods_status = models.IntegerField(verbose_name='商品状态', choices=((1, '有货'),(2, '缺货')), default=1)
 goods_enable = models.BooleanField(verbose_name='可⽤状态', choices=((True, '开启'),(False, '关闭')),default=True)
 cost_price = models.FloatField(verbose_name='原来价格', default=0)
 actual_price = models.FloatField(verbose_name='实际价格', default=0)
 sale_nums = models.IntegerField(verbose_name='商品销量', default=0)
 storage_nums = models.IntegerField(verbose_name='库存销量', default=0)
 view_nums = models.IntegerField(verbose_name='浏览量', default=0)
 created_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)

 def get_good_url(self):
   return reverse('goods:goods_detail',kwargs={'pk':self.goods_id})

 class Meta:
    verbose_name = "商品信息"
    verbose_name_plural = verbose_name
    ordering = ('created_time', )

 def __str__(self):
    return self.goods_name