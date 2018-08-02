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

@register.filter(name='select_tf')
def select_tf(data):
    if data is True:
        data = '已支付'
    else:
        data = '未支付'
    return data
@register.filter(name='select_tf_pay')
def select_tf_pay(data):
    if data is True:
        data = '已付款'
    else:
        data = '未付款'
    return data