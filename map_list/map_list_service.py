from map_list.map_list_dao import MapListDao
from flask import Blueprint,request
from flask_cors import CORS

#蓝图创建
map_list=Blueprint("map_list",__name__)
#设置跨域
CORS(map_list)

@map_list.route("/get_map_list",methods=["GET"])
def get_map_list():
    datas=MapListDao().get_map_list()
    return datas