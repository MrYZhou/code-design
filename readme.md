前端

vue3 + vite 

vue document

[ https://cn.vuejs.org/guide/introduction.html](https://cn.vuejs.org/guide/introduction.html)

vite document

[https://cn.vitejs.dev/guide](https://cn.vitejs.dev/guide/)

后端

fastapi

fastapi document
[https://fastapi.tiangolo.com/zh/tutorial/first-steps/](https://fastapi.tiangolo.com/zh/tutorial/first-steps/)

orm document
[https://sqlmodel.tiangolo.com/tutorial/](https://sqlmodel.tiangolo.com/tutorial/)

jinja2 document
[http://docs.jinkan.org/docs/jinja2/index.html](http://docs.jinkan.org/docs/jinja2/index.html)

## step:

### quick use

```
docker run -d -p 8000:8000 -p 2666:5173 larryane/codedesign
```

### dir desc

resource 存数据库配置等脚本
router 路由层
server 服务实现逻辑
static 静态资源访问目录
template 代码模板
util 工具类
web 前端项目

### develop prepare

1: need build a venv folder

```bash
python -m venv .venv
```

2.start venv

```bash
.\.venv\Scripts\activate 
```

3.install pacakge

```bash
pip install -r requirements.txt
```

4.start app

```bash
uvicorn main:app --reload --port=8000
```

5.install  package

```
cd web && pnpm i
```

6.start vue

```
npm run dev
```



## build app

```bash
docker-compose up -d
```

if you want build a docker image,you can use dockerfile.
such as

```bash
docker build -t codeapi .
docker run -d -p 8000:8000 codeapi
```

### web

```bash
npm run build
```




