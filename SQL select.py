import pymysql
import datetime

mydb = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='mydb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
mycursor = mydb.cursor()

sql = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
      'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
      'SUM(task), SUM(maket) FROM worktime WHERE year = \'2020\' AND month = 2'

mycursor.execute(sql)
myresult = mycursor.fetchall()

print(myresult)
