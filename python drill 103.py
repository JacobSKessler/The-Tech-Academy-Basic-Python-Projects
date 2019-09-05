import sqlite3

conn = sqlite3.connect('drill_103.db')
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#msg = ""
#exists for runtime test

with conn:
    cur = conn.cursor()
    cur.execute("create table if not exists tbl_files(\
        ID integer primary key autoincrement, \
        col_fname \
        )")
    conn.commit()
conn.close()

def chkTxt(file):
    #checks if a given file name ends in .txt
    if file.endswith('.txt') == True:
        return True
    else:
        return False

conn = sqlite3.connect('drill_103.db')

for i in fileList:
    #adds .txt files one at a time
    cur = conn.cursor()
    if chkTxt(i) == True:
        cur.execute("insert into tbl_files(col_fname) values (?)", \
                    (i,))
        conn.commit()
conn.close()

conn = sqlite3.connect('drill_103.db')
with conn:
    cur = conn.cursor()
    cur.execute("select col_fname from tbl_files")
    varFile = cur.fetchall()
    for item in varFile:
        msg = "file name: {}".format(item[0])
        print(msg)
conn.close()




