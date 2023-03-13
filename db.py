import mysql.connector
import json

db=mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='tech2go',
)

""" retrieve data from the database """
def get_all(table:str,fields:list)->list:
    flds:str="`,`".join(fields)
    sql:str=f"SELECT `{flds}` FROM `{table}`"
    conn=db.cursor(dictionary=True)
    conn.execute(sql)
    slist:list=conn.fetchall()
    return slist

"""add data into the database"""
def add_user(table:str,fields:list=[],data:list=[])->bool:
    #INSERT INTO `table`(`fld1`,`fld2`,`fld3`,...) VALUES(%s,%s,%s,...)
    qmark:list=[]
    okey:bool=False
    if len(fields)==len(data):
        [qmark.append("%s") for item in data] #populate the qmark list
        flds:str="`,`".join(fields)
        dta:str=",".join(qmark)
        sql:str=f"INSERT INTO `{table}`(`{flds}`) VALUES({dta})"
        conn=db.cursor()
        conn.execute(sql,data)
        db.commit()
        conn.close()
        okey=True
    return okey

def validate_user(table:str,username:str,password:str)->bool:
    sql:str=f"SELECT * FROM `{table}` WHERE `username`='{username}' and `password`='{password}'"
    conn=db.cursor(dictionary=True)
    conn.execute(sql)
    slist:list=conn.fetchall()
    return len(slist)>0

def read_userName(table:str,username,password:str)->str:
    sql:str=f"SELECT lastname, firstname FROM `{table}` WHERE `username`='{username}' and `password`='{password}'"
    conn=db.cursor(dictionary=True)
    conn.execute(sql)
    slist:list=conn.fetchall()
    res = ", ".join([ x['lastname'] for x in slist ] + [ x['firstname'] for x in slist ])
    return res

def main()->None:
    print("sikret")
    #print(json.dumps(find_item("student",2),indent=4))

if __name__=="__main__":
    main()