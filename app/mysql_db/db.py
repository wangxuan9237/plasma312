# -*-coding:utf-8 -*-
 
import MySQLdb   
import ConfigParser
import pdb 
cf=ConfigParser.ConfigParser()
cf.read("/root/microblog/app/mysql_db/conf.ini")
 
DATABASE=cf.get("app_info","DATABASE")
#pdb.set_trace()
USER=cf.get("app_info","USER")
PASSWORD=cf.get("app_info","PASSWORD")
HOST=cf.get("app_info","HOST")
PORT=int(cf.get("app_info","PORT"))
CHARSET=cf.get("app_info","CHARSET")
def mysql(sql):
        conn=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,db=DATABASE,port=PORT,charset=CHARSET)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.commit()  
        conn.close()
        return rows

#print mysql('SELECT * FROM user')
