from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel, root_validator, Field
from fastapi import Depends
app = FastAPI()


class User(BaseModel):
    # Q：Field 作用？
    username: str = Field(..., title='姓名', description='姓名字段需要长度大于6且小于等于12', max_length=12, min_length=6, example="Foo")
    age: int = Field(..., title='年龄', description='年龄需要大于18岁', ge=18, example=12)
    password_old: str = Field(..., title='旧密码', description='密码需要长度大于6', gl=6, example=6)
    password_new: str = Field(..., title='新密码', description='密码需要长度大于6', gl=6, example=6)
    # A：定义字段的额外信息和约束条件，... 表示不能省略

    # Q: @root_validator 这个注解的作用？
    @root_validator
    def check_passwords(cls, values):
        password_old, password_new = values.get('password_old'), values.get('password_new')
        # 新旧号码的确认匹配处理
        if password_old and password_new and password_old != password_new:
            raise ValueError('passwords do not match')
        return values
    # A：@root_validator 是 Pydantic 中的一个装饰器，用于在模型的所有字段验证之后执行额外的自定义验证逻辑。
    # 与字段级别的验证（如 @validator）不同，@root_validator 可以访问整个模型的数据（即所有字段的值），因此它适用于需要基于多个字段之间关系进行验证的场景。


# Q:=Depends() 的作用？
@app.get("/user")
def read_user(user: User=Depends()):
    return {
        'username': user.username,
        'password_old': user.password_old,
        'password_new': user.password_new,
    }
# A: 表示在调用 read_user 视图函数之前，会自动调用相应的函数来创建 User 对象。
# 通常用于输入验证、从请求中提取数据（例如，将 JSON 数据解析为 User 对象），或者从外部资源（例如数据库）获取数据。

class FileGet(BaseModel):
    username: str = Field(..., title='姓名', description='姓名字段需要长度大于6且小于等于12', max_length=12, min_length=6, example="Foo")
    file: UploadFile = File(...)

@app.post("/file_get")
async def file_get(user: FileGet=Depends()):
    return {
        'username': user.username,
        'filenme': user.file.filename
    }


if __name__ == "__main__":
    import uvicorn
    import os

    app_modeel_name = os.path.basename(__file__).replace(".py", "")
    print(app_modeel_name)
    uvicorn.run(f"{app_modeel_name}:app", host='127.0.0.1', reload=True)
