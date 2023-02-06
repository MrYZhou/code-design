<div align="center">
<strong>
<samp>

[English](README.md) · [简体中文](README.zh-Hans.md)
</samp>
</strong>
</div>

front

vue3 + vite + element plus

vue document

[ https://cn.vuejs.org/guide/introduction.html](https://cn.vuejs.org/guide/introduction.html)

vite document

[https://cn.vitejs.dev/guide](https://cn.vitejs.dev/guide/)

server

base on fastapi

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

resource (Save database configuration and other scripts)

router (Routing layer)
 
server (Service implementation logic)

static (Static resource access directory)

template (Code template)

util (Tools)

web (Front-end project)


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




