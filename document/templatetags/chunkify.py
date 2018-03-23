from django import template

from department.models import Department

register = template.Library()


@register.filter(is_safe=True)
def chunk_list(value, chunk_size=Department.objects.count()//2+1):
    for i in range(0, len(value), chunk_size):
        yield value[i:i+chunk_size]
