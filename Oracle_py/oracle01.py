# myscript.py
# -*- coding=utf-8 -*-
from __future__ import print_function
import cx_Oracle
# Connect as user "hr" with password "welcome" to the "oraclepdb" service running on this computer.
# connection = cx_Oracle.connect("hr", "welcome", "localhost/orclpdb")
connection = cx_Oracle.connect("smxepoint", "123456", "10.165.2.99:1521/SMXEPOINT")
cursor = connection.cursor().execute("""SELECT OUNAME,OUGUID FROM "FRAME_OU""")
