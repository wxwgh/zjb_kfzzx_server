from spatial_list.spatial_list_dao import SpatialListDao
from flask import Blueprint,request
from flask_cors import CORS

#蓝图创建
spatial_list=Blueprint("spatial_list",__name__)
#设置跨域
CORS(spatial_list)

@spatial_list.route("/get_spatial_list",methods=["GET"])
def get_map_list():
    datas=SpatialListDao().get_spatial_list()
    return datas