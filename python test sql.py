import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("create table if not exists tbl_persons(\
        ID integer primary key autoincrement, \
        col_fname text, \
        col_lname text, \
        col_email text \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("insert into tbl_persons(col_fname, col_lname, col_email) values (?,?,?)", \
                ('sarah','jones','sjones@gmail.com'))
    cur.execute("insert into tbl_persons(col_fname, col_lname, col_email) values (?,?,?)", \
                ('sally','may','smay@gmail.com'))
    cur.execute("insert into tbl_persons(col_fname, col_lname, col_email) values (?,?,?)", \
                ('kevin','bacon','kbacon@gmail.com'))
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("select col_fname,col_lname,col_email from tbl_persons where col_fname = 'sarah'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "first name: {}\nlast name: {}\nemail: {}".format(item[0],item[1],item[2])
    print(msg)
