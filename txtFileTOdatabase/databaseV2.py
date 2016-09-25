import MySQLdb
db = MySQLdb.connect("localhost","root","pavilion@1","TEST" )

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS MOBILE")

sql = """CREATE TABLE MOBILE(
         MOBILE_NAME  CHAR(20) NOT NULL,
         MODEL_NAME  CHAR(20),
         RAM_SIZE CHAR(10),  
         INTERNAL_SPACE CHAR(10),
         CAMERA CHAR(10) )"""
cursor.execute(sql)
db.commit()
#insert from txt file


mobile = open("mobile.txt", "r")
lines = mobile.readlines()

for line in lines:
	print line
	data = line.split()
	name = data[0]
	model = data[1]
	ram= data[2]
	internal = data[3]
	camera = data[4]
	insrt= "INSERT INTO MOBILE (MOBILE_NAME, MODEL_NAME, RAM_SIZE, INTERNAL_SPACE, CAMERA) VALUES('%s', '%s', '%s', '%s', '%s')"%(name,model,ram,internal,camera)
	cursor.execute(insrt)
try:
	db.commit()
except:
	db.rollback()


db.close()