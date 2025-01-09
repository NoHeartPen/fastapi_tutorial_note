# 创建引擎对象
from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine,update,delete
engine = create_engine("sqlite:///user.db")
from sqlmodel import Field, SQLModel

class Users(SQLModel, table=True):
    # Q： 主键为什么要被设为 Optional 呢？
    id: Optional[int] = Field(default=None, primary_key=True)
    # A： 创建用户的时候不需要提供这个地方的数据，所以设为了可选
    name:str
    nikename:str
    password :str
    email:str

"""
# Q：下面的是 SQlAlachemy 的写法，和上面的相比，最明显的就是这个少了 autoincrement=True 和 Column(String(32))
class User(Base):
    # 指定本类映射到users表
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    nikename = Column(String(32))
    password = Column(String(32))
    email = Column(String(50))
# A：SQLModel默认会把主键设成 autoincrement=True

# 如果需要指明 Column(String(32)) 这样类似的存储限制，可以用下面的写法
class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(..., max_length=20)  # 限制 name 字段最大长度为 20
    nikename: str = Field(..., max_length=32)
    password: str = Field(..., max_length=32)
    email: str = Field(..., max_length=50)
"""

from sqlmodel import Session,select
with Session(engine) as session:

    allusers = select(Users)
    results = session.exec(allusers)
    for user in results:
        print(user)
    print('>'*5)
    userresult = select(Users).where(Users.name == "xiaozhong1")
    user = session.exec(userresult).first()
    print(user)
    print('>' * 5)
    userresult = select(Users).where(Users.name == "xiaozhong1").where(Users.nikename == "zyx")
    users = session.exec(userresult).all()
    print(users)
    print('>' * 5)
    userresult = select(Users).where(Users.name == "xiaozhong1",Users.nikename == "zyx")
    users = session.exec(userresult).all()
    print(users)

with Session(engine) as session:
    results = session.exec(select(Users).where(Users.name == "xiaozhong1"))
    user = results.first()
    print("user:", user)
    user.email = 'zyx1232@qq.com'
    session.add(user)
    session.commit()
    session.refresh(user)

with Session(engine) as session:
    updateusers = update(Users).where(Users.name == "xiaozhong1")
    results = session.exec(updateusers.values(email='xiaozhong@qw.com'))
    session.commit()

with Session(engine) as session:
    user = session.exec(select(Users).where(Users.name == "xiaozhong1")).first()
    session.delete(user)
    session.commit()

with Session(engine) as session:
    user = session.exec(delete(Users).where(Users.name == "xiaozhong1"))
    session.commit()