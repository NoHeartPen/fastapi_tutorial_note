#!/usr/bin/evn python
# coding=utf-8
# + + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + +
#        ┏┓　　　┏┓+ +
# 　　　┏┛┻━━━┛┻┓ + +
# 　　　┃　　　　　　 ┃ 　
# 　　　┃　　　━　　　┃ ++ + + +
# 　　 ████━████ ┃+
# 　　　┃　　　　　　 ┃ +
# 　　　┃　　　┻　　　┃
# 　　　┃　　　　　　 ┃ + +
# 　　　┗━┓　　　┏━┛
# 　　　　　┃　　　┃　　　　　　　　　　　
# 　　　　　┃　　　┃ + + + +
# 　　　　　┃　　　┃　　　　Codes are far away from bugs with the animal protecting　　　
# 　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
# 　　　　　┃　　　┃
# 　　　　　┃　　　┃　　+　　　　　　　　　
# 　　　　　┃　 　　┗━━━┓ + +
# 　　　　　┃ 　　　　　　　┣┓
# 　　　　　┃ 　　　　　　　┏┛
# 　　　　　┗┓┓┏━┳┓┏┛ + + + +
# 　　　　　　┃┫┫　┃┫┫
# 　　　　　　┗┻┛　┗┻┛+ + + +
# + + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + +"""
"""
Author = zyx
@Create_Time: 2022/4/3 20:18
@version: v1.0.0
@Contact: 308711822@qq.com
@File: confiig.py
@文件功能描述:------
"""

from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # 定义连接数据库的URL地址
    # 注意这个地方只是返回了数据库的配置，所以地址还是相对 main 来说的
    # 允许异步操作数据库
    ASYNC_DATABASE_URI: str = "sqlite+aiosqlite:///user.db"

# Q：解释这个地方的　@lru_cache() 的实际应用场景
@lru_cache()
def get_settings():
    return Settings()
# A： 应用场景：
# 1. 返回值是不可变的（如 Settings() 对象）且调用频繁的函数。
# 2. 显著减少相同计算的重复次数，优化性能，尤其是当对象创建代价较高时。
