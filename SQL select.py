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
        'WHERE year BETWEEN (%s) AND (%s) ' \
        'AND month BETWEEN (%s) AND (%s) ' \
        'AND day BETWEEN (%s) AND (%s)' \
        'AND hours BETWEEN (%s) AND (%s)' \
        'AND minutes BETWEEN (%s) AND (%s)'
val1 = '2020'
val2 = '2020'
val3 = '01'
val4 = '12'
val5 = '23'
val6 = '23'
val7 = '00'
val8 = '24'
val9 = '00'
val10 = '60'

mycursor.execute(sql, (val1, val2, val3, val4, val5, val6, val7, val8, val9, val10))
myresult = mycursor.fetchall()

print(myresult)
