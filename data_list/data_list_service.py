from data_list.data_list_dao import DataListDao
from flask import Blueprint,request
from flask_cors import CORS

#蓝图创建
data_list=Blueprint("data_list",__name__)
#设置跨域
CORS(data_list)

@data_list.route("/get_data_list",methods=["GET"])
def get_data_list():
    data=DataListDao().get_data_list()
    return data