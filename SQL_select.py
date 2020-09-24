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

my_cursor = mydb.cursor()

year = 2020
year2 = 2020
month = 9
month2 = 9
day = 12
day2 = 12
h1 = 14
h2 = 15
h3 = 13
h4 = 12
m1 = 15
m2 = 15
m3 = 0
m4 = 60

query1 = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup), SUM(autoserv), SUM(ppr), SUM(break), SUM(material), ' \
       'SUM(task), SUM(maket) FROM worktime WHERE (year = (%s)) AND (month = (%s)) AND (day = (%s)) ' \
       'AND (hours BETWEEN (%s) AND (%s))'

query2 = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup), SUM(autoserv), SUM(ppr), SUM(break), SUM(material), ' \
       'SUM(task), SUM(maket) FROM worktime WHERE (year = (%s)) AND (month = (%s)) ' \
       'AND (day = (%s)) AND (hours = (%s)) AND (minutes BETWEEN (%s) AND (%s))'


def sql5(sql, val1, val2, val3, val4, val5):
    my_cursor.execute(sql, (val1, val2, val3, val4, val5))


def sql6(sql, val1, val2, val3, val4, val5, val6):
    my_cursor.execute(sql, (val1, val2, val3, val4, val5, val6))


def main(sql):
    result = my_cursor.fetchall()
    my_result = (result[0])
    total1 = my_result.get('SUM(totaltime)')
    plan1 = my_result.get('SUM(plantime)')
    setup1 = my_result.get('SUM(setup)')
    autoserv1 = my_result.get('SUM(autoserv)')
    ppr1 = my_result.get('SUM(ppr)')
    break1 = my_result.get('SUM(break)')
    material1 = my_result.get('SUM(material)')
    task1 = my_result.get('SUM(task)')
    maket1 = my_result.get('SUM(maket)')
    print('total: ' + str(total1), 'plan: ' + str(plan1), 'setup: ' + str(setup1), 'autoserv: ' + str(autoserv1),
          'ppr: ' + str(ppr1), 'break: ' + str(break1), 'material: ' + str(material1), 'task: ' + str(task1),
          'maket: ' + str(maket1))


def total(sql):
    result = my_cursor.fetchall()
    my_result = (result[0])
    total1 = my_result.get('SUM(totaltime)')
    return total1


def plan(sql):
    result = my_cursor.fetchall()
    my_result = (result[0])
    plan1 = my_result.get('SUM(plantime)')
    return plan1


def act():
    if year == year2:
        print('year = year2')
        if month == month2:
            print('month = month2')
            if day == day2:
                print('day = day2')
                if h1 == h2:
                    print('h1 = h2')
                    if m1 == m2:
                        print('m1 = m2')
                        pass
                    elif m1 <= m2:
                        print('m1 <= m2')
                        pass
                elif h1 <= h2:
                    print('h1 <= h2')
                    pass
                    if m1 == m2:
                        print('m1 = m2')
                        main(sql6(query2, year, month, day, h4, m1, m4))
                        main(sql5(query1, year, month, day, h3, h1))
                        main(sql6(query2, year, month, day, h1, m3, m1))
                        print('total: ' + str(total(sql6(query2, year, month, day, h4, m1, m4)) +
                              total(sql5(query1, year, month, day, h3, h1)) +
                              total(sql6(query2, year, month, day, h1, m3, m1))))
                        print('plan: ' + str(plan(sql6(query2, year, month, day, h4, m1, m4)) +
                              plan(sql5(query1, year, month, day, h3, h1)) +
                              plan(sql6(query2, year, month, day, h1, m3, m1))))
                    elif m1 <= m2:
                        print('m1 <= m2')
                        main(sql5(query1, year, month, day, h4, h1))
                        main(sql6(query2, year, month, day, h1, m1, m2))
                        print('total: ' + str(total(sql5(query1, year, month, day, h4, h1)) +
                              total(sql6(query2, year, month, day, h1, m1, m2))))
                        print('plan: ' + str(plan(sql5(query1, year, month, day, h4, h1)) +
                              plan(sql6(query2, year, month, day, h1, m1, m2))))


act()
