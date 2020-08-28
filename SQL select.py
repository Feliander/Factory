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

val1 = '2020'
val2 = '2020'
val3 = '01'
val4 = '12'


def sql():
    if val1 == '2020' and val2 == '2020':
        if val3 == '01' and val4 == '12':
            sql = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
                  'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
                  'SUM(task), SUM(maket) FROM worktime WHERE (year = 2020) AND (month BETWEEN 1 AND 12)'
            return sql



mycursor.execute(sql())
myresult = mycursor.fetchall()
print(myresult)



