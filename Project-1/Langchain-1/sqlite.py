import sqlite3 

##connect to sqlite
conn=sqlite3.connect("student.db")

# create a cursor obj to insert record , create table
cursor=conn.cursor()

##create table

table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT)
"""

#table will be created
cursor.execute(table_info)

#insert some record

cursor.execute('''
               
               Insert Into STUDENT values ('Tim','Data Science','B',80)
               
               ''')

cursor.execute('''
               
               Insert Into STUDENT values ('Mark','Data Science','A',90)
               
               ''')


cursor.execute('''
               
               Insert Into STUDENT values ('Ed','AI','C',70)
               
               ''')

cursor.execute('''
               
               Insert Into STUDENT values ('Alice','OS','B+',83)
               
               ''')

##Display all the records
print("The inserted records are")
data=cursor.execute('''
                    select * from Student
                    ''')


for row in data:
    print(row)
    
    
#Commit
conn.commit()
conn.close()