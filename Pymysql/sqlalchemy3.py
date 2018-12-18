#!/usr/bin/env python
# Version = 3.5.2
# author = '无名小妖'
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from  sqlalchemy.orm import sessionmaker

Base = declarative_base()  # 生成一个SqlORM 基类
engine = create_engine("mysql+pymysql://admin:kevin2018@10.165.2.115:3306/testdb", max_overflow=5)
class Host(Base):
    __tablename__ = 'hosts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
    ip_addr = Column(String(128), unique=True, nullable=False)
    port = Column(Integer, default=22)


Base.metadata.create_all(engine)  # 创建所有表结构

if __name__ == '__main__':
    SessionCls = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    session = SessionCls()
    # h1 = Host(hostname='localhost',ip_addr='127.0.0.1')
    # h2 = Host(hostname='ubuntu',ip_addr='192.168.2.243',port=20000)
    # h3 = Host(hostname='ubuntu2',ip_addr='192.168.2.244',port=20000)
    # session.add(h3)  #可以一个一个添加
    # session.add_all( [h1,h2])  # 也可以全部添加
    # h2.hostname = 'ubuntu_test' #只要没提交,此时修改也没问题
    # 想要修改需得先查询
    res = session.query(Host).filter(Host.hostname.in_(['ubuntu2', 'localhost'])).all()  # all查出所有
    print(res)
    obj = session.query(Host).filter(Host.hostname=='localhost').first()  # first查出第一条
    print(obj)
    # obj.hostname = 'test data'
    # 删除数据
    session.delete(obj)
    session.rollback()  # 回滚
    session.commit()  # 提交