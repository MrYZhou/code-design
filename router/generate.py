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
