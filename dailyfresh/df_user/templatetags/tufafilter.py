from django import template

register = template.Library()

@register.filter(name='select_tf')
def select_tf(data):
    if data is True:
        data = '已支付'
    else:
        data = '未支付'
    return data

