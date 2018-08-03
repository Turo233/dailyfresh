# 自定义Django过滤器
from django import template
import re

register = template.Library()

@register.filter(name='F_delete_num')
def F_delete_num(data):
    try:
        pattern = '(.+?)\d'
        data = re.findall(pattern, data)[0]
        return data
    except:
        return data

