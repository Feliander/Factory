import pymysql
import datetime

my_db = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='mydb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

my_cursor = my_db.cursor()

name = ['Laser1', 'Laser2', 'Punch', 'Bend1', 'Bend2', 'Bend3', 'Weld', 'Weld_Robot']

sql = 'INSERT INTO worktime (name, action, totaltime, plantime, setup, autoserv, ppr, break, material,' \
      'task, maket, secs, minutes, hours, day, month, year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,' \
      ' %s, %s, %s, %s, %s, %s, %s, %s)'
val1 = 'all'
val2 = 'manual'
val3 = 10000
val4 = 100
val5 = 100
val6 = 100
val7 = 100
val8 = 100
val9 = 100
val10 = 100
val11 = 100
val12 = datetime.datetime.strftime(datetime.datetime.now(), "%S")
# val13 = datetime.datetime.strftime(datetime.datetime.now(), "%M")
# val14 = datetime.datetime.strftime(datetime.datetime.now(), "%H")
# val15 = datetime.datetime.strftime(datetime.datetime.now(), "%d")
# val16 = datetime.datetime.strftime(datetime.datetime.now(), "%m")
# val17 = datetime.datetime.strftime(datetime.datetime.now(), "%Y")'
val13 = 11
val14 = 17
val15 = 12
val16 = 9
val17 = 2020
my_cursor.execute(sql, (val1, val2, val3, val4, val5, val6,
                        val7, val8, val9, val10, val11, val12,
                        val13, val14, val15, val16, val17))

my_db.commit()
