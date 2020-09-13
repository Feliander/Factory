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

year = 2020
year2 = 2020
month = 9
month2 = 9
day = 12
day2 = 12
h1 = 14
h2 = 15
h3 = 13
m1 = 30
m2 = 60


def act():
    if year == year2:
        print('year == year2')
        if month == month2:
            print('month == month2')
            if day == day2:
                print('day == day2')
                if h1 == h2:
                    print('h1 == h2')
                    if m1 == m2:
                        print('m1 == m2')
                        pass
                    elif m1 <= m2:
                        print('m1 <= m2')
                        pass
                elif h1 <= h2:
                    print('h1 <= h2')
                    pass
                    if m1 == m2:
                        print('m1 == m2')
                        pass
                    elif m1 <= m2:
                        print('m1 <= m2')
                        main(query)


query = 'SELECT SUM(totaltime) + (SELECT SUM(totaltime) FROM worktime WHERE (year = (%s)) AND (month = (%s)) ' \
        'AND (day = (%s)) AND (hours = (%s)) AND (minutes BETWEEN (%s) AND (%s))) as SumTotal, ' \
        'SUM(plantime) + (SELECT SUM(plantime) FROM worktime WHERE (year = (%s)) AND (month = (%s)) ' \
        'AND (day = (%s)) AND (hours = (%s)) AND (minutes BETWEEN (%s) AND (%s))) as SumPlan, ' \
        'SUM(setup) + (SELECT SUM(setup) FROM worktime WHERE (year = (%s)) AND (month = (%s)) ' \
        'AND (day = (%s)) AND (hours = (%s)) AND (minutes BETWEEN (%s) AND (%s))) as SumSetup, ' \
        'SUM(autoserv) + (SELECT SUM(autoserv) FROM worktime WHERE (year = (%s)) AND (month = (%s)) ' \
        'AND (day = (%s)) AND (hours = (%s)) AND (minutes BETWEEN (%s) AND (%s))) as SumAutoserv, ' \
        'SUM(ppr) + (SELECT SUM(ppr) FROM worktime WHERE (year = (%s)) AND (month = (%s)) ' \
        'AND (day = (%s)) AND (hours = (%s)) AND (minutes BETWEEN (%s) AND (%s))) as SumPpr, ' \
        'SUM(break) + (SELECT SUM(break) FROM worktime WHERE (year = (%s)) AND (month = (%s)) ' \
        'AND (day = (%s)) AND (hours = (%s)) AND (minutes BETWEEN (%s) AND (%s))) as SumBreak, ' \
        'SUM(material) + (SELECT SUM(material) FROM worktime WHERE (year = (%s)) AND (month = (%s)) ' \
        'AND (day = (%s)) AND (hours = (%s)) AND (minutes BETWEEN (%s) AND (%s))) as SumMaterial, ' \
        'SUM(task) + (SELECT SUM(task) FROM worktime WHERE (year = (%s)) AND (month = (%s)) ' \
        'AND (day = (%s)) AND (hours = (%s)) AND (minutes BETWEEN (%s) AND (%s))) as SumTask, ' \
        'SUM(maket) + (SELECT SUM(setup) FROM worktime WHERE (year = (%s)) AND (month = (%s)) ' \
        'AND (day = (%s)) AND (hours = (%s)) AND (minutes BETWEEN (%s) AND (%s))) as SumMaket ' \
        'FROM worktime WHERE (year = (%s)) AND (month = (%s)) AND (day = (%s)) AND (hours BETWEEN (%s) AND (%s))'


def main(sql):
    mycursor.execute(sql, (
        year, month, day, h3, m1, m2, year, month, day, h3, m1, m2, year, month, day, h3, m1, m2,
        year, month, day, h3, m1, m2, year, month, day, h3, m1, m2, year, month, day, h3, m1, m2,
        year, month, day, h3, m1, m2, year, month, day, h3, m1, m2, year, month, day, h3, m1, m2,
        year, month, day, h1, h2))
    result = mycursor.fetchall()
    my_result = (result[0])
    total1 = my_result.get('SumTotal')
    print(total1)
    print(result)


act()
