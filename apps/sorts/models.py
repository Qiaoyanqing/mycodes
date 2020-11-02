
# Create your models here.
from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.utils.html import format_html

class SortType(models.Model):
 sort_id = models.AutoField(primary_key=True)
 sort_name = models.CharField(max_length=30, verbose_name='分类名称', blank=True)
 sort_detail = models.CharField(max_length=50, verbose_name='分类描述', blank=True)
 sort_image = models.ImageField(verbose_name='分类图⽚',upload_to='sort_images/%Y/%m/%d', default="sort_images/default.png", blank=True)
 sort_level = models.IntegerField(verbose_name='分类级别')
 parent_id = models.ForeignKey('self', null=True, blank=True,on_delete=models.CASCADE, verbose_name='⽗级分类')
 show_flag = models.IntegerField(verbose_name='显示标记', default=1) # 显示位置 0 表示不显示，1 表示主⻚显示
 priority = models.IntegerField(verbose_name='显示优先级', default=0)
 created_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)

 def get_goods_list_url(self):
     return reverse('goods:goods_list')

 def get_image(self):
    return format_html('<img src="{}"class="field_img">'.format(self.sort_image.url))

 get_image.short_description = format_html('''<span style="color:#428bca;">分类图⽚</span>''')

 def get_absolute_url(self):
     return reverse('goods:goods_list') + '?sort_type=' + str(self.sort_id)

 class Meta:
    verbose_name = "分类信息"
    verbose_name_plural = verbose_name
    ordering = ('created_time', )

 def __str__(self):
    return self.sort_name