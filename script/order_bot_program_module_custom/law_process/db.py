import sqlite3

# data is a list whose base element contains 6 elements number,of,name,isNTWC,issin,content
# row data contains all information about the article
# this function have two mode, one is add one or more raw data, another is modify the existing row data


def save_to_db(dbpath, ismodify, data):
    con = sqlite3.connect(dbpath)
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS criminal(number,of,name,isNTWC,issin,content)")
    if ismodify == 0:
        cur.executemany("INSERT INTO criminal VALUES(?,?,?,?,?,?)", data)
    if ismodify == 1:
        cur.execute(
            "DELETE FROM criminal WHERE number=? and of=?", data[0], data[1])
        cur.execute("INSERT INTO criminal VALUES(?,?,?,?,?,?)", data)
    con.commit()
    con.close()


def get_all_from_db(dbpath):
    con = sqlite3.connect(dbpath)
    cur = con.cursor()
    res = cur.execute(
        "SELECT number,of,name,isNTWC,issin,content FROM criminal")
    result = res.fetchall()
    con.close()
    return result

# mode 1: search by number


def search_by_number(dbpath, data, mode):
    con = sqlite3.connect(dbpath)
    cur = con.cursor()
    if mode == 1:
        res = cur.execute(
            "SELECT number,of,name,isNTWC,issin,content FROM criminal WHERE number=? and of=?", data)
    result = res.fetchall()
    con.close()
    return result

# mode 2: search by str


def search_by_str(dbpath, data, mode):
    con = sqlite3.connect(dbpath)
    cur = con.cursor()
    if mode == 1:
        res = cur.execute(
            "SELECT number,of,name,isNTWC,issin,content FROM criminal WHERE name like ?", data)
    result = res.fetchall()
    con.close()
    return result
