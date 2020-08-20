import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='mydb'
)


mycursor = mydb.cursor()
# sql = 'DROP TABLE worktime'
# sql = 'CREATE TABLE worktime (' \
#       'id INT(255) AUTO_INCREMENT PRIMARY KEY,' \
#       'name VARCHAR(20),' \
#       'action VARCHAR (20),' \
#       'totaltime INT(10),' \
#       'plantime INT (10),' \
#       'setup INT (10),' \
#       'autoserv INT (10),' \
#       'ppr INT (10),' \
#       'break INT (10),' \
#       'material INT (10),' \
#       'task INT (10),' \
#       'maket INT (10),' \
#       'secs INT(10),' \
#       'minutes INT(10),' \
#       'hours INT(10),' \
#       'day INT(10),' \
#       'month INT(10),' \
#       'year INT(10)' \
#       ')'
sql = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
                            'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
                            'SUM(task), SUM(maket) FROM worktime WHERE (year = \'2019\') and (year = \'2020\')'
# sql = 'DELETE FROM worktime WHERE id = 46'
sql = 'INSERT INTO worktime (name, action, totaltime, plantime, setup, autoserv, ppr, break, material,' \
                   'task, maket, secs, minutes, hours, day, month, year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,' \
                   ' %s, %s, %s, %s, %s, %s, %s, %s)'
val1 = 'all'
val2 = 'manual'
val3 = 273600
val4 = 0
val5 = 0
val6 = 0
val7 = 0
val8 = 0
val9 = 0
val10 = 0
val11 = 0
val12 = datetime.datetime.strftime(datetime.datetime.now(), "%S")
val13 = datetime.datetime.strftime(datetime.datetime.now(), "%M")
val14 = datetime.datetime.strftime(datetime.datetime.now(), "%H")
val15 = datetime.datetime.strftime(datetime.datetime.now(), "%d")
val16 = datetime.datetime.strftime(datetime.datetime.now(), "%m")
val17 = datetime.datetime.strftime(datetime.datetime.now(), "%Y")
val17 = 2019
mycursor.execute(sql, (val1, val2, val3, val4, val5, val6,
                                         val7, val8, val9, val10, val11, val12,
                                         val13, val14, val15, val16, val17))
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# mycursor.execute(sql, (val1, val2, val3))
# mydb.commit()
for x in myresult:
    print(x)
# print(mycursor.rowcount, "record(s) deleted")