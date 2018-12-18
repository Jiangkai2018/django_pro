# 增删改查

#!/usr/bin/env python
# Version = 3.5.2
# __auth__ = '无名小妖'
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, select
engine = create_engine("mysql+pymysql://admin:kevin2018@10.165.2.115:3306/testdb", max_overflow=5)
metadata = MetaData()
user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(20)),
             )
color = Table('color', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(20)),
              )

conn = engine.connect()

# 创建SQL语句，INSERT INTO "user" (id, name) VALUES (:id, :name)
# conn.execute(user.insert(), {'id': 7, 'name': 'seven'})
# sql = user.insert().values(id=123, name='wu')
# conn.execute(sql)
# conn.close()

# sql = user.delete().where(user.columns.id > 10)

# sql = user.update().values(fullname=user.c.name)
sql = user.update().where(user.c.name == 'jack').values(name='ed')

# sql = select([user, ])
ret = conn.execute(sql)
print(ret)
sql = select([user.c.id, ])
# sql = select([user.c.name, color.c.name]).where(user.c.id==color.c.id)
# sql = select([user.c.name]).order_by(user.c.name)
# sql = select([user]).group_by(user.c.name)

result = conn.execute(sql)
print (result.fetchall())
conn.close()
