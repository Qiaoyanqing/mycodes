# Generated by Django 2.2 on 2020-10-15 16:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sorts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('goods_id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='uuid')),
                ('goods_name', models.CharField(blank=True, max_length=30, unique=True, verbose_name='商品名称')),
                ('goods_brief', models.CharField(blank=True, max_length=255, unique=True, verbose_name='商品简介')),
                ('goods_detail', models.TextField(blank=True, verbose_name='商品详情')),
                ('goods_image', models.ImageField(blank=True, default='goods_image/default.png', upload_to='goods_image/%Y/%m/%d', verbose_name='商品图⽚')),
                ('goods_status', models.IntegerField(choices=[(1, '有货'), (2, '缺货')], default=1, verbose_name='商品状态')),
                ('goods_enable', models.BooleanField(choices=[(True, '开启'), (False, '关闭')], default=True, verbose_name='可⽤状态')),
                ('cost_price', models.FloatField(default=0, verbose_name='原来价格')),
                ('actual_price', models.FloatField(default=0, verbose_name='实际价格')),
                ('sale_nums', models.IntegerField(default=0, verbose_name='商品销量')),
                ('storage_nums', models.IntegerField(default=0, verbose_name='库存销量')),
                ('view_nums', models.IntegerField(default=0, verbose_name='浏览量')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('goods_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='SortType', to='sorts.SortType', verbose_name='商品类别')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品信息',
                'ordering': ('created_time',),
            },
        ),
    ]