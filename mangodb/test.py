"""
    启动mongodb
    mongod --config /usr/local/etc/mongod.conf
"""
import time

from pymongo import MongoClient

conn = MongoClient(host='127.0.0.1', port=27017)
test_db = conn['test']
test_table = test_db['test_table']
# test_table = test_db['test_table_city']


# res = test_table.find_one({"_id": "123"})
# print(res)
# if res:
#     print("---")
# else:
# data = {
#     "_id": "123"
# }
# test_table.save(data)
# # 增， 改
data = {
    "_id": "02_2019-02-29",
    "date_string": '2019-01-29',
    "spl_id": '01',
    "roomtype_count": '1022',
    "roomtype_has_mapping_count": '500',
    "update": time.strftime('%Y-%m-%d', time.localtime(time.time()))
}

test_table.save(data)

res_data = test_table.find_one("02_2019-02-29")
print(res_data)
#
# # 差
# aa = test_table.find_one({"_id": '02_2019-01-29'})
# print(type(aa))
