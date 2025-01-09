#!/usr/bin/evn python
# coding=utf-8
from fastapi import FastAPI
import pathlib
from fastapi import Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# TODO 补充 melonpan 文档描述
app = FastAPI(title="学习Fastapi框架文档",
              description="以下是关于相Fastapi框架文档介绍和描述",
              version="0.0.1",debug=True)




# Q:解释这个地方的 pathlib.Path.cwd()
staticfiles = StaticFiles(directory=f"{pathlib.Path.cwd()}/static/")
# A: 用于获取当前工作目录的路径。cwd 代表 "current working directory"（当前工作目录）。
# TODO 补充实际的调用方法：<link href="{{url_for('static', path='/CSS/style.css')}}" rel="stylesheet">
# 由于三个地方的 static 完全一致
# 这意味着，当用户访问 http://<your-domain>/static 路径时，FastAPI 将自动从 staticfiles 指定的目录中提供静态文件。
# name="static" 是给这个挂载的静态文件资源起的名字，它可以用作 URL 反向生成或其他地方的引用。
app.mount("/static", staticfiles, name="static")


# 允许多个网址指向一个函数操作
@app.get('/', response_class=HTMLResponse)
@app.get('/index', response_class=HTMLResponse)
@app.post('/index', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html",
                                      {"request": request})


def myinex():
    return {"Hello": "myinex api"}

# 这种写法其实和下面是一样的，但建议还是下面的写法
app.get("/myindex", tags=["路由注册方式"], summary="路由注册方式说明")(myinex)

# 这种写法和上面等价
@app.get("/myindex", tags=["路由注册方式"], summary="路由注册方式说明")
def myindex():
    return {"Hello": "myinex api"}

# 返回纯文本的响应，有什么实际的应用场景么：
# 调用机器翻译 API /用于提供当前服务状态等不需要渲染的场景
@app.route('/loginjig', methods=['GET', 'POST'], name='loginjig')
def loginjig(req: Request):
    return PlainTextResponse('大爷')


if __name__ == '__main__':
    # Q：这个写法很有趣，是为了节省内存所以才在要调用的地方导入相关的包么？
    import uvicorn

    # A：不是。主要目的应该是为了控制代码的执行时机。如果这个文件作为主程序启动，只是作为包导入的话，就不会执行到这里
    # Q：解释下 main:app 的写法
    uvicorn.run(app='main:app', host="127.0.0.1", port=65535, reload=True, debug=True)
    # A：告诉 uvicorn 在 main.py 文件中寻找名为 app 的 FastAPI 实例并运行。
