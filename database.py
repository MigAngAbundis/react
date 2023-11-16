import cx_Oracle
import pymysql

# Conexión a Oracle
oracle_conn = cx_Oracle.connect("system/12345@172.17.0.2:1522/XE")

# Conexión a MySQL
mysql_conn = pymysql.connect(host='host', user='root', password='23456', db='mysql.bastion')
