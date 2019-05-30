import redis

connect = redis.Redis(
    host='127.0.0.1',
    password='',
    port=6379,
    decode_responses=True,
    db=1
)
print(connect)
s = connect.get('cache_survival')
print(s is None)
print(type(s))
connect.set('cache_survival', 1)
# connect.expire('cache_survival', 0)
#
s = connect.get('cache_survival')
print(s)
print(type(s))
#
# x = connect.ttl('cache_survival')
# print(x)
# x = connect.ttl('cache_')
# print(x)

# for x in range(1, 100):
#     if x % 2 == 0:
#         connect.set('el_'+str(x), 123)
#     else:
#         connect.set('test_'+str(x), 123)
#
# key_list = connect.keys()
# if key_list:
#     for k in key_list:
#         if 'el' in k:
#             connect.expire(k, 100)  # 60 * 60 * 24
#         else:
#             connect.expire(k, 0)
#
# x = connect.ttl('el_2')
# print(x)
# y = connect.ttl('test_1')
# print(y)
# connect.set('el_', 123)
# connect.set('el_', 124)
# res = connect.get('el_')
# connect.expire('oyjx', 0)
# print(res)
