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

name = ['Laser1', 'Laser2', 'Punch1', 'Punch2', 'Bend1', 'Bend2', 'Weld1', 'Weld2', 'Weld_Robot1', 'Weld_Robot2',
        'Assembly1', 'Assembly2', 'Cleaning1', 'Cleaning2']
starts = ['start_plan_counter', 'start_setup', 'start_auto_service', 'start_break', 'start_material', 'start_task',
          'start_ppr', 'start_model', ]
stops = ['stop_plan_counter', 'stop_setup', 'stop_auto_service', 'stop_break', 'stop_material', 'stop_task',
         'stop_ppr', 'stop_model']
temp1 = {}
temp3 = []


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
        for h in range(24):
            for min in range(60):
                if len(name) == 0:
                    for word in temp3:
                        if random.randint(1, 2) == 1:
                            day = d
                            month = m
                            year = 2020
                            name3 = word
                            temporary = temp1.get(name3)
                            action = temporary[0]
                            num = temporary[1]
                            secs = temporary[2]
                            minutes = temporary[3]
                            hours = temporary[4]
                            total2 = hours * 60 * 60 + minutes * 60 + secs
                            if action == starts[0]:
                                action3 = stops[0]
                                time = random.choice(range(300, 1800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[1]:
                                action3 = stops[1]
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[2]:
                                action3 = stops[2]
                                time = random.choice(range(900, 1800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[3]:
                                action3 = stops[3]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(900, 3600))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[4]:
                                action3 = stops[4]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(3600, 10800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[5]:
                                action3 = stops[5]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[6]:
                                action3 = stops[6]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[7]:
                                action3 = stops[7]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(600, 7200))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                        else:
                            pass
                elif h == 0:
                    if len(name) != 14:
                        for word in temp3:
                            day = d
                            month = m
                            year = 2020
                            name3 = word
                            temporary = temp1.get(name3)
                            action = temporary[0]
                            num = temporary[1]
                            secs = temporary[2]
                            minutes = temporary[3]
                            hours = temporary[4]
                            total2 = hours * 60 * 60 + minutes * 60 + secs
                            if action == starts[0]:
                                action3 = stops[0]
                                time = random.choice(range(300, 1800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[1]:
                                action3 = stops[1]
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[2]:
                                action3 = stops[2]
                                time = random.choice(range(900, 1800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[3]:
                                action3 = stops[3]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(900, 3600))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[4]:
                                action3 = stops[4]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(3600, 10800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[5]:
                                action3 = stops[5]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[6]:
                                action3 = stops[6]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[7]:
                                action3 = stops[7]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(600, 7200))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = random.choice(range(0, 3))
                            secs = random.choice(range(0, 60))
                            name2 = word
                            action2 = starts[0]
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) + ((3 * 60 * 60) + (30 * 60))
                            plan = 0
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
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes1 = random.choice(range(30, 35))
                            secs1 = random.choice(range(0, 60))
                            time = minutes1 * 60 - minutes * 60 + secs1 - secs
                            name2 = word
                            action2 = stops[0]
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) + ((3 * 60 * 60) + (30 * 60)) + time
                            plan = time
                            setup = 0
                            auto = 0
                            ppr = 0
                            break1 = 0
                            material = 0
                            task = 0
                            model = 0
                            my_cursor.execute(query, (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                      task, model, secs1, minutes1, hours, day, month, year))
                            my_db.commit()
                        h += 1
                    elif min / 15 == 1 or min / 15 == 2 or min / 15 == 3 or min / 15 == 4:
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = min
                            secs = random.choice(range(0, 60))
                            time = (hours * 60 * 60) + (minutes * 60) + secs
                            name2 = random.choice(name)
                            action2 = 'checkpoint'
                            if time < (7 * 60 * 60) + (45 * 60) + 0:
                                total = ((3 * 60 * 60) + (30 * 60) + 0) + time
                                plan = 0
                                setup = 0
                                auto = 0
                                ppr = 0
                                break1 = 0
                                material = 0
                                task = 0
                                model = 0
                                my_cursor.execute(query,
                                                  (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                   task, model, secs, minutes, hours, day, month, year))
                                my_db.commit()
                            elif (7 * 60 * 60) + (45 * 60) + 0 < time < (20 * 60 * 60) + (30 * 60) + 0:
                                total = time - ((7 * 60 * 60) + (45 * 60) + 0)
                                plan = 0
                                setup = 0
                                auto = 0
                                ppr = 0
                                break1 = 0
                                material = 0
                                task = 0
                                model = 0
                                my_cursor.execute(query,
                                                  (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                   task, model, secs, minutes, hours, day, month, year))
                                my_db.commit()
                            elif time > (20 * 60 * 60) + (30 * 60) + 0:
                                total = time - ((20 * 60 * 60) + (30 * 60) + 0)
                                plan = 0
                                setup = 0
                                auto = 0
                                ppr = 0
                                break1 = 0
                                material = 0
                                task = 0
                                model = 0
                                my_cursor.execute(query,
                                                  (
                                                  name2, action2, total, plan, setup, auto, ppr, break1, material, task,
                                                  model, secs, minutes, hours, day, month, year))
                                my_db.commit()
                    else:
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = random.choice(range(0, 3))
                            secs = random.choice(range(0, 60))
                            name2 = word
                            action2 = starts[0]
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) + ((3 * 60 * 60) + (30 * 60))
                            plan = 0
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
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes1 = random.choice(range(30, 35))
                            secs1 = random.choice(range(0, 60))
                            time = minutes1 * 60 - minutes * 60 + secs1 - secs
                            name2 = word
                            action2 = stops[0]
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) + ((3 * 60 * 60) + (30 * 60)) + time
                            plan = time
                            setup = 0
                            auto = 0
                            ppr = 0
                            break1 = 0
                            material = 0
                            task = 0
                            model = 0
                            my_cursor.execute(query, (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                      task, model, secs1, minutes1, hours, day, month, year))
                            my_db.commit()
                        h += 1
                elif min/15 == 1 or min/15 == 2 or min/15 == 3 or min/15 == 4:
                    for word in name:
                        day = d
                        month = m
                        year = 2020
                        hours = h
                        minutes = min
                        secs = random.choice(range(0, 60))
                        time = (hours * 60 * 60) + (minutes * 60) + secs
                        name2 = random.choice(name)
                        action2 = 'checkpoint'
                        if time < (7 * 60 * 60) + (45 * 60) + 0:
                            total = ((3 * 60 * 60) + (30 * 60) + 0) + time
                            plan = 0
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
                        elif (7 * 60 * 60) + (45 * 60) + 0 < time < (20 * 60 * 60) + (30 * 60) + 0:
                            total = time - ((7 * 60 * 60) + (45 * 60) + 0)
                            plan = 0
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
                        elif time > (20 * 60 * 60) + (30 * 60) + 0:
                            total = time - ((20 * 60 * 60) + (30 * 60) + 0)
                            plan = 0
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
                elif h == 5:
                    if len(name) != 14:
                        for word in temp3:
                            day = d
                            month = m
                            year = 2020
                            name3 = word
                            temporary = temp1.get(name3)
                            action = temporary[0]
                            num = temporary[1]
                            secs = temporary[2]
                            minutes = temporary[3]
                            hours = temporary[4]
                            total2 = hours * 60 * 60 + minutes * 60 + secs
                            if action == starts[0]:
                                action3 = stops[0]
                                time = random.choice(range(300, 1800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[1]:
                                action3 = stops[1]
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[2]:
                                action3 = stops[2]
                                time = random.choice(range(900, 1800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[3]:
                                action3 = stops[3]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(900, 3600))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[4]:
                                action3 = stops[4]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(3600, 10800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[5]:
                                action3 = stops[5]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[6]:
                                action3 = stops[6]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[7]:
                                action3 = stops[7]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(600, 7200))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = random.choice(range(0, 3))
                            secs = random.choice(range(0, 60))
                            name2 = word
                            action2 = starts[0]
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) + ((3 * 60 * 60) + (30 * 60))
                            plan = 0
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
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes1 = random.choice(range(30, 35))
                            secs1 = random.choice(range(0, 60))
                            time = minutes1 * 60 - minutes * 60 + secs1 - secs
                            name2 = word
                            action2 = stops[0]
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) + ((3 * 60 * 60) + (30 * 60)) + time
                            plan = time
                            setup = 0
                            auto = 0
                            ppr = 0
                            break1 = 0
                            material = 0
                            task = 0
                            model = 0
                            my_cursor.execute(query, (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                      task, model, secs1, minutes1, hours, day, month, year))
                            my_db.commit()
                        h += 1
                    elif min / 15 == 1 or min / 15 == 2 or min / 15 == 3 or min / 15 == 4:
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = min
                            secs = random.choice(range(0, 60))
                            time = (hours * 60 * 60) + (minutes * 60) + secs
                            name2 = random.choice(name)
                            action2 = 'checkpoint'
                            if time < (7 * 60 * 60) + (45 * 60) + 0:
                                total = ((3 * 60 * 60) + (30 * 60) + 0) + time
                                plan = 0
                                setup = 0
                                auto = 0
                                ppr = 0
                                break1 = 0
                                material = 0
                                task = 0
                                model = 0
                                my_cursor.execute(query,
                                                  (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                   task, model, secs, minutes, hours, day, month, year))
                                my_db.commit()
                            elif (7 * 60 * 60) + (45 * 60) + 0 < time < (20 * 60 * 60) + (30 * 60) + 0:
                                total = time - ((7 * 60 * 60) + (45 * 60) + 0)
                                plan = 0
                                setup = 0
                                auto = 0
                                ppr = 0
                                break1 = 0
                                material = 0
                                task = 0
                                model = 0
                                my_cursor.execute(query,
                                                  (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                   task, model, secs, minutes, hours, day, month, year))
                                my_db.commit()
                            elif time > (20 * 60 * 60) + (30 * 60) + 0:
                                total = time - ((20 * 60 * 60) + (30 * 60) + 0)
                                plan = 0
                                setup = 0
                                auto = 0
                                ppr = 0
                                break1 = 0
                                material = 0
                                task = 0
                                model = 0
                                my_cursor.execute(query,
                                                  (
                                                  name2, action2, total, plan, setup, auto, ppr, break1, material, task,
                                                  model, secs, minutes, hours, day, month, year))
                                my_db.commit()
                    else:
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = random.choice(range(0, 3))
                            secs = random.choice(range(0, 60))
                            name2 = word
                            action2 = starts[0]
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) + ((3 * 60 * 60) + (30 * 60))
                            plan = 0
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
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes1 = random.choice(range(30, 35))
                            secs1 = random.choice(range(0, 60))
                            time = minutes1 * 60 - minutes * 60 + secs1 - secs
                            name2 = word
                            action2 = stops[0]
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) + ((3 * 60 * 60) + (30 * 60)) + time
                            plan = time
                            setup = 0
                            auto = 0
                            ppr = 0
                            break1 = 0
                            material = 0
                            task = 0
                            model = 0
                            my_cursor.execute(query, (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                      task, model, secs1, minutes1, hours, day, month, year))
                            my_db.commit()
                        h += 1
                elif h == 7:
                    if len(name) != 14:
                        for word in temp3:
                            day = d
                            month = m
                            year = 2020
                            name3 = word
                            temporary = temp1.get(name3)
                            action = temporary[0]
                            num = temporary[1]
                            secs = temporary[2]
                            minutes = temporary[3]
                            hours = temporary[4]
                            total2 = hours * 60 * 60 + minutes * 60 + secs
                            if action == starts[0]:
                                action3 = stops[0]
                                time = random.choice(range(300, 1800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[1]:
                                action3 = stops[1]
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[2]:
                                action3 = stops[2]
                                time = random.choice(range(900, 1800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[3]:
                                action3 = stops[3]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(900, 3600))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[4]:
                                action3 = stops[4]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(3600, 10800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[5]:
                                action3 = stops[5]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[6]:
                                action3 = stops[6]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[7]:
                                action3 = stops[7]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(600, 7200))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = random.choice(range(36, 42))
                            secs = random.choice(range(0, 60))
                            name2 = word
                            action2 = 'stop'
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) + ((3 * 60 * 60) + (30 * 60))
                            plan = 0
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
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = random.choice(range(43, 51))
                            secs = random.choice(range(0, 60))
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
                            my_cursor.execute(query, (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                      task, model, secs, minutes, hours, day, month, year))
                            my_db.commit()
                        h += 1
                    elif min / 15 == 1 or min / 15 == 2 or min / 15 == 3 or min / 15 == 4:
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = min
                            secs = random.choice(range(0, 60))
                            time = (hours * 60 * 60) + (minutes * 60) + secs
                            name2 = random.choice(name)
                            action2 = 'checkpoint'
                            if time < (7 * 60 * 60) + (45 * 60) + 0:
                                total = ((3 * 60 * 60) + (30 * 60) + 0) + time
                                plan = 0
                                setup = 0
                                auto = 0
                                ppr = 0
                                break1 = 0
                                material = 0
                                task = 0
                                model = 0
                                my_cursor.execute(query,
                                                  (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                   task, model, secs, minutes, hours, day, month, year))
                                my_db.commit()
                            elif (7 * 60 * 60) + (45 * 60) + 0 < time < (20 * 60 * 60) + (30 * 60) + 0:
                                total = time - ((7 * 60 * 60) + (45 * 60) + 0)
                                plan = 0
                                setup = 0
                                auto = 0
                                ppr = 0
                                break1 = 0
                                material = 0
                                task = 0
                                model = 0
                                my_cursor.execute(query,
                                                  (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                   task, model, secs, minutes, hours, day, month, year))
                                my_db.commit()
                            elif time > (20 * 60 * 60) + (30 * 60) + 0:
                                total = time - ((20 * 60 * 60) + (30 * 60) + 0)
                                plan = 0
                                setup = 0
                                auto = 0
                                ppr = 0
                                break1 = 0
                                material = 0
                                task = 0
                                model = 0
                                my_cursor.execute(query,
                                                  (
                                                  name2, action2, total, plan, setup, auto, ppr, break1, material, task,
                                                  model, secs, minutes, hours, day, month, year))
                                my_db.commit()
                    else:
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = random.choice(range(36, 42))
                            secs = random.choice(range(0, 60))
                            name2 = word
                            action2 = 'stop'
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) + ((3 * 60 * 60) + (30 * 60))
                            plan = 0
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
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = random.choice(range(43, 51))
                            secs = random.choice(range(0, 60))
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
                            my_cursor.execute(query, (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                      task, model, secs, minutes, hours, day, month, year))
                            my_db.commit()
                        h += 1
                elif h == 12:
                    if len(name) != 14:
                        for word in temp3:
                            day = d
                            month = m
                            year = 2020
                            name3 = word
                            temporary = temp1.get(name3)
                            action = temporary[0]
                            num = temporary[1]
                            secs = temporary[2]
                            minutes = temporary[3]
                            hours = temporary[4]
                            total2 = hours * 60 * 60 + minutes * 60 + secs
                            if action == starts[0]:
                                action3 = stops[0]
                                time = random.choice(range(300, 1800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[1]:
                                action3 = stops[1]
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[2]:
                                action3 = stops[2]
                                time = random.choice(range(900, 1800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[3]:
                                action3 = stops[3]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(900, 3600))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[4]:
                                action3 = stops[4]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(3600, 10800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[5]:
                                action3 = stops[5]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[6]:
                                action3 = stops[6]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[7]:
                                action3 = stops[7]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(600, 7200))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = random.choice(range(0, 3))
                            secs = random.choice(range(0, 60))
                            name2 = word
                            action2 = starts[0]
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) - (7 * 60 * 60 + 45 * 60)
                            plan = 0
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
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes1 = random.choice(range(30, 35))
                            secs1 = random.choice(range(0, 60))
                            time = minutes1 * 60 - minutes * 60 + secs1 - secs
                            name2 = word
                            action2 = stops[0]
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) - (7 * 60 * 60 + 45 * 60) + time
                            plan = time
                            setup = 0
                            auto = 0
                            ppr = 0
                            break1 = 0
                            material = 0
                            task = 0
                            model = 0
                            my_cursor.execute(query, (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                      task, model, secs1, minutes1, hours, day, month, year))
                            my_db.commit()
                        h += 1
                    elif min / 15 == 1 or min / 15 == 2 or min / 15 == 3 or min / 15 == 4:
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = min
                            secs = random.choice(range(0, 60))
                            time = (hours * 60 * 60) + (minutes * 60) + secs
                            name2 = random.choice(name)
                            action2 = 'checkpoint'
                            if time < (7 * 60 * 60) + (45 * 60) + 0:
                                total = ((3 * 60 * 60) + (30 * 60) + 0) + time
                                plan = 0
                                setup = 0
                                auto = 0
                                ppr = 0
                                break1 = 0
                                material = 0
                                task = 0
                                model = 0
                                my_cursor.execute(query,
                                                  (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                   task, model, secs, minutes, hours, day, month, year))
                                my_db.commit()
                            elif (7 * 60 * 60) + (45 * 60) + 0 < time < (20 * 60 * 60) + (30 * 60) + 0:
                                total = time - ((7 * 60 * 60) + (45 * 60) + 0)
                                plan = 0
                                setup = 0
                                auto = 0
                                ppr = 0
                                break1 = 0
                                material = 0
                                task = 0
                                model = 0
                                my_cursor.execute(query,
                                                  (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                   task, model, secs, minutes, hours, day, month, year))
                                my_db.commit()
                            elif time > (20 * 60 * 60) + (30 * 60) + 0:
                                total = time - ((20 * 60 * 60) + (30 * 60) + 0)
                                plan = 0
                                setup = 0
                                auto = 0
                                ppr = 0
                                break1 = 0
                                material = 0
                                task = 0
                                model = 0
                                my_cursor.execute(query,
                                                  (
                                                  name2, action2, total, plan, setup, auto, ppr, break1, material, task,
                                                  model, secs, minutes, hours, day, month, year))
                                my_db.commit()
                    else:
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = random.choice(range(0, 3))
                            secs = random.choice(range(0, 60))
                            name2 = word
                            action2 = starts[0]
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) - (7 * 60 * 60 + 45 * 60)
                            plan = 0
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
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes1 = random.choice(range(30, 35))
                            secs1 = random.choice(range(0, 60))
                            time = minutes1 * 60 - minutes * 60 + secs1 - secs
                            name2 = word
                            action2 = stops[0]
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) - (7 * 60 * 60 + 45 * 60) + time
                            plan = time
                            setup = 0
                            auto = 0
                            ppr = 0
                            break1 = 0
                            material = 0
                            task = 0
                            model = 0
                            my_cursor.execute(query, (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                      task, model, secs1, minutes1, hours, day, month, year))
                            my_db.commit()
                        h += 1
                elif h == 17:
                    if len(name) != 14:
                        for word in temp3:
                            day = d
                            month = m
                            year = 2020
                            name3 = word
                            temporary = temp1.get(name3)
                            action = temporary[0]
                            num = temporary[1]
                            secs = temporary[2]
                            minutes = temporary[3]
                            hours = temporary[4]
                            total2 = hours * 60 * 60 + minutes * 60 + secs
                            if action == starts[0]:
                                action3 = stops[0]
                                time = random.choice(range(300, 1800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[1]:
                                action3 = stops[1]
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[2]:
                                action3 = stops[2]
                                time = random.choice(range(900, 1800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[3]:
                                action3 = stops[3]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(900, 3600))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[4]:
                                action3 = stops[4]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(3600, 10800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[5]:
                                action3 = stops[5]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[6]:
                                action3 = stops[6]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[7]:
                                action3 = stops[7]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(600, 7200))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = random.choice(range(0, 3))
                            secs = random.choice(range(0, 60))
                            name2 = word
                            action2 = starts[0]
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) - (7 * 60 * 60 + 45 * 60)
                            plan = 0
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
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes1 = random.choice(range(30, 35))
                            secs1 = random.choice(range(0, 60))
                            time = minutes1 * 60 - minutes * 60 + secs1 - secs
                            name2 = word
                            action2 = stops[0]
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) - (7 * 60 * 60 + 45 * 60) + time
                            plan = time
                            setup = 0
                            auto = 0
                            ppr = 0
                            break1 = 0
                            material = 0
                            task = 0
                            model = 0
                            my_cursor.execute(query, (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                      task, model, secs1, minutes1, hours, day, month, year))
                            my_db.commit()
                        h += 1
                    elif min / 15 == 1 or min / 15 == 2 or min / 15 == 3 or min / 15 == 4:
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = min
                            secs = random.choice(range(0, 60))
                            time = (hours * 60 * 60) + (minutes * 60) + secs
                            name2 = random.choice(name)
                            action2 = 'checkpoint'
                            if time < (7 * 60 * 60) + (45 * 60) + 0:
                                total = ((3 * 60 * 60) + (30 * 60) + 0) + time
                                plan = 0
                                setup = 0
                                auto = 0
                                ppr = 0
                                break1 = 0
                                material = 0
                                task = 0
                                model = 0
                                my_cursor.execute(query,
                                                  (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                   task, model, secs, minutes, hours, day, month, year))
                                my_db.commit()
                            elif (7 * 60 * 60) + (45 * 60) + 0 < time < (20 * 60 * 60) + (30 * 60) + 0:
                                total = time - ((7 * 60 * 60) + (45 * 60) + 0)
                                plan = 0
                                setup = 0
                                auto = 0
                                ppr = 0
                                break1 = 0
                                material = 0
                                task = 0
                                model = 0
                                my_cursor.execute(query,
                                                  (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                   task, model, secs, minutes, hours, day, month, year))
                                my_db.commit()
                            elif time > (20 * 60 * 60) + (30 * 60) + 0:
                                total = time - ((20 * 60 * 60) + (30 * 60) + 0)
                                plan = 0
                                setup = 0
                                auto = 0
                                ppr = 0
                                break1 = 0
                                material = 0
                                task = 0
                                model = 0
                                my_cursor.execute(query,
                                                  (
                                                  name2, action2, total, plan, setup, auto, ppr, break1, material, task,
                                                  model, secs, minutes, hours, day, month, year))
                                my_db.commit()
                    else:
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = random.choice(range(0, 3))
                            secs = random.choice(range(0, 60))
                            name2 = word
                            action2 = starts[0]
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) - (7 * 60 * 60 + 45 * 60)
                            plan = 0
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
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes1 = random.choice(range(30, 35))
                            secs1 = random.choice(range(0, 60))
                            time = minutes1 * 60 - minutes * 60 + secs1 - secs
                            name2 = word
                            action2 = stops[0]
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) - (7 * 60 * 60 + 45 * 60) + time
                            plan = time
                            setup = 0
                            auto = 0
                            ppr = 0
                            break1 = 0
                            material = 0
                            task = 0
                            model = 0
                            my_cursor.execute(query, (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                      task, model, secs1, minutes1, hours, day, month, year))
                            my_db.commit()
                        h += 1
                elif h == 20:
                    if len(name) != 14:
                        for word in temp3:
                            day = d
                            month = m
                            year = 2020
                            name3 = word
                            temporary = temp1.get(name3)
                            action = temporary[0]
                            num = temporary[1]
                            secs = temporary[2]
                            minutes = temporary[3]
                            hours = temporary[4]
                            total2 = hours * 60 * 60 + minutes * 60 + secs
                            if action == starts[0]:
                                action3 = stops[0]
                                time = random.choice(range(300, 1800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[1]:
                                action3 = stops[1]
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = time
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[2]:
                                action3 = stops[2]
                                time = random.choice(range(900, 1800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = time
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[3]:
                                action3 = stops[3]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(900, 3600))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = time
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[4]:
                                action3 = stops[4]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(3600, 10800))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = time
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[5]:
                                action3 = stops[5]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = time
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[6]:
                                action3 = stops[6]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(300, 900))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = time
                                    model = 0
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                            elif action == starts[7]:
                                action3 = stops[7]
                                print(name3 + ' ' + action3)
                                time = random.choice(range(600, 7200))
                                total = num + time
                                if total2 < (7 * 60 * 60 + 45 * 60):
                                    print('!!!continue of a night shift')
                                    total1 = total - (3 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif total2 > (20 * 60 * 60 + 30 * 60):
                                    print('!!!night shift')
                                    total1 = total + (20 * 60 * 60 + 30 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                                elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                    print('!!!day shift')
                                    total1 = total + (7 * 60 * 60 + 45 * 60)
                                    secs = int(total1 % 60)
                                    minutes = int(total1 / 60 % 60)
                                    hours = int(total1 / 3600)
                                    plan = 0
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = time
                                    my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                              break1, material, task, model, secs,
                                                              minutes, hours, day, month, year))
                                    my_db.commit()
                                    name.append(name3)
                                    temp3.remove(name3)
                                    temp1.pop(name3)
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = random.choice(range(11, 24))
                            secs = random.choice(range(0, 60))
                            name2 = word
                            action2 = 'stop'
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) - ((7 * 60 * 60) + (45 * 60))
                            plan = 0
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
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = random.choice(range(25, 38))
                            secs = random.choice(range(0, 60))
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
                            my_cursor.execute(query, (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                      task, model, secs, minutes, hours, day, month, year))
                            my_db.commit()
                        h += 1
                    elif min / 15 == 1 or min / 15 == 2 or min / 15 == 3 or min / 15 == 4:
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = min
                            secs = random.choice(range(0, 60))
                            time = (hours * 60 * 60) + (minutes * 60) + secs
                            name2 = random.choice(name)
                            action2 = 'checkpoint'
                            if time < (7 * 60 * 60) + (45 * 60) + 0:
                                total = ((3 * 60 * 60) + (30 * 60) + 0) + time
                                plan = 0
                                setup = 0
                                auto = 0
                                ppr = 0
                                break1 = 0
                                material = 0
                                task = 0
                                model = 0
                                my_cursor.execute(query,
                                                  (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                   task, model, secs, minutes, hours, day, month, year))
                                my_db.commit()
                            elif (7 * 60 * 60) + (45 * 60) + 0 < time < (20 * 60 * 60) + (30 * 60) + 0:
                                total = time - ((7 * 60 * 60) + (45 * 60) + 0)
                                plan = 0
                                setup = 0
                                auto = 0
                                ppr = 0
                                break1 = 0
                                material = 0
                                task = 0
                                model = 0
                                my_cursor.execute(query,
                                                  (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                   task, model, secs, minutes, hours, day, month, year))
                                my_db.commit()
                            elif time > (20 * 60 * 60) + (30 * 60) + 0:
                                total = time - ((20 * 60 * 60) + (30 * 60) + 0)
                                plan = 0
                                setup = 0
                                auto = 0
                                ppr = 0
                                break1 = 0
                                material = 0
                                task = 0
                                model = 0
                                my_cursor.execute(query,
                                                  (
                                                  name2, action2, total, plan, setup, auto, ppr, break1, material, task,
                                                  model, secs, minutes, hours, day, month, year))
                                my_db.commit()
                    else:
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = random.choice(range(11, 24))
                            secs = random.choice(range(0, 60))
                            name2 = word
                            action2 = 'stop'
                            total = ((hours * 60 * 60) + (minutes * 60) + secs) - ((7 * 60 * 60) + (45 * 60))
                            plan = 0
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
                        for word in name:
                            day = d
                            month = m
                            year = 2020
                            hours = h
                            minutes = random.choice(range(25, 38))
                            secs = random.choice(range(0, 60))
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
                            my_cursor.execute(query, (name2, action2, total, plan, setup, auto, ppr, break1, material,
                                                      task, model, secs, minutes, hours, day, month, year))
                            my_db.commit()
                        h += 1
                else:
                    if random.randint(1, 20) == 1:
                        day = d
                        month = m
                        year = 2020
                        hours = h
                        minutes = min
                        secs = random.choice(range(0, 60))
                        time = (hours * 60 * 60) + (minutes * 60) + secs
                        name2 = random.choice(name)
                        action2 = random.choice(starts)
                        if time < (7 * 60 * 60) + (45 * 60) + 0:
                            total = ((3 * 60 * 60) + (30 * 60) + 0) + time
                            plan = 0
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
                            temp1.update({name2: [action2, total, secs, minutes, hours]})
                            temp3.append(name2)
                            name.remove(name2)
                        elif (7 * 60 * 60) + (45 * 60) + 0 < time < (20 * 60 * 60) + (30 * 60) + 0:
                            total = time - ((7 * 60 * 60) + (45 * 60) + 0)
                            plan = 0
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
                            temp1.update({name2: [action2, total, secs, minutes, hours]})
                            # print('addition: ' + name2 + ' ' + str(total))
                            # print(temp1)
                            temp3.append(name2)
                            name.remove(name2)
                        elif time > (20 * 60 * 60) + (30 * 60) + 0:
                            total = time - ((20 * 60 * 60) + (30 * 60) + 0)
                            plan = 0
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
                            temp1.update({name2: [action2, total, secs, minutes, hours]})
                            # print('addition: ' + name2 + ' ' + str(total))
                            # print(temp1)
                            temp3.append(name2)
                            name.remove(name2)
                        if len(temp3) != 0:
                            for word in temp3:
                                if random.randint(1, 2) == 1:
                                    name3 = word
                                    temporary = temp1.get(name3)
                                    action = temporary[0]
                                    num = temporary[1]
                                    secs = temporary[2]
                                    minutes = temporary[3]
                                    hours = temporary[4]
                                    total2 = hours * 60 * 60 + minutes * 60 + secs
                                    if action == starts[0]:
                                        action3 = stops[0]
                                        time = random.choice(range(300, 1800))
                                        total = num + time
                                        if total2 < (7 * 60 * 60 + 45 * 60):
                                            print('!!!continue of a night shift')
                                            total1 = total - (3 * 60 * 60 + 30 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = time
                                            setup = 0
                                            auto = 0
                                            ppr = 0
                                            break1 = 0
                                            material = 0
                                            task = 0
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                        elif total2 > (20 * 60 * 60 + 30 * 60):
                                            print('!!!night shift')
                                            total1 = total + (20 * 60 * 60 + 30 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = time
                                            setup = 0
                                            auto = 0
                                            ppr = 0
                                            break1 = 0
                                            material = 0
                                            task = 0
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                        elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                            print('!!!day shift')
                                            total1 = total + (7 * 60 * 60 + 45 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = time
                                            setup = 0
                                            auto = 0
                                            ppr = 0
                                            break1 = 0
                                            material = 0
                                            task = 0
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                    elif action == starts[1]:
                                        action3 = stops[1]
                                        time = random.choice(range(300, 900))
                                        total = num + time
                                        if total2 < (7 * 60 * 60 + 45 * 60):
                                            print('!!!continue of a night shift')
                                            total1 = total - (3 * 60 * 60 + 30 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = time
                                            auto = 0
                                            ppr = 0
                                            break1 = 0
                                            material = 0
                                            task = 0
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                        elif total2 > (20 * 60 * 60 + 30 * 60):
                                            print('!!!night shift')
                                            total1 = total + (20 * 60 * 60 + 30 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = time
                                            auto = 0
                                            ppr = 0
                                            break1 = 0
                                            material = 0
                                            task = 0
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                        elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                            print('!!!day shift')
                                            total1 = total + (7 * 60 * 60 + 45 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = time
                                            auto = 0
                                            ppr = 0
                                            break1 = 0
                                            material = 0
                                            task = 0
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                    elif action == starts[2]:
                                        action3 = stops[2]
                                        time = random.choice(range(900, 1800))
                                        total = num + time
                                        if total2 < (7 * 60 * 60 + 45 * 60):
                                            print('!!!continue of a night shift')
                                            total1 = total - (3 * 60 * 60 + 30 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = 0
                                            auto = time
                                            ppr = 0
                                            break1 = 0
                                            material = 0
                                            task = 0
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                        elif total2 > (20 * 60 * 60 + 30 * 60):
                                            print('!!!night shift')
                                            total1 = total + (20 * 60 * 60 + 30 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = 0
                                            auto = time
                                            ppr = 0
                                            break1 = 0
                                            material = 0
                                            task = 0
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                        elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                            print('!!!day shift')
                                            total1 = total + (7 * 60 * 60 + 45 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = 0
                                            auto = time
                                            ppr = 0
                                            break1 = 0
                                            material = 0
                                            task = 0
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                    elif action == starts[3]:
                                        action3 = stops[3]
                                        print(name3 + ' ' + action3)
                                        time = random.choice(range(900, 3600))
                                        total = num + time
                                        if total2 < (7 * 60 * 60 + 45 * 60):
                                            print('!!!continue of a night shift')
                                            total1 = total - (3 * 60 * 60 + 30 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = 0
                                            auto = 0
                                            ppr = time
                                            break1 = 0
                                            material = 0
                                            task = 0
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                        elif total2 > (20 * 60 * 60 + 30 * 60):
                                            print('!!!night shift')
                                            total1 = total + (20 * 60 * 60 + 30 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = 0
                                            auto = 0
                                            ppr = time
                                            break1 = 0
                                            material = 0
                                            task = 0
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                        elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                            print('!!!day shift')
                                            total1 = total + (7 * 60 * 60 + 45 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = 0
                                            auto = 0
                                            ppr = time
                                            break1 = 0
                                            material = 0
                                            task = 0
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                    elif action == starts[4]:
                                        action3 = stops[4]
                                        print(name3 + ' ' + action3)
                                        time = random.choice(range(3600, 10800))
                                        total = num + time
                                        if total2 < (7 * 60 * 60 + 45 * 60):
                                            print('!!!continue of a night shift')
                                            total1 = total - (3 * 60 * 60 + 30 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = 0
                                            auto = 0
                                            ppr = 0
                                            break1 = time
                                            material = 0
                                            task = 0
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                        elif total2 > (20 * 60 * 60 + 30 * 60):
                                            print('!!!night shift')
                                            total1 = total + (20 * 60 * 60 + 30 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = 0
                                            auto = 0
                                            ppr = 0
                                            break1 = time
                                            material = 0
                                            task = 0
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                        elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                            print('!!!day shift')
                                            total1 = total + (7 * 60 * 60 + 45 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = 0
                                            auto = 0
                                            ppr = 0
                                            break1 = time
                                            material = 0
                                            task = 0
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                    elif action == starts[5]:
                                        action3 = stops[5]
                                        print(name3 + ' ' + action3)
                                        time = random.choice(range(300, 900))
                                        total = num + time
                                        if total2 < (7 * 60 * 60 + 45 * 60):
                                            print('!!!continue of a night shift')
                                            total1 = total - (3 * 60 * 60 + 30 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = 0
                                            auto = 0
                                            ppr = 0
                                            break1 = 0
                                            material = time
                                            task = 0
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                        elif total2 > (20 * 60 * 60 + 30 * 60):
                                            print('!!!night shift')
                                            total1 = total + (20 * 60 * 60 + 30 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = 0
                                            auto = 0
                                            ppr = 0
                                            break1 = 0
                                            material = time
                                            task = 0
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                        elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                            print('!!!day shift')
                                            total1 = total + (7 * 60 * 60 + 45 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = 0
                                            auto = 0
                                            ppr = 0
                                            break1 = 0
                                            material = time
                                            task = 0
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                    elif action == starts[6]:
                                        action3 = stops[6]
                                        print(name3 + ' ' + action3)
                                        time = random.choice(range(300, 900))
                                        total = num + time
                                        if total2 < (7 * 60 * 60 + 45 * 60):
                                            print('!!!continue of a night shift')
                                            total1 = total - (3 * 60 * 60 + 30 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = 0
                                            auto = 0
                                            ppr = 0
                                            break1 = 0
                                            material = 0
                                            task = time
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                        elif total2 > (20 * 60 * 60 + 30 * 60):
                                            print('!!!night shift')
                                            total1 = total + (20 * 60 * 60 + 30 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = 0
                                            auto = 0
                                            ppr = 0
                                            break1 = 0
                                            material = 0
                                            task = time
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                        elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                            print('!!!day shift')
                                            total1 = total + (7 * 60 * 60 + 45 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = 0
                                            auto = 0
                                            ppr = 0
                                            break1 = 0
                                            material = 0
                                            task = time
                                            model = 0
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                    elif action == starts[7]:
                                        action3 = stops[7]
                                        print(name3 + ' ' + action3)
                                        time = random.choice(range(600, 7200))
                                        total = num + time
                                        if total2 < (7 * 60 * 60 + 45 * 60):
                                            print('!!!continue of a night shift')
                                            total1 = total - (3 * 60 * 60 + 30 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = 0
                                            auto = 0
                                            ppr = 0
                                            break1 = 0
                                            material = 0
                                            task = 0
                                            model = time
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                        elif total2 > (20 * 60 * 60 + 30 * 60):
                                            print('!!!night shift')
                                            total1 = total + (20 * 60 * 60 + 30 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = 0
                                            auto = 0
                                            ppr = 0
                                            break1 = 0
                                            material = 0
                                            task = 0
                                            model = time
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                        elif (7 * 60 * 60 + 45 * 60) < total2 < (20 * 60 * 60 + 30 * 60):
                                            print('!!!day shift')
                                            total1 = total + (7 * 60 * 60 + 45 * 60)
                                            secs = int(total1 % 60)
                                            minutes = int(total1 / 60 % 60)
                                            hours = int(total1 / 3600)
                                            plan = 0
                                            setup = 0
                                            auto = 0
                                            ppr = 0
                                            break1 = 0
                                            material = 0
                                            task = 0
                                            model = time
                                            my_cursor.execute(query, (name3, action3, total, plan, setup, auto, ppr,
                                                                      break1, material, task, model, secs,
                                                                      minutes, hours, day, month, year))
                                            my_db.commit()
                                            name.append(name3)
                                            temp3.remove(name3)
                                            temp1.pop(name3)
                                else:
                                    pass
