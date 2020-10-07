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
temp = []


def act():
    query = 'INSERT INTO worktime (name, action, totaltime, plantime, setup, autoserv, ppr, break, material,' \
            'task, maket, secs, minutes, hours, day, month, year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,' \
            ' %s, %s, %s, %s, %s, %s, %s, %s)'
    for i in range(1):
        m = i + 1
        for k in range(1):
            d = k + 1
            for word in name:
                if random.randint(1, 20) == 1:
                    name3 = word
                    name.remove(name3)
                else:
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
            for a in range(random.choice(range(0, 8))):
                day = d
                month = m
                year = 2020
                name2 = random.choice(name)
                action2 = starts[0]
                if action2 == 'start_plan_counter':
                    print('Success')
                    hours = random.choice(range(8, 10))
                    h1 = hours * 60 * 60
                    minutes = random.choice(range(0, 59))
                    m1 = minutes * 60
                    secs = random.choice(range(0, 60))
                    s1 = secs
                    total = h1 + m1 + s1
                    plan = h1 + m1 + s1
                    setup = 0
                    auto = 0
                    ppr = 0
                    break1 = 0
                    material = 0
                    task = 0
                    model = 0
                    my_cursor.execute(query, (name2, action2, total, plan, setup, auto, ppr, break1, material, task,
                                              model, secs, minutes, hours, day, month, year))
                    my_db.commit()
                    temp.append(name2)
                    name.remove(name2)


act()
