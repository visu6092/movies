#import sqlite3 Database
import sqlite3

#create or connect with database
con=sqlite3.connect('movie_01.db')
print("Database created or connected....")

#Creating a Tbale
con.execute("create table Movies(id int primary key not null,name text,actor text,actress text,director text, yearOfrelease text)")
print("Table created....")

#inserting a record into Table 
con.execute('insert into Movies values(1,"Bachan_pandey","akshay_kumar","kirti_salon","Farhad_Samji","2022")')


con.execute('insert into Movies values(3,"shershah","Sidharth_Malhotra","kira_advani","Vishnuvardhan","2022")')

con.execute('insert into Movies values(4,"keshri","akshay_kumar","priti","Anurag Singh","2019")')

con.execute('insert into Movies values(5,"bharat","salman_khan","ketrina","Ali Abbas Zafar","2018")')


#fetch the record from Table
data=con.execute("select * from Movies")

for row in data:
    print("id:",row[0])
    print("Name:",row[1])
    print("Actor:",row[2])
    print("Actress:",row[3])
    print("Director:",row[4])
    print("Year Of Release:",row[5])

    print("-----------------------------")
    

#fetch actress and acor name with particular movie name
data1=con.execute("select actress,actor  from Movies where name='Shershaah'")

for row1 in data1:
    print(row1)
