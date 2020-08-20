from postgis.postgis_dao import PostGisDao
import json

class SpatialListDao:

    # 获取空间分析服务列表
    def get_spatial_list(self):
        sql_str = "select * from spatial_analysis_services where is_delete = 0 order by order_code asc"
        datas = PostGisDao().select_all(sql_str)
        # json字符串转python对象
        for index in range(len(datas)):
            datas[index]["params"] = json.loads(datas[index]["params"])
            datas[index]["param_example"] = json.loads(datas[index]["param_example"])
        return json.dumps(datas)
