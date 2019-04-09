from collections import namedtuple


# 字典对象装具名元祖
def dict_to_namedtuple(*, obj: dict):
    NamedTuple = namedtuple('NamedTuple', obj.keys())
    return NamedTuple(**obj)


dct = {
    "RoomTypeID": 763417,
    "StandardBedType": "1 Double or 2 Twin beds (大床或双床)",
    "BedTypeID": 9,
    "RoomTypeName": "Adjoining Semi Double Room, Smoking",
    "RoomTypeNameCN": "客房, 吸烟房 (Adjoining Semi Double Room )",
    "BedTypeDescCN": "<p>2 张单人床",
    "BedTypeDesc": "<p>2 Twin Beds",
    "SRoomID": 139461,
    "SupplierID": 6,
    "SourceRoomID": "",
    "UserName": None,
    "UserRemark": None,
    "Status": 14
}
print(dict_to_namedtuple(obj=dct))

