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
temp2 = {}


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
                while h == 7:
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
                while h == 20:
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
                        temp1.update({name2: action2})
                        temp2.update({name2: total})
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
                        temp1.update({name2: action2})
                        temp2.update({name2: total})
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
                        temp1.update({name2: action2})
                        temp2.update({name2: total})
                        name.remove(name2)
                    if len(temp1) != 0:
                        for word in temp1:
                            name3 = word
                            action3 = temp1.get(name3)
                            # if random.randint(1, 2) == 1:
                            if action3 == starts[0]:
                                action4 = stops[0]
                                time = random.choice(range(300, 3600))
                                secs = secs + int(time % 60)
                                minutes = minutes + int(time / 60 % 60)
                                hours = hours + int(time / 3600)
                                if secs >= 60:
                                    minutes = minutes + 1
                                    secs = secs - 60
                                if minutes >= 60:
                                    hours = hours + 1
                                    minutes = minutes - 60
                                num = temp2.get(name3)
                                total = num + time
                                plan = time
                                setup = 0
                                auto = 0
                                ppr = 0
                                break1 = 0
                                material = 0
                                task = 0
                                model = 0
                                my_cursor.execute(query,
                                                  (name3, action4, total, plan, setup, auto, ppr, break1,
                                                   material, task, model, secs, minutes, hours, day, month,
                                                   year))
                                my_db.commit()
                                name.append(name3)
                                del temp1[name2]
                                del temp2[name2]
                            elif action2 == starts[1]:
                                action3 = stops[1]
                                time = random.choice(range(300, 3600))
                                secs += int(time % 60)
                                minutes += int(time / 60 % 60)
                                hours += int(time / 3600)
                                if secs >= 60:
                                    secs -= 60
                                    minutes += 1
                                if minutes >= 60:
                                    minutes -= 60
                                    hours += 1
                                    num = temp2.get(name3)
                                    total = num + time
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (
                                        name3, action3, total, plan, setup, auto, ppr, break1,
                                        material, task, model, secs, minutes, hours, day, month,
                                        year))
                                    my_db.commit()
                                    name.append(name3)
                                    del temp1[name2]
                                    del temp2[name2]
                            elif action2 == starts[2]:
                                action3 = stops[2]
                                time = random.choice(range(300, 3600))
                                secs += int(time % 60)
                                minutes += int(time / 60 % 60)
                                hours += int(time / 3600)
                                if secs >= 60:
                                    secs -= 60
                                    minutes += 1
                                if minutes >= 60:
                                    minutes -= 60
                                    hours += 1
                                    num = temp2.get(name3)
                                    total = num + time
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (
                                        name3, action3, total, plan, setup, auto, ppr, break1,
                                        material, task, model, secs, minutes, hours, day, month,
                                        year))
                                    my_db.commit()
                                    name.append(name3)
                                    del temp1[name2]
                                    del temp2[name2]
                            elif action2 == starts[3]:
                                action3 = stops[3]
                                time = random.choice(range(300, 3600))
                                secs += int(time % 60)
                                minutes += int(time / 60 % 60)
                                hours += int(time / 3600)
                                if secs >= 60:
                                    secs -= 60
                                    minutes += 1
                                if minutes >= 60:
                                    minutes -= 60
                                    hours += 1
                                    num = temp2.get(name3)
                                    total = num + time
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (
                                        name3, action3, total, plan, setup, auto, ppr, break1,
                                        material, task, model, secs, minutes, hours, day, month,
                                        year))
                                    my_db.commit()
                                    name.append(name3)
                                    del temp1[name2]
                                    del temp2[name2]
                            elif action2 == starts[4]:
                                action3 = stops[4]
                                time = random.choice(range(300, 3600))
                                secs += int(time % 60)
                                minutes += int(time / 60 % 60)
                                hours += int(time / 3600)
                                if secs >= 60:
                                    secs -= 60
                                    minutes += 1
                                if minutes >= 60:
                                    minutes -= 60
                                    hours += 1
                                    num = temp2.get(name3)
                                    total = num + time
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (
                                        name3, action3, total, plan, setup, auto, ppr, break1,
                                        material, task, model, secs, minutes, hours, day, month,
                                        year))
                                    my_db.commit()
                                    name.append(name3)
                                    del temp1[name2]
                                    del temp2[name2]
                            elif action2 == starts[5]:
                                action3 = stops[5]
                                time = random.choice(range(300, 3600))
                                secs += int(time % 60)
                                minutes += int(time / 60 % 60)
                                hours += int(time / 3600)
                                if secs >= 60:
                                    secs -= 60
                                    minutes += 1
                                if minutes >= 60:
                                    minutes -= 60
                                    hours += 1
                                    num = temp2.get(name3)
                                    total = num + time
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (
                                        name3, action3, total, plan, setup, auto, ppr, break1,
                                        material, task, model, secs, minutes, hours, day, month,
                                        year))
                                    my_db.commit()
                                    name.append(name3)
                                    del temp1[name2]
                                    del temp2[name2]
                            elif action2 == starts[6]:
                                action3 = stops[6]
                                time = random.choice(range(300, 3600))
                                secs += int(time % 60)
                                minutes += int(time / 60 % 60)
                                hours += int(time / 3600)
                                if secs >= 60:
                                    secs -= 60
                                    minutes += 1
                                if minutes >= 60:
                                    minutes -= 60
                                    hours += 1
                                    num = temp2.get(name3)
                                    total = num + time
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (
                                        name3, action3, total, plan, setup, auto, ppr, break1,
                                        material, task, model, secs, minutes, hours, day, month,
                                        year))
                                    my_db.commit()
                                    name.append(name3)
                                    del temp1[name2]
                                    del temp2[name2]
                            elif action2 == starts[7]:
                                action3 = stops[7]
                                time = random.choice(range(300, 3600))
                                secs += int(time % 60)
                                minutes += int(time / 60 % 60)
                                hours += int(time / 3600)
                                if secs >= 60:
                                    secs -= 60
                                    minutes += 1
                                if minutes >= 60:
                                    minutes -= 60
                                    hours += 1
                                    num = temp2.get(name3)
                                    total = num + time
                                    plan = time
                                    setup = 0
                                    auto = 0
                                    ppr = 0
                                    break1 = 0
                                    material = 0
                                    task = 0
                                    model = 0
                                    my_cursor.execute(query, (
                                        name3, action3, total, plan, setup, auto, ppr, break1,
                                        material, task, model, secs, minutes, hours, day, month,
                                        year))
                                    my_db.commit()
                                    name.append(name3)
                                    del temp1[name2]
                                    del temp2[name2]
