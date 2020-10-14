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

name = ['Laser1', 'Laser2', 'Punch1', 'Punch2', 'Bend1', 'Bend2', 'Weld1', 'Weld2', 'Weld_Robot1',  'Weld_Robot2',
        'Assembly1', 'Assembly2', 'Cleaning1', 'Cleaning2']
starts = ['start_plan_counter',  'start_setup', 'start_auto_service', 'start_break', 'start_material', 'start_task',
          'start_ppr', 'start_model', ]
stops = ['stop_plan_counter', 'stop_setup', 'stop_auto_service', 'stop_break', 'stop_material', 'stop_task',
         'stop_ppr', 'stop_model']
temp1 = []
temp2 = []


def days(val):
    if val == 1 or val == 3 or val == 5 or val == 7 or val == 8 or val == 10 or val == 12:
        r = range(31)
        return r
    elif val == 2:
        r = range(29)
        return r
    else:
        r = range(30)
        return r


query = 'INSERT INTO worktime (name, action, totaltime, plantime, setup, autoserv, ppr, break, material,' \
        'task, maket, secs, minutes, hours, day, month, year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,' \
        ' %s, %s, %s, %s, %s, %s, %s, %s)'

for i in range(1):
    m = i + 1
    for k in range(1):
        d = k + 1
        for h in range(1):
            for min in range(60):
                if random.randint(1, 20) == 1:
                    day = d
                    month = m
                    year = 2020
                    hours = h
                    minutes = min
                    secs = random.choice(range(0, 60))
                    name2 = random.choice(name)
                    action2 = random.choice(starts)
                    if action2 == starts[0]:
                        print('success plan counter')
                        if hours <= 7 and minutes < 45:
                            total = ((24 - 21) * 60 * 60 + 30 * 60) + (hours * 60 * 60 + minutes * 60)
                            plan = ((24 - 21) * 60 * 60 + 30 * 60) + (hours * 60 * 60 + minutes * 60)
                            setup = 0
                            auto = 0
                            ppr = 0
                            break1 = 0
                            material = 0
                            task = 0
                            model = 0
                            my_cursor.execute(query, (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                      task, model, secs, minutes, hours, day, month, year))
                            my_db.commit()
                            temp1.append(name2)
                            name.remove(name2)
                        else:
                            total = (hours * 60 * 60 + minutes * 60) - (7 * 60 * 60 + 45 * 60)
                            plan = (hours * 60 * 60 + minutes * 60) - (7 * 60 * 60 + 45 * 60)
                            setup = 0
                            auto = 0
                            ppr = 0
                            break1 = 0
                            material = 0
                            task = 0
                            model = 0
                            my_cursor.execute(query,
                                              (name2, action2, total, plan, setup, auto, ppr, break1, material, task,
                                               model, secs, minutes, hours, day, month, year))
                            my_db.commit()
                            temp1.append(name2)
                            name.remove(name2)
                        if len(temp1) != 0:
                            pass
