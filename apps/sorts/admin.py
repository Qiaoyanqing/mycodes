from django.contrib import admin
from .models import SortType
# Register your models here.

class SorTypeAdmin(admin.ModelAdmin):
 list_display = ('sort_name','get_image','sort_level', 'parent_id', 'show_flag','priority', 'sort_detail')
 list_filter = ('sort_level', 'parent_id')
 list_editable = ['show_flag', 'priority']
 ordering = ( 'sort_level', 'parent_id', 'sort_id','priority')
 # 在admin中注册绑定
admin.site.register(SortType, SorTypeAdmin)