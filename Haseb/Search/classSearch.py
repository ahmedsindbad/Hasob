from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

import sqlite3
import os


#database phyzical path ....
@python_2_unicode_compatible
class EXE:
    def exe(value):
        conn = sqlite3.connect('C://test//myenv//Haseb//db.sqlite3')
        c = conn.cursor()
        c.execute("select text from Search_verse where text like '%"+value+"%';", )
        result = c.fetchall()
        #print(unicode(result, "utf-8"))
        conn.commit()
        conn.close()
        return result

    def __str__(self):
        return self

    #def __init__(self, name):
        #self.name = name
