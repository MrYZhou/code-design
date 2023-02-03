import os

from fastapi import APIRouter, Body
from fastapi.responses import FileResponse

from server.generate.dao import Config
from server.generate.index import codeParse
from util.base import Common

router = APIRouter(
    prefix="/generate",
    tags=["代码生成"],
    responses={404: {"description": "Not found"}},
)

# 通过缓存下载
@router.post("/download")
async def index(data: Config = Config()):
    # 解析模板
    if not data.cacheKey:
        data.cacheKey = Common.randomkey()
        configParse(data.cacheKey, data)

    # 压缩模板
    name = "模板" + data.cacheKey
    url = os.path.join(os.getcwd(), "static", name + ".zip")
    return FileResponse(url, filename=name + ".zip", status_code=200)

@router.post("/codeParse")
async def index(config: dict = Body(None)):
    # 获取表的字段信息
    # list = getTable(dyConnect(config), config.get('name'), config.get('table'))
    return codeParse([],config)


@router.get("/zipfile")
async def root():
    Common.zipfile("./template/java", "./template/java")
    url = "./template/java.zip"
    return FileResponse(url, filename="java.zip")
