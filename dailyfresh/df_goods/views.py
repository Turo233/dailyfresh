from django.shortcuts import render
from django.core.paginator import Paginator
from .models import TypeInfo
from .models import GoodsInfo

# Create your views here.

def index(request):
    TypeInfo_list = TypeInfo.objects.all()
    id_1_info = TypeInfo_list[0].goodsinfo_set.order_by('-id')[0:4]
    id_2_info = TypeInfo_list[1].goodsinfo_set.order_by('-id')[0:4]
    id_3_info = TypeInfo_list[2].goodsinfo_set.order_by('-id')[0:4]
    id_4_info = TypeInfo_list[3].goodsinfo_set.order_by('-id')[0:4]
    id_5_info = TypeInfo_list[4].goodsinfo_set.order_by('-id')[0:4]
    id_6_info = TypeInfo_list[5].goodsinfo_set.order_by('-id')[0:4]

    content = {'title': '首页', 'market_page': 1,
               'type1':id_1_info, 'type2':id_2_info,
               'type3':id_3_info, 'type4':id_4_info,
               'type5':id_5_info, 'type6':id_6_info,
               'type11': id_1_info[3], 'type21': id_2_info[3],
               'type31': id_3_info[3], 'type41': id_4_info[3],
               'type51': id_5_info[3], 'type61': id_6_info[3]
               }
    return render(request, 'df_goods/index.html', content)

def list(request, typeNum, pageNum, sortNum):
    goodtype = TypeInfo.objects.get(id=int(typeNum))
    news = goodtype.goodsinfo_set.order_by('-id')[0:2]
    if sortNum == '1':#按默认最新排序
        goods_lists = GoodsInfo.objects.filter(goods_type_id=int(typeNum)).order_by('-id')
    elif sortNum == '2':#按价格排序
        goods_lists = GoodsInfo.objects.filter(goods_type_id=int(typeNum)).order_by('-goods_price')
    elif sortNum == '3':   # 按人气
        goods_lists = GoodsInfo.objects.filter(goods_type_id=int(typeNum)).order_by('-goods_click')

    paginator = Paginator(goods_lists, 10)
    page = paginator.page(int(pageNum))
    content = {'title':'商品列表',
               'market_page':1,
               'page':page,
               'sortNum':sortNum,
               'paginator':paginator,
               'goodtype':goodtype,
               'news':news}
    return render(request, 'df_goods/list.html', content)

def detail(request, goods_id):
    goodinfo = GoodsInfo.objects.get(id=int(goods_id))
    goodinfo.goods_click += 1
    goodinfo.save()


    news = goodinfo.goods_type.goodsinfo_set.order_by('-id')[0:2]
    content = {
        'title':goodinfo.goods_type.type_title,
        'market_page': 1,
        'news':news,
        'goodinfo': goodinfo,
    }
    response = render(request, 'df_goods/detail.html', content)

    # 用户最近浏览
    goods_id_list = request.COOKIES.get('goods_ids', '')
    goods_id = str(goodinfo.id)
    if goods_id_list != '':
        id_list = goods_id_list.split(',')
        if id_list.count(goods_id) >= 1:
            id_list.remove(goods_id)
        id_list.insert(0,goods_id)
        if len(id_list) >= 6:
            id_list.pop(-1)
        goods_id_list = ','.join(id_list)
    else:
        goods_id_list = goods_id
    response.set_cookie('goods_ids',goods_id_list)
    return response
