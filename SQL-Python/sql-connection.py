"""
    Basic steps to connect sql database

    1. import sqlite3 module / library
    2. create a connection
    3. create a cursor
    4. execute query
    5. commit using connectName.commit()
    6. close connection 
"""


# import module
import sqlite3

# create a connection
connection = sqlite3.connect("employee.db" , isolation_level=None)

# create a cursor
cursor = connection.cursor()

# execute the query

# cursor.execute(
#     """
#     insert into emp('ename' , 'salary' , 'job')
#     values
#         ('scott' , 980 , 'clerk'),
#         ('Allen' , 1000 , 'Manager'),
#         ('scott' , 1500 , 'analyst');    
# """
# )

cursor.execute("select max(salary) from emp;")

max_sal = cursor.fetchone()[0]
print(round(max_sal))
# cursor.execute("delete from emp where ename = 'smith'")

# close the connection
connection.close()