#!/usr/bin/evn python
# -*- coding: utf-8 -*-
from fastapi import Request
from fastapi import FastAPI, Query, HTTPException
from starlette.responses import JSONResponse

app = FastAPI()


from enum import Enum
class ExceptionEnum(Enum):
    # TODO 枚举的元组？
    SUCCESS = ("0000", "OK")
    FAILED = ("9999", "系统异常")
    USER_NO_DATA = ("10001", "用户不存在")
    USER_REGIESTER_ERROR = ("10002", "注册异常")
    PERMISSIONS_ERROR = ("2000", "用户权限错误")

class BusinessError(Exception):
    # Q： 魔术方法的意思是？
    __slots__ = ['err_code', 'err_code_des']
    # A： 表示 BusinessError 只有这2个属性
    def __init__(self,  result: ExceptionEnum = None, err_code: str = "00000", err_code_des: str = ""):
        # 注意 result 的默认值是 None，为什么要这么设定呢
        if result:
            # 如果不是 None
            self.err_code = result.value[0]
            self.err_code_des = err_code_des or result.value[1]
        else:
            self.err_code = err_code
            self.err_code_des = err_code_des
        super().__init__(self)

# Q：这个的调用位置？难道是默认触发的么
@app.exception_handler(BusinessError)
async def custom_exception_handler(request: Request, exc: BusinessError):
    return JSONResponse(content={
        'return_code':'FAIL',
        'return_msg':'参数错误',
        'err_code': exc.err_code,
        'err_code_des': exc.err_code_des,
    })
# A： 当 BusinessError 异常被抛出时，FastAPI 框架会自动触发这个的异常处理器，所以这个文件里面找不到显式调用的声明。

@app.get("/custom_exception")
async def custom_exception(name: str = 'zhong'):
    if name == "xiaozhong":
        raise BusinessError(ExceptionEnum.USER_NO_DATA)
    return {"name": name}


if __name__ == "__main__":
    import uvicorn
    import os

    app_modeel_name = os.path.basename(__file__).replace(".py", "")
    print(app_modeel_name)
    uvicorn.run(f"{app_modeel_name}:app", host='127.0.0.1', reload=True)
