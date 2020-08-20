from flask import Flask
# from book_shelf.book_shelf_service import book_shelf
from map_list.map_list_service import map_list
from data_list.data_list_service import data_list
from spatial_list.spatial_list_service import spatial_list
from spatial_list.spatial_mock_service import cim_service

# 主路由文件
app = Flask(__name__)
# 蓝图注册 需要把模块下声明的蓝图对象导入
app.register_blueprint(map_list, url_prefix="/map_list")
app.register_blueprint(data_list, url_prefix="/data_list")
app.register_blueprint(spatial_list, url_prefix="/spatial_list")
app.register_blueprint(cim_service, url_prefix="/cim_service")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
# -- coding:utf-8 --