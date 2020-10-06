import pymysql
import random

my_db = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='mydb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

my_cursor = my_db.cursor()

name = ['Laser1', 'Laser2', 'Punch', 'Bend1', 'Bend2', 'Bend3', 'Weld', 'Weld_Robot', 'Assembly', 'Cleaning']
action = ['start_plan_counter', 'stop_plan_counter', 'start_setup', 'stop_setup', 'start_auto_service',
          'stop_auto_service', 'start_break', 'stop_break', 'start_material', 'stop_material', 'start_task',
          'stop_task', 'start_ppr', 'stop_ppr', 'start_model', 'stop_model']


def tot(val):
    if val != 0:
        return val


def act():
    query = 'INSERT INTO worktime (name, action, totaltime, plantime, setup, autoserv, ppr, break, material,' \
            'task, maket, secs, minutes, hours, day, month, year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,' \
            ' %s, %s, %s, %s, %s, %s, %s, %s)'
    for i in range(1):
        m = i + 1
        for k in range(1):
            d = k + 1
            for word in name:
                name2 = word
                action2 = 'start'
                total = 0
                plan = 0
                setup = 0
                auto = 0
                ppr = 0
                break1 = 0
                material = 0
                task = 0
                model = 0
                secs = random.choice(range(0, 60))
                minutes = random.choice(range(45, 59))
                hours = 7
                day = d
                month = m
                year = 2020
                my_cursor.execute(query, (name2, action2, total, plan, setup, auto, ppr, break1, material, task,
                                          model, secs, minutes, hours, day, month, year))
                my_db.commit()
            # for a in range(random.choice(range(14, 40))):
            #     name2 = random.choice(name)
            #     action2 = random.choice(action)
            #     total = random.choice(range(0, 3200))
            #     plan = random.choice(range(0, 3200))
            #     setup = random.choice(range(0, 3200))
            #     auto = random.choice(range(0, 3200))
            #     ppr = random.choice(range(0, 3200))
            #     break1 = random.choice(range(0, 3200))
            #     material = random.choice(range(0, 3200))
            #     task = random.choice(range(0, 3200))
            #     model = random.choice(range(0, 3200))
            #     secs = random.choice(range(0, 60))
            #     minutes = random.choice(range(0, 60))
            #     hours = random.choice(range(0, 23))
            #     day = d
            #     month = m
            #     year = 2020
            #     my_cursor.execute(query, (name2, action2, total, plan, setup, auto, ppr, break1, material, task,
            #                               model, secs, minutes, hours, day, month, year))
            #     my_db.commit()


act()
