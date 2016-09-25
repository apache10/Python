

import MySQLdb
db = MySQLdb.connect("localhost","root","pavilion@1","TEST" )

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'lee', 20, 'F', 2291)"""
sql1 = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('jack', 'tee', 22, 'M', 9290)"""
sql2 = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('joe', 'sparow', 20, 'M', 2000)"""
try:
   cursor.execute(sql)
   cursor.execute(sql1)
   cursor.execute(sql2)
   db.commit()
except:
   db.rollback()

#read

sql = "SELECT * FROM EMPLOYEE  WHERE INCOME > '%d'" % (2100)
try:
   cursor.execute(sql)
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income )
except:
   print "Error: unable to fecth data"



#update

sql = "UPDATE EMPLOYEE SET AGE = AGE + 2 WHERE SEX = '%c'" % ('M')
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()


#delete
sql = "DELETE FROM EMPLOYEE WHERE SEX = '%c' AND AGE > '%d'" % ('M',22)
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()   

# disconnect from server
db.close()