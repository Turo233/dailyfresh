from django import template
import re

register = template.Library()

@register.filter(name='F_delete_num')
def F_delete_num(data):
    if data == 1:
        return '已支付'
    else:
        return '未支付'

