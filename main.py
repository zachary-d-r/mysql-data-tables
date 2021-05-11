import mysql.connector

text = open('pass.txt', 'r')
passwd = text.readline()
database = "students"
db = mysql.connector.connect(
    host='localhost',
    user="Zachary",
    password=passwd,
    database=database
    )
    
cursor = db.cursor()
cursor.execute(f"SELECT * FROM {database}")
students = cursor.fetchall()

cursor.execute(f"SHOW COLUMNS FROM {database}")
columns = cursor.fetchall()

spaces = 10
for i in range(len(columns)):
    print(f'{columns[i][0]}', end='')
    for space in range(spaces):
        print(' ', end='')
print("\n")


for i in range(len(students)):
    for j in range(len(students[i])):
        newSpaces = (len(str(columns[j][0]))-len(str(students[i][j]))) + spaces
        print(students[i][j], end='')
        for space in range(newSpaces):
            print(" ", end='')
    print("")

