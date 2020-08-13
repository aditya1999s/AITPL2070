import mysql.connector
con = mysql.connector.connect(host = '18.219.99.141', database = 'db1', user = 'root', password = 'India12345')
c = con.cursor()
def create_table():
    c.execute("create table aditya_product(pro_id varchar(20) primary key, pro_num int, pro_des varchar(20), price int)")

def insert_table():
    c.execute("insert into aditya_product values('001','500','chennai',5000)")
    c.execute("insert into aditya_product values('002','45','mumbai',11000)")
    c.execute("insert into aditya_product values('003','80','kolkata',620000)")
    c.execute("insert into aditya_product values('004','10','delhi',90000)")
    c.execute("insert into aditya_product values('005','5','Bangalore',9000000)")
    con.commit()

def delete_table():
    c.execute("delete from aditya_product where price=90000")
    con.commit()

def update_table():
    c.execute("update aditya_product set pro_num=8 where pro_des='Bangalore'")
    con.commit()

def select_table():
    c.execute("select * from aditya_product")
    data = c.fetchall()
    for row in data:
        print(row)

while True:
    print(" Enter your choice : \n Press 1. to create table \n Press 2. to insert into table \n Press 3. to delete into table \n "
          "Press 4. to update in table \n Press 5. to display content of the table \n Press 6. to exit.")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        create_table()
    elif ch == 2:
        insert_table()
    elif ch == 3:
        delete_table()
    elif ch == 4:
        update_table()
    elif ch == 5:
        select_table()
    elif ch == 6:
        exit(0)
    else :
        print("Invalid choice")

c.close()
con.close()