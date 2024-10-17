import mysql.connector

db = mysql.connector.connect(
    host=input("Host Name: "),
    user=input("Username: "),
    password=input("Password: "),
    database=input("Database Name:")
)

cs=db.cursor()

#cs.execute("alter table student add column email varchar(50)")

cs.execute("select * from student")
students = cs.fetchall()

for row in students:
    roll_no = row[0]

    cs.execute(""" update student
    set email = concat(fname, ".", lname, "@ambertag.com")
    where roll_no = %s """, (roll_no,))
    print(row)
    print("#---------------------#")
    db.commit()

