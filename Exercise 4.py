import sqlite3
con = sqlite3.connect('db.db4')
c = con.cursor()

def create():
    c.execute('create table emp (ssn text primary key,name text, salary int)')
    c.execute("insert into emp values ('001','Aditya',10000)")
    c.execute("insert into emp values ('002','Aliyas',29000)")
    c.execute("insert into emp values ('003','Ankit',121312)")
    c.execute("insert into emp values ('004','Ayush',67777)")
    con.commit()
def select():
    c.execute('select * from emp')
    data = c.fetchall()
    for row in data:
         print(row)
    # print(data[0])
    # print(data[1])
    c.close()
    con.close()

    # data1 = c.fetchall()
    # print(data1)
    # c.close()
    # con.close()
while True:
    print("Press 1. to create database\nPress 2. to print the data\nPress 3. for exit")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        create()
    elif ch == 2:
        select()
    elif ch == 3:
        exit(1)
    else:
        print("Invalid choice ")