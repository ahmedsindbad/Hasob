import sqlite3
import os


#database phyzical path ....


def exe(want):
    conn = sqlite3.connect('C://test//myenv//Haseb//db.sqlite3')
    c = conn.cursor()
    c.execute("select text from Search_verse where text like '%"+want+"%';", )
    result = str(c.fetchall()).encode(encoding='utf-8')
    #print(unicode(result, "utf-8"))
    conn.commit()
    conn.close()
    return result



