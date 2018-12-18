#!/usr/bin/env python
# Version = 3.5.2
# __auth__ = '无名小妖'
# 创建表
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
metadata = MetaData()  # 类
user = Table('user',  # 表名
             metadata,  # 绑定
             Column('id', Integer, primary_key=True),  # 列名
             Column('name', String(20)),  # 列名
             )
color = Table('color', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(20)),
              )
engine = create_engine("mysql+pymysql://admin:kevin2018@10.165.2.115:3306/testdb", max_overflow=5)
metadata.create_all(engine)  # 创建上面定义的表
engine.execute(
    "INSERT INTO color VALUES (%(id)s, %(name)s)",
    id=999, name="alex"
)
result = engine.execute('select * from color')
ret = result.fetchall()
print(ret)