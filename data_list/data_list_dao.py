from postgis.postgis_dao import PostGisDao
import json
from urllib.request import unquote

class DataListDao:

    #获取数据列表
    def get_data_list(self):
        sql_str = "select * from data_services"
        datas = PostGisDao().select_all(sql_str)
        #json字符串转python对象
        for index in range(len(datas)):
            datas[index]["fields"]=json.loads(datas[index]["fields"])
        #python对象转json字符串
        return json.dumps(datas)
