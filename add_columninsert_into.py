import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9923",
    database="college"
)

cs=db.cursor()

#cs.execute("""
#alter table student
#add column email varchar(50)
#""")

cs.execute("""
update student
set email = concat(fname, ".", lname, "@ambertag.com")
""")

db.commit()

cs.execute("select * from student")
students_mail = cs.fetchall()

print("Student record with_email")

for student in students_mail:
    print(student)

cs.close()
db.close()

