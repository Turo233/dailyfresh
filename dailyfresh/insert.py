# -*- coding:utf-8 -*-
import os 
import json

def readJsonFile(path):
    with open(path, "rb") as f:
        data = json.load(f)

    return data

a = readJsonFile("./lessflash.json")
data = a["products"]
list_mysql = []
type_id = 1
for v, k in data.items():
    # if k == "104749":
    #     continue
    for item in k:    
        str = "insert into df_goods_goodsinfo(goods_title,goods_pic,goods_price,goods_unit,goods_click,goods_intru,goods_stock,goods_detail,goods_type_id, isDelete) values("
        str += "\"" + item["name"] + "\","
        str += "\"" + item["img"] + "\","
        str += '%.2f,'%float(item["price"]) # price
        str += "\"" + item["specifics"] + "\","
        str += '%d,'%0 # click
        str += "\"" + item["long_name"] + "\","
        str += '%d,'%float(item["store_nums"]) # stock
        str += "\"" + item["long_name"] + "\","
        str += '%d,'%type_id
        str += '%d'%0
        str += ");"
        list_mysql.append(str)
    type_id += 1  
with open("./less_info.txt", 'a') as f:
	for each in list_mysql:
		f.write(each+"\n")

        



