from spatial_list.spatial_mock_dao import MockDao
from flask import Blueprint,request
from flask_cors import CORS

#蓝图创建
cim_service=Blueprint("cim_service",__name__)
#设置跨域
CORS(cim_service)

@cim_service.route("/api/v1/buffer/lvxian",methods=["POST"])
def get_city():
    datas=MockDao().get_city()
    return datas
@cim_service.route("/api/v1/buffer/xzjsyd",methods=["POST"])
def get_guangzhou():
    datas=MockDao().get_guangzhou()
    return datas