#!/usr/bin/evn python
# -*- coding: utf-8 -*-
from typing import Dict, Optional

from pydantic import BaseModel, validator, ValidationError, PydanticValueError

class AddressError(PydanticValueError):
    code = '错误类型'
    msg_template = '当前地址长度不对，它应该需要{errmeg}，当前传入的值为：{value}'

class Person(BaseModel):
    username: str
    address: str

    # Q： pre = False 的意思是？
    @validator("address",pre=False)
    # 验证器会在字段的值经过所有其他处理后执行，通常用于需要确认最终的字段值是否符合某些条件。
    # Q：cls 的作用是？
    # A：cls 通常是用作类方法（class method）中的第一个参数，它代表当前类的引用，而不是实例对象的引用。
    # cls 和实例方法中的 self 类似，区别在于 cls 用于类方法，self 用于实例方法。
    def adress_rule(cls, address):
        # 如果地址长度小于6，那么则返回
        if len(address) < 6:
            raise AddressError(errmeg='小于6',value=address)
        elif len(address) > 12:
            raise AddressError(errmeg='大于12',value=address)
        return address

if __name__ == '__main__':
    # try:
    #     user = Person(username='xiaozhong', address='12345')
    # except ValidationError as e:
    #     print(e.errors())
    # else:
    #     print(user.username, user.address)


    class Person(BaseModel):
        name: str
        nums: str
        age: Optional[int]


    if __name__ == '__main__':
        try:
            user = Person(name='xiaozhong')
        except ValidationError as e:
            # print(e.errors())
            # print(e.json())
            print(str(e))
        else:
            print(user.name, user.age)