import psycopg2

class PostGisDao:

    #构造函数
    def __init__(self):
        #打开数据连接
        self.conn= psycopg2.connect(
            database="postgis",
            user="postgis",
            password="0",
            host="172.17.0.2",
            port="5432"
        )
        #获取操作游标
        self.cursor = self.conn.cursor()

    #全部查询操作
    def select_all(self,sql_str):
        #执行查询
        self.cursor.execute(sql_str)
        #获取结果
        result = self.cursor.fetchall()
        #获取字段
        fields = self.cursor.description
        datas=[]
        for i in range(len(result)):
            data={}
            for s in range(len(fields)):
                data[fields[s][0]]=result[i][s]

            datas.append(data)

        self.conn.close()
        return datas