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
          'SUM(task), SUM(maket) FROM worktime ' \
          'WHERE (year = (%s))' \
          'AND (month = (%s))' \
          'AND (day = (%s))' \
          'AND (hours = (%s))' \
          'AND (minutes BETWEEN (%s) AND (%s))'
val1 = 2020
val2 = 9
val3 = 1
val4 = 15
val5 = 11
val6 = 23


mycursor.execute(sql, (val1, val2, val3, val4, val5, val6))
myresult = mycursor.fetchall()
print(myresult)
