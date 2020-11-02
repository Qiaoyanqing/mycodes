from django import template
from ..models import SortType
register = template.Library()
@register.simple_tag
def get_sorts_type():
 return SortType.objects.filter(show_flag=1).order_by('-priority')