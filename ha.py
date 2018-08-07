import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="Achyuth")

cursor = db.cursor()

a = "Achyuth@gmail.com"
p = "achyuth"
query =  'insert into smac(id,number) values(14,40)'
#args = (a,p)
#cursor.execute("""insert into acchu values(14,%s,%s)""",('Achyuth','achyuth'))
#cursor.execute("select * from acchu")
#cursor.execute("""insert into acchu(id,name,password) values(007,'Achyuth','achyuth')""")
cursor.execute('insert into acchu values(100,"%s","%s")' % (a,p))
db.commit()
data = cursor.fetchone()

print (data)

db.close()
                     
