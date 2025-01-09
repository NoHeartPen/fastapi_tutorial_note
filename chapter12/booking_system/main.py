from app import creat_app
# 有趣，本来应该写在这里的代码移到 creat_app 里，然后 return 直接返回 app 本身
app =creat_app()
if __name__ == "__main__":
    import uvicorn
    import os
    app_model_name = os.path.basename(__file__).replace(".py", "")
    print(app_model_name)
    uvicorn.run(f"{app_model_name}:app", host='127.0.0.1', reload=True)


# Q： 下面这段在 Python 源码里看到代码的作用是？
# tree -I "node_modules|cache|test_*"
# tree -I "__pycache__"
# A：是一个在 Unix/Linux/macOS 系统中常见的命令行工具
# 用于显示当前目录及其子目录的树状结构
# -I 参数用来指定要忽略的目录或文件模式。