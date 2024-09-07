import sqlite3
#Connecting to sqlite

connection = sqlite3.connect("student.db")

#creating a cursor CRUD
cursor = connection.cursor()

# table_info = """
# Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
# SECTION VARCHAR(25), MARKS INT);

# """

# cursor.execute(table_info)


cursor.execute('''INSERT INTO STUDENT VALUES ('Rohit', 'FIRST', 'D',98)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Himanshu', 'FIRST', 'B',99)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Ranveer', 'SECOND', 'C',54)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Sheetal', 'FIRST', 'C',31)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Neha', 'SECOND', 'A',45)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Aman', 'THIRD', 'B',45)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Priya', 'FIRST', 'A',58)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Arjun', 'SECOND', 'B',57)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Riya', 'THIRD', 'C',54)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Kartik', 'FIRST', 'D',25)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Anjali', 'SECOND', 'C',21)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Mohan', 'THIRD', 'A',45)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Sahil', 'FIRST', 'B',45)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Pooja', 'SECOND', 'A',78)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Rahul', 'THIRD', 'D',95)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Sneha', 'FIRST', 'C',24)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Deepak', 'SECOND', 'B',54)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Simran', 'THIRD', 'C',45)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Vikram', 'FIRST', 'A',44)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Nikita', 'SECOND', 'D',0)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Rohini', 'THIRD', 'A',47)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Ajay', 'FIRST', 'C',78)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Shivam', 'SECOND', 'B',49)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Komal', 'FIRST', 'D',65)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Vikas', 'THIRD', 'B',63)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Sonia', 'SECOND', 'A',20)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Ishaan', 'FIRST', 'B',4)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Megha', 'THIRD', 'D',56)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Gaurav', 'SECOND', 'C',71)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Tina', 'FIRST', 'A',12)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Naman', 'SECOND', 'D',56)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Suman', 'THIRD', 'C',79)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Vivek', 'FIRST', 'B',23)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Alisha', 'SECOND', 'A',99)''')

  
# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM STUDENT''') 
for row in data: 
    print(row) 
  
# Commit your changes in the database     
connection.commit() 
  
# Closing the connection 
connection.close()

