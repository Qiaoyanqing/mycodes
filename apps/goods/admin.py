from django.contrib import admin

# Register your models here.
from .models import Goods


class GoodsAdmin(admin.ModelAdmin):
 list_display = ('goods_name','goods_type','goods_status', 'goods_enable',
'actual_price', 'storage_nums', 'created_time')
 list_filter = ('goods_status', 'goods_enable')
 list_editable = ['goods_enable', 'goods_status']
 ordering = ( 'actual_price', 'goods_type', 'goods_name','created_time')

 class Media:
  js = [
  'tinymce/jquery.tinymce.min.js',
  'tinymce/tinymce.min.js',
  'tinymce/js/textareas.js'
  ]

# 在admin中注册绑定
admin.site.register(Goods, GoodsAdmin)
