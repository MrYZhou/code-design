from glob import iglob
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from util.system import Init

app = FastAPI()

Init.do(app)


@app.get("/")
async def index():
    return FileResponse("static/web/index.html")


if __name__ == '__main__':
    #新增下面一行代码即可打包多进程
    # multiprocessing.freeze_support()
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True, workers=1)
