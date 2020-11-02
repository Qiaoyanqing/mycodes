from django.shortcuts import render
# Create your views here.
from apps.sorts.models import SortType


def index(request):
    sorts = SortType.objects.filter(show_flag=1).order_by('-priority')
    # print(list(sorts))
    context = {
        'sorts': sorts
    }
    return render(request, 'myshop/index2.html', context)