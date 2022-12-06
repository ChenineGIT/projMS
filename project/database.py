import mysql.connector as con
import json
def connect():
    mydb = con.connect(
        host="127.0.0.1",
        user="root",
        password="1234",
        database="timetable"
        )

    cur = mydb.cursor()
    return mydb, cur
'''============================================='''
# read file json
def write_file(list):
    path = "out/list.json"
    with open(path, "w") as file:
        file.write(list)



def all_profs():
    db, cur = connect()
    profs = {
        "prof" : {

        }
    }

    sql = "select * from prof"
    cur.execute(sql)
    all = cur.fetchall()
    for prof in all:
        inf = {f"{prof[0]}" : {"name": f"{prof[1]}"}}
        for p in profs:
            profs[p].update(inf)
    print(profs)
    write_file(json.dumps(profs))


all_profs()