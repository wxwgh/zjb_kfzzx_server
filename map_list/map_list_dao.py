from postgis.postgis_dao import PostGisDao
import json


class MapListDao:

    # 获取地图列表 树形结构
    def get_map_tree(self):
        result = {}
        result["name"] = "地图服务列表"
        result["child"] = []
        sql_str = "select * from map_services"
        datas = PostGisDao().select_all(sql_str)
        for data in datas:
            first = {}
            second = {}
            three = {}
            first["id"] = data["id"]
            first["name"] = data["root_node"]
            first["child"] = []
            if data["layer_tree_height"] == 2:
                second["name"] = data["tail_node"]
                second["urls"] = [
                    {
                        "type": "rest",
                        "url": data["rest"]
                    },
                    {
                        "type": "wmts_china",
                        "url": data["wmts_china"]
                    },
                    {
                        "type": "wmts100",
                        "url": data["wmts100"]
                    }
                ]
                second["params"] = json.loads(data["params"])
                # print(second)
            else:
                second["name"] = data["mid_node"]
                second["child"] = []
                three["name"] = data["tail_node"]
                three["urls"] = [
                    {
                        "type": "rest",
                        "url": data["rest"]
                    },
                    {
                        "type": "wmts_china",
                        "url": data["wmts_china"]
                    },
                    {
                        "type": "wmts100",
                        "url": data["wmts100"]
                    }
                ]
                three["params"] = json.loads(data["params"])
                second["child"].append(three)
            first["child"].append(second)
            result["child"].append(first)
        return result

    #获取地图列表
    def get_map_list(self):
        sql_str = "select * from map_services where is_delete = 0 order by order_code asc"
        datas = PostGisDao().select_all(sql_str)
        # json字符串转python对象
        for index in range(len(datas)):
            datas[index]["params"] = json.loads(datas[index]["params"])
        return json.dumps(datas)
