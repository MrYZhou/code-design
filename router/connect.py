from typing import List

from fastapi import APIRouter
from nanoid import generate
from fastapi import Body
from server.connect.dao import DataBase, Table, dyConnect, getAllTable, getTable, savedb

router = APIRouter(
    prefix="/connect",
    tags=["代码生成"],
    responses={404: {"description": "Not found"}},
)



# 保存连接的数据库信息
@router.post("/database", status_code=200)
async def index(dataBase: DataBase):
    dataBase.id = generate()
    savedb(dataBase)
    return dataBase



# 读取所有表信息,动态连接数据库
@router.post("/tableList")
async def index(dataBase: DataBase):
    engine = dyConnect(dataBase)
    list: List[Table] = getAllTable(engine, dataBase.name)
    map = {}
    for item in list:
        key = item.dbName
        if not key in map:
            map[key]: List = []
        map[key].append(item)
    return map

# 读取单表信息
@router.post("/tableInfo")
async def index(dataBase:dict=Body(None)):
    return getTable(dyConnect(dataBase), dataBase.get('name'), dataBase.get('table'))







