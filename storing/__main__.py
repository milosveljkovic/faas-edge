from array import array
from pydantic import BaseModel
from datetime import datetime
import psycopg2

#{'time': '1970-0-0 0:0:02', 'use': -1.0, 'gen': -1.0, 'dw': -1.0, 'fu': -1.0, 'fu2': -1.0, 'ho': -1.0, 'fridge': -1.0, 'wc': -1.0}
# {"dw":6.0,"fridge":0.0,"fu":2.0,"fu2":4.0,"gen":5.0,"ho":4.0,"time":"1970-01-01 00:00:02","use":4.0,"wc":0.0}

def connectToDb():
    print("Connecting to db")
    conn=psycopg2.connect("host=pg-minikube-postgresql.default port=5432 dbname=postgres user=postgres password=postgres")
    cur=conn.cursor()
    return cur, conn

def disconnect(cur):
    print("Disconnect from db")
    cur.close()


def main(dict):
    try:
        cur,conn = connectToDb()
        cur.execute('INSERT INTO iot.smart_home(time, use, gen, dw, fu, fu2, ho, fridge, wc) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',(dict['time'],dict['use'],dict['gen'],dict['dw'],dict['fu'],dict['fu2'],dict['ho'],dict['fridge'],dict['wc']))
        conn.commit()
    except:
        print("Something went wrong")
        return {"msg":"Something went wrong"}
    # finally:
    #     return {"msg":"Finally"}
    #     disconnect(cur)
    return {"msg":"Successfully stored iot data"}