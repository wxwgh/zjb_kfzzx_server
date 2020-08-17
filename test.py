from map_list.map_list_dao import MapListDao
from data_list.data_list_dao import DataListDao
import unittest
#继承写法
class Test(unittest.TestCase):

    def test(self):
        data=DataListDao().get_data_list()
        print(data)
unittest.main()