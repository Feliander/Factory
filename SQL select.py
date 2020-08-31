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
        'WHERE (year = (%s) OR year = (%s)) ' \
        'AND (month BETWEEN (%s) AND (%s))'
val1 = 2020
val2 = 2020
val3 = 1
val4 = 12

mycursor.execute(sql, (val1, val2, val3, val4))
myresult = mycursor.fetchall()
print(myresult)
