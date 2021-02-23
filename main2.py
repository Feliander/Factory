import sys
import pymysql
from PyQt5 import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib import pyplot as plt
from MyGUI2 import Ui_MainWindow


db = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='mydb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
my_cursor = db.cursor()


query1 = 'SELECT MAX(totaltime), SUM(plantime), SUM(setup), SUM(autoserv), SUM(ppr), SUM(break), SUM(material), ' \
         'SUM(task), SUM(maket) FROM worktime WHERE (name = %s) AND (year = (%s)) AND (month = (%s)) AND (day = (%s)) '\
         'AND (hours BETWEEN (%s) AND (%s))'

query2 = 'SELECT MAX(totaltime), SUM(plantime), SUM(setup), SUM(autoserv), SUM(ppr), SUM(break), SUM(material), ' \
         'SUM(task), SUM(maket) FROM worktime WHERE (name = %s) AND (year = (%s)) AND (month = (%s)) ' \
         'AND (day = (%s)) AND (hours = (%s)) AND (minutes BETWEEN (%s) AND (%s))'

query3 = 'SELECT MAX(totaltime), SUM(plantime), SUM(setup), SUM(autoserv), SUM(ppr), SUM(break), SUM(material), ' \
         'SUM(task), SUM(maket) FROM worktime WHERE (name = %s) AND (year = (%s)) AND (month = (%s)) AND ' \
         '(day BETWEEN (%s) AND (%s))'

query4 = 'SELECT MAX(totaltime), SUM(plantime), SUM(setup), SUM(autoserv), SUM(ppr), SUM(break), SUM(material), ' \
         'SUM(task), SUM(maket) FROM worktime WHERE (name = %s) AND (year = (%s)) AND (month between (%s) and (%s))'

eng_name = 'Laser1'


class MyMplCanvas(FigureCanvasQTAgg):
    def __init__(self, fig):
        FigureCanvasQTAgg.__init__(self, fig)


def prepare_canvas(gra, layout=None):
    fig, axes = gra
    canvas = MyMplCanvas(fig)
    layout.addWidget(canvas)
    return canvas


def sql4(query, val1, val2, val3, val4):
    my_cursor.execute(query, (val1, val2, val3, val4))


def sql5(query, val1, val2, val3, val4, val5):
    my_cursor.execute(query, (val1, val2, val3, val4, val5))


def sql6(query, val1, val2, val3, val4, val5, val6):
    my_cursor.execute(query, (val1, val2, val3, val4, val5, val6))


def sql7(query, val1, val2, val3, val4, val5, val6, val7):
    my_cursor.execute(query, (val1, val2, val3, val4, val5, val6, val7))


def tot(sql):
    result = my_cursor.fetchall()
    my_result = (result[0])
    total1 = my_result.get('MAX(totaltime)')
    return total1


def pln(sql):
    result = my_cursor.fetchall()
    my_result = (result[0])
    plan = my_result.get('SUM(plantime)')
    return plan


def stp(sql):
    result = my_cursor.fetchall()
    my_result = (result[0])
    setup = my_result.get('SUM(setup)')
    return setup


def asv(sql):
    result = my_cursor.fetchall()
    my_result = (result[0])
    auto = my_result.get('SUM(autoserv)')
    return auto


def ppr(sql):
    result = my_cursor.fetchall()
    my_result = (result[0])
    ppr1 = my_result.get('SUM(ppr)')
    return ppr1


def brk(sql):
    result = my_cursor.fetchall()
    my_result = (result[0])
    break1 = my_result.get('SUM(break)')
    return break1


def mat(sql):
    result = my_cursor.fetchall()
    my_result = (result[0])
    material = my_result.get('SUM(material)')
    return material


def tsk(sql):
    result = my_cursor.fetchall()
    my_result = (result[0])
    task = my_result.get('SUM(task)')
    return task


def mkt(sql):
    result = my_cursor.fetchall()
    my_result = (result[0])
    model = my_result.get('SUM(maket)')
    return model


def graph(name, totall, plan, setup, autoserv, ppr, br, material, task, maket):
    pieces = (totall, plan, setup, autoserv, ppr, br, material, task, maket)
    cols = ('#87E65C', '#ff5500', '#5500ff', '#ff00ff', '#aa0000', '#848400', '#309090', '#6d6da3', '#0000ff')
    fig, axes = plt.subplots()
    owners = ['Работа', 'Плановый перерыв', 'Переналадка/Перенастройка',
              'Автономное обслуживание', 'ППР', 'Поломка оборудования', 'Отсутствие материалов',
              'Отсутствие задания', 'Изготовление макетов']
    axes.pie(pieces, colors=cols, wedgeprops={'lw': 0.5, 'ls': '-', 'edgecolor': "k"}, )
    plt.legend(owners, loc='best', bbox_to_anchor=(0, 1), title='Легенда')
    axes.set_title(name)
    return fig, axes


class Main_Class(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.comboBox.activated[str].connect(self.act)
        self.composition = QtWidgets.QVBoxLayout(self.widget_2)
        self.canvas = prepare_canvas(graph('Графика нет, выберите дату', 10, 10, 10, 10, 10, 10, 10, 10, 10),
                                     layout=self.composition)
        self.prepare_label('Графика нет, выберите дату')
        self.pushButton.clicked.connect(self.push)
        self.pushButton.setText('Найти')
        self.label_22.setText('Поиск:')
        self.label_22.setAlignment(QtCore.Qt.AlignRight)
        self.label_23.setAlignment(QtCore.Qt.AlignRight)
        self.label_24.setAlignment(QtCore.Qt.AlignRight)
        self.label.setAlignment(QtCore.Qt.AlignRight)
        self.label_1.setAlignment(QtCore.Qt.AlignLeft)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(2020, 1, 1, 0, 0, 0))
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.dateTimeEdit_2.setDateTime(QtCore.QDateTime(2020, 1, 2, 0, 0, 0))

    def prepare_label(self, txt, total_1=100, plan=10, setup=10, auto_serv=10, ppr1=10, br=10, material=10, task=10,
                      model=10):
        total = total_1 - plan - setup - auto_serv - ppr1 - br - material - task - model
        self.label_3.setText(txt + ':')
        self.label_1.setText("%02d ч %02d м %02d с " %
                             (total_1 / 3600, (total_1 / 60) % 60, total_1 % 60))
        self.label_2.setText('Работа:')
        self.label_5.setText("%02d ч %02d м %02d с " %
                             (total / 3600, (total / 60) % 60, total % 60))
        self.label_6.setText('Плановый перерыв:')
        self.label_14.setText("%02d ч %02d м %02d с " %
                              (plan / 3600, (plan / 60) % 60, plan % 60))
        self.label_7.setText('Переналадка/перенастройка:')
        self.label_15.setText("%02d ч %02d м %02d с " %
                              (setup / 3600, (setup / 60) % 60, setup % 60))
        self.label_8.setText('Автономное обслуживание:')
        self.label_16.setText("%02d ч %02d м %02d с " %
                              (auto_serv / 3600, (auto_serv / 60) % 60, auto_serv % 60))
        self.label_9.setText('ППР:')
        self.label_17.setText("%02d ч %02d м %02d с " %
                              (ppr1 / 3600, (ppr1 / 60) % 60, ppr1 % 60))
        self.label_10.setText('Поломка оборудования:')
        self.label_18.setText("%02d ч %02d м %02d с " %
                              (br / 3600, (br / 60) % 60, br % 60))
        self.label_11.setText('Отсутствие материалов:')
        self.label_19.setText("%02d ч %02d м %02d с " %
                              (material / 3600, (material / 60) % 60, material % 60))
        self.label_12.setText('Отсутствие задания:')
        self.label_20.setText("%02d ч %02d м %02d с " %
                              (task / 3600, (task / 60) % 60, task % 60))
        self.label_13.setText('Изготовление макетов:')
        self.label_21.setText("%02d ч %02d м %02d с " %
                              (model / 3600, (model / 60) % 60, model % 60))

    def update(self):
        self.composition.removeWidget(self.canvas)
        self.canvas.deleteLater()
        self.canvas = None

    def zero(self):
        self.canvas = prepare_canvas(graph('Графика нет, выберите дату', 10, 10, 10, 10, 10, 10, 10, 10, 10),
                                     layout=self.composition)
        self.prepare_label('Графика нет, выберите дату')
        QtWidgets.QMessageBox.information(None, 'Ошибка', 'Информации за данный промежуток не существует.\n\n'
                                                          'На данный момент есть записи только за 2020 год.\n\n'
                                                          'Никаких данных отображено не будет.')

    def zero2(self):
        self.canvas = prepare_canvas(
            graph('Графика нет, выберите дату', 10, 10, 10, 10, 10, 10, 10, 10, 10),
            layout=self.composition)
        self.prepare_label('Графика нет, выберите дату')
        QtWidgets.QMessageBox.information(None, 'Ошибка',
                                          'Время начала отсчёта должно быть меньше времени конца '
                                          'отсчёта!\n\n'
                                          'Никаких данных отображено не будет.')

    @staticmethod
    def act(text):
        global eng_name
        if text == 'Лазер №1':
            eng_name = 'Laser1'
        elif text == 'Лазер №2':
            eng_name = 'Laser2'
        elif text == 'Пробивка №1':
            eng_name = 'Punch1'
        elif text == 'Пробивка №2':
            eng_name = 'Punch2'
        elif text == 'Гибка №1':
            eng_name = 'Bend1'
        elif text == 'Гибка №2':
            eng_name = 'Bend2'
        elif text == 'Сварка №1':
            eng_name = 'Weld1'
        elif text == 'Сварка №2':
            eng_name = 'Weld2'
        elif text == 'Сварочный робот №1':
            eng_name = 'Weld_Robot1'
        elif text == 'Сварочный робот №2':
            eng_name = 'Weld_Robot2'
        elif text == 'Сборка №1':
            eng_name = 'Assembly1'
        elif text == 'Сборка №2':
            eng_name = 'Assembly2'
        elif text == 'Зачистка №1':
            eng_name = 'Cleaning1'
        elif text == 'Зачистка №2':
            eng_name = 'Cleaning2'

    @staticmethod
    def text(text):
        if text == 'Laser1':
            txt = 'Лазер №1'
            return txt
        elif text == 'Laser2':
            txt = 'Лазер №2'
            return txt
        elif text == 'Punch1':
            txt = 'Пробивка №1'
            return txt
        elif text == 'Punch2':
            txt = 'Пробивка №2'
            return txt
        elif text == 'Bend1':
            txt = 'Гибка №1'
            return txt
        elif text == 'Bend2':
            txt = 'Гибка №2'
            return txt
        elif text == 'Weld1':
            txt = 'Сварка №1'
            return txt
        elif text == 'Weld2':
            txt = 'Сварка №2'
            return txt
        elif text == 'Weld_Robot1':
            txt = 'Сварочный робот №1'
            return txt
        elif text == 'Weld_Robot2':
            txt = 'Сварочный робот №2'
            return txt
        elif text == 'Assembly1':
            txt = 'Сборка №1'
            return txt
        elif text == 'Assembly2':
            txt = 'Сборка №2'
            return txt
        elif text == 'Cleaning1':
            txt = 'Зачистка №1'
            return txt
        elif text == 'Cleaning2':
            txt = 'Зачистка №2'
            return txt

    def get(self, txt, text):
        if self.year() == self.year2():
            if self.month() == self.month2():
                if self.day() == self.day2():
                    if self.hour() == self.hour2():
                        if self.min() <= self.min2():
                            t = self.get_total(txt, self.hour(), self.hour2(), self.min(), self.min2())
                            p = pln(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(),
                                         self.min2()))
                            s = stp(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(),
                                         self.min2()))
                            a = asv(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(),
                                         self.min2()))
                            r = ppr(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(),
                                         self.min2()))
                            b = brk(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(),
                                         self.min2()))
                            m = mat(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(),
                                         self.min2()))
                            k = tsk(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(),
                                         self.min2()))
                            d = mkt(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(),
                                         self.min2()))
                            self.canvas = prepare_canvas(graph(text, self.check(t),
                                                               self.check(p), self.check(s), self.check(a),
                                                               self.check(r), self.check(b), self.check(m),
                                                               self.check(k), self.check(d)), layout=self.composition)
                            self.prepare_label(text, self.check(t),
                                               self.check(p),
                                               self.check(s), self.check(a), self.check(r), self.check(b),
                                               self.check(m), self.check(k), self.check(d))
                        else:
                            self.zero2()
                    elif self.hour() <= self.hour2():
                        t = self.get_total(txt, self.hour(), self.hour2(), self.min(), self.min2())
                        p1 = pln(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 60))
                        p2 = pln(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1,
                                      self.hour2() - 1))
                        p3 = pln(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour2(), 0, self.min2()))
                        p = self.check(p1) + self.check(p2) + self.check(p3)
                        s1 = stp(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 60))
                        s2 = stp(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1,
                                      self.hour2() - 1))
                        s3 = stp(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour2(), 0, self.min2()))
                        s = self.check(s1) + self.check(s2) + self.check(s3)
                        a1 = asv(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 60))
                        a2 = asv(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1,
                                      self.hour2() - 1))
                        a3 = asv(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour2(), 0, self.min2()))
                        a = self.check(a1) + self.check(a2) + self.check(a3)
                        r1 = ppr(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 60))
                        r2 = ppr(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1,
                                      self.hour2() - 1))
                        r3 = ppr(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour2(), 0, self.min2()))
                        r = self.check(r1) + self.check(r2) + self.check(r3)
                        b1 = brk(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 60))
                        b2 = brk(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1,
                                      self.hour2() - 1))
                        b3 = brk(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour2(), 0, self.min2()))
                        b = self.check(b1) + self.check(b2) + self.check(b3)
                        m1 = mat(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 60))
                        m2 = mat(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1,
                                      self.hour2() - 1))
                        m3 = mat(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour2(), 0, self.min2()))
                        m = self.check(m1) + self.check(m2) + self.check(m3)
                        k1 = tsk(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 60))
                        k2 = tsk(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1,
                                      self.hour2() - 1))
                        k3 = tsk(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour2(), 0, self.min2()))
                        k = self.check(k1) + self.check(k2) + self.check(k3)
                        d1 = mkt(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 60))
                        d2 = mkt(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1,
                                      self.hour2() - 1))
                        d3 = mkt(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour2(), 0, self.min2()))
                        d = self.check(d1) + self.check(d2) + self.check(d3)
                        self.canvas = prepare_canvas(graph(text, t, p, s, a, r, b, m, k, d), layout=self.composition)
                        self.prepare_label(text, t, p, s, a, r, b, m, k, d)
                    else:
                        self.zero2()
                elif self.day() <= self.day2():
                    t = self.get_total_2(txt, self.day(), self.day2(), self.hour(), self.hour2(), self.min(),
                                         self.min2())
                    p1 = pln(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 60))
                    p2 = pln(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1, 23))
                    p3 = pln(sql6(query1, txt, self.year(), self.month(), self.day2(), 0, self.hour2() - 1))
                    p4 = pln(sql7(query2, txt, self.year(), self.month(), self.day2(), self.hour2(), 0, self.min2()))
                    p = self.check(p1) + self.check(p2) + self.check(p3) + self.check(p4)
                    if self.day2() - self.day() != 1:
                        p5 = pln(sql5(query3, txt, self.year(), self.month(), self.day() + 1, self.day2() - 1))
                        p = self.check(p1) + self.check(p2) + self.check(p3) + self.check(p4) + self.check(p5)
                    s1 = stp(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 60))
                    s2 = stp(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1, 24))
                    s3 = stp(sql6(query1, txt, self.year(), self.month(), self.day2(), 0, self.hour2() - 1))
                    s4 = stp(sql7(query2, txt, self.year(), self.month(), self.day2(), self.hour2(), 0, self.min2()))
                    s = self.check(s1) + self.check(s2) + self.check(s3) + self.check(s4)
                    if self.day2() - self.day() != 1:
                        s5 = stp(sql5(query3, txt, self.year(), self.month(), self.day() + 1, self.day2() - 1))
                        s = self.check(s1) + self.check(s2) + self.check(s3) + self.check(s4) + self.check(s5)
                    a1 = asv(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 60))
                    a2 = asv(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1, 24))
                    a3 = asv(sql6(query1, txt, self.year(), self.month(), self.day2(), 0, self.hour2() - 1))
                    a4 = asv(sql7(query2, txt, self.year(), self.month(), self.day2(), self.hour2(), 0, self.min2()))
                    a = self.check(a1) + self.check(a2) + self.check(a3) + self.check(a4)
                    if self.day2() - self.day() != 1:
                        a5 = asv(sql5(query3, txt, self.year(), self.month(), self.day() + 1, self.day2() - 1))
                        a = self.check(a1) + self.check(a2) + self.check(a3) + self.check(a4) + self.check(a5)
                    r1 = ppr(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 60))
                    r2 = ppr(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1, 24))
                    r3 = ppr(sql6(query1, txt, self.year(), self.month(), self.day2(), 0, self.hour2() - 1))
                    r4 = ppr(sql7(query2, txt, self.year(), self.month(), self.day2(), self.hour2(), 0, self.min2()))
                    r = self.check(r1) + self.check(r2) + self.check(r3) + self.check(r4)
                    if self.day2() - self.day() != 1:
                        r5 = ppr(sql5(query3, txt, self.year(), self.month(), self.day() + 1, self.day2() - 1))
                        r = self.check(r1) + self.check(r2) + self.check(r3) + self.check(r4) + self.check(r5)
                    b1 = brk(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 60))
                    b2 = brk(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1, 24))
                    b3 = brk(sql6(query1, txt, self.year(), self.month(), self.day2(), 0, self.hour2() - 1))
                    b4 = brk(sql7(query2, txt, self.year(), self.month(), self.day2(), self.hour2(), 0, self.min2()))
                    b = self.check(b1) + self.check(b2) + self.check(b3) + self.check(b4)
                    if self.day2() - self.day() != 1:
                        b5 = brk(sql5(query3, txt, self.year(), self.month(), self.day() + 1, self.day2() - 1))
                        b = self.check(b1) + self.check(b2) + self.check(b3) + self.check(b4) + self.check(b5)
                    m1 = mat(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 60))
                    m2 = mat(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1, 24))
                    m3 = mat(sql6(query1, txt, self.year(), self.month(), self.day2(), 0, self.hour2() - 1))
                    m4 = mat(sql7(query2, txt, self.year(), self.month(), self.day2(), self.hour2(), 0, self.min2()))
                    m = self.check(m1) + self.check(m2) + self.check(m3) + self.check(m4)
                    if self.day2() - self.day() != 1:
                        m5 = mat(sql5(query3, txt, self.year(), self.month(), self.day() + 1, self.day2() - 1))
                        m = self.check(m1) + self.check(m2) + self.check(m3) + self.check(m4) + self.check(m5)
                    k1 = tsk(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 60))
                    k2 = tsk(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1, 24))
                    k3 = tsk(sql6(query1, txt, self.year(), self.month(), self.day2(), 0, self.hour2() - 1))
                    k4 = tsk(sql7(query2, txt, self.year(), self.month(), self.day2(), self.hour2(), 0, self.min2()))
                    k = self.check(k1) + self.check(k2) + self.check(k3) + self.check(k4)
                    if self.day2() - self.day() != 1:
                        k5 = tsk(sql5(query3, txt, self.year(), self.month(), self.day() + 1, self.day2() - 1))
                        k = self.check(k1) + self.check(k2) + self.check(k3) + self.check(k4) + self.check(k5)
                    d1 = mkt(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 60))
                    d2 = mkt(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1, 24))
                    d3 = mkt(sql6(query1, txt, self.year(), self.month(), self.day2(), 0, self.hour2() - 1))
                    d4 = mkt(sql7(query2, txt, self.year(), self.month(), self.day2(), self.hour2(), 0, self.min2()))
                    d = self.check(d1) + self.check(d2) + self.check(d3) + self.check(d4)
                    if self.day2() - self.day() != 1:
                        d5 = mkt(sql5(query3, txt, self.year(), self.month(), self.day() + 1, self.day2() - 1))
                        d = self.check(d1) + self.check(d2) + self.check(d3) + self.check(d4) + self.check(d5)
                    self.canvas = prepare_canvas(graph(text, t, p, s, a, r, b, m, k, d),
                                                 layout=self.composition)
                    self.prepare_label(text, t, p, s, a, r, b, m, k, d)
                else:
                    self.zero2()
            elif self.month() <= self.month2():
                t = self.get_total_3(txt, self.month(), self.month2(), self.day(), self.day2(), self.hour(),
                                     self.hour2(), self.min(), self.min2())
                p1 = pln(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 59))
                p2 = pln(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1, 23))
                p3 = pln(sql5(query3, txt, self.year(), self.month(), self.day() + 1, self.days(self.month())))
                p4 = pln(sql5(query3, txt, self.year(), self.month2(), 1, self.day2() - 1))
                p5 = pln(sql6(query1, txt, self.year(), self.month2(), self.day2(), 1, self.hour2() - 1))
                p6 = pln(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), 0, self.min2()))
                p = self.check(p1) + self.check(p2) + self.check(p3) + self.check(p4) + self.check(p5) + self.check(p6)
                if self.month2() - self.month() != 1:
                    p7 = pln(sql4(query4, txt, self.year(), self.month() + 1, self.month2() - 1))
                    p += self.check(p7)
                s1 = stp(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 59))
                s2 = stp(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1, 23))
                s3 = stp(sql5(query3, txt, self.year(), self.month(), self.day() + 1, self.days(self.month())))
                s4 = stp(sql5(query3, txt, self.year(), self.month2(), 1, self.day2() - 1))
                s5 = stp(sql6(query1, txt, self.year(), self.month2(), self.day2(), 1, self.hour2() - 1))
                s6 = stp(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), 0, self.min2()))
                s = self.check(s1) + self.check(s2) + self.check(s3) + self.check(s4) + self.check(s5) + self.check(s6)
                if self.month2() - self.month() != 1:
                    s7 = stp(sql4(query4, txt, self.year(), self.month() + 1, self.month2() - 1))
                    s += self.check(s7)
                a1 = asv(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 59))
                a2 = asv(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1, 23))
                a3 = asv(sql5(query3, txt, self.year(), self.month(), self.day() + 1, self.days(self.month())))
                a4 = asv(sql5(query3, txt, self.year(), self.month2(), 1, self.day2() - 1))
                a5 = asv(sql6(query1, txt, self.year(), self.month2(), self.day2(), 1, self.hour2() - 1))
                a6 = asv(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), 0, self.min2()))
                a = self.check(a1) + self.check(a2) + self.check(a3) + self.check(a4) + self.check(a5) + self.check(a6)
                if self.month2() - self.month() != 1:
                    a7 = asv(sql4(query4, txt, self.year(), self.month() + 1, self.month2() - 1))
                    a += self.check(a7)
                r1 = ppr(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 59))
                r2 = ppr(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1, 23))
                r3 = ppr(sql5(query3, txt, self.year(), self.month(), self.day() + 1, self.days(self.month())))
                r4 = ppr(sql5(query3, txt, self.year(), self.month2(), 1, self.day2() - 1))
                r5 = ppr(sql6(query1, txt, self.year(), self.month2(), self.day2(), 1, self.hour2() - 1))
                r6 = ppr(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), 0, self.min2()))
                r = self.check(r1) + self.check(r2) + self.check(r3) + self.check(r4) + self.check(r5) + self.check(r6)
                if self.month2() - self.month() != 1:
                    r7 = ppr(sql4(query4, txt, self.year(), self.month() + 1, self.month2() - 1))
                    r += self.check(r7)
                b1 = brk(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 59))
                b2 = brk(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1, 23))
                b3 = brk(sql5(query3, txt, self.year(), self.month(), self.day() + 1, self.days(self.month())))
                b4 = brk(sql5(query3, txt, self.year(), self.month2(), 1, self.day2() - 1))
                b5 = brk(sql6(query1, txt, self.year(), self.month2(), self.day2(), 1, self.hour2() - 1))
                b6 = brk(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), 0, self.min2()))
                b = self.check(b1) + self.check(b2) + self.check(b3) + self.check(b4) + self.check(b5) + self.check(b6)
                if self.month2() - self.month() != 1:
                    b7 = brk(sql4(query4, txt, self.year(), self.month() + 1, self.month2() - 1))
                    b += self.check(b7)
                m1 = mat(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 59))
                m2 = mat(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1, 23))
                m3 = mat(sql5(query3, txt, self.year(), self.month(), self.day() + 1, self.days(self.month())))
                m4 = mat(sql5(query3, txt, self.year(), self.month2(), 1, self.day2() - 1))
                m5 = mat(sql6(query1, txt, self.year(), self.month2(), self.day2(), 1, self.hour2() - 1))
                m6 = mat(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), 0, self.min2()))
                m = self.check(m1) + self.check(m2) + self.check(m3) + self.check(m4) + self.check(m5) + self.check(m6)
                if self.month2() - self.month() != 1:
                    m7 = mat(sql4(query4, txt, self.year(), self.month() + 1, self.month2() - 1))
                    m += self.check(m7)
                k1 = tsk(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 59))
                k2 = tsk(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1, 23))
                k3 = tsk(sql5(query3, txt, self.year(), self.month(), self.day() + 1, self.days(self.month())))
                k4 = tsk(sql5(query3, txt, self.year(), self.month2(), 1, self.day2() - 1))
                k5 = tsk(sql6(query1, txt, self.year(), self.month2(), self.day2(), 1, self.hour2() - 1))
                k6 = tsk(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), 0, self.min2()))
                k = self.check(k1) + self.check(k2) + self.check(k3) + self.check(k4) + self.check(k5) + self.check(k6)
                if self.month2() - self.month() != 1:
                    k7 = tsk(sql4(query4, txt, self.year(), self.month() + 1, self.month2() - 1))
                    k += self.check(k7)
                d1 = mkt(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 59))
                d2 = mkt(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1, 23))
                d3 = mkt(sql5(query3, txt, self.year(), self.month(), self.day() + 1, self.days(self.month())))
                d4 = mkt(sql5(query3, txt, self.year(), self.month2(), 1, self.day2() - 1))
                d5 = mkt(sql6(query1, txt, self.year(), self.month2(), self.day2(), 1, self.hour2() - 1))
                d6 = mkt(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), 0, self.min2()))
                d = self.check(d1) + self.check(d2) + self.check(d3) + self.check(d4) + self.check(d5) + self.check(d6)
                if self.month2() - self.month() != 1:
                    d7 = mkt(sql4(query4, txt, self.year(), self.month() + 1, self.month2() - 1))
                    d += self.check(d7)
                self.canvas = prepare_canvas(graph(text, t, p, s, a, r, b, m, k, d), layout=self.composition)
                self.prepare_label(text, t, p, s, a, r, b, m, k, d)

            else:
                self.zero2()
        elif self.year() <= self.year2():
            self.zero()
        else:
            self.zero2()

    @staticmethod
    def check(val):
        if val is None:
            val = 0
        return val

    @staticmethod
    def days(val):
        if val == 1 or val == 3 or val == 5 or val == 7 or val == 8 or val == 10 or val == 12:
            d = 31
            return d
        elif val == 2:
            d = 29
            return d
        else:
            d = 30
            return d

    def get_total(self, txt, h1, h2, m1, m2):
        if h1*60*60+m1*60 <= 27900 and h2*60*60+m2*60 <= 27900:
            t1 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), h1, 0, m1)) - 12600
            t2 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), h2, 0, m2)) - 12600
            t = self.check(t2) - self.check(t1)
            return t
        elif h1*60*60+m1*60 <= 27900 <= h2*60*60+m2*60 <= 73800:
            t1 = tot(sql6(query1, txt, self.year(), self.month(), self.day(), h1, 8))
            t2 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), h1, 0, m1))
            t3 = self.check(t1) - self.check(t2)
            if h2 == 7:
                t4 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), h2, 45, m2))
                t4 = self.check(t4)
            else:
                t4 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), h2, 0, m2))
            t = self.check(t3) + self.check(t4)
            return t
        elif h1*60*60+m1*60 <= 27900 and 73800 <= h2*60*60+m2*60 <= 86400:
            t1 = tot(sql6(query1, txt, self.year(), self.month(), self.day(), h1, 8))
            t2 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), h1, 0, m1))
            t3 = self.check(t1) - self.check(t2)
            t4 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), 20, 0, 30))
            if h2 == 20:
                t5 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), h2, 30, m2))
                t5 = self.check(t5)
            else:
                t5 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), h2, 0, m2))
                t5 = self.check(t5)
            t = self.check(t3) + self.check(t4) + self.check(t5)
            return t
        elif 27900 <= h1*60*60+m1*60 <= 73800 and 27900 <= h2*60*60+m2*60 <= 73800:
            if h1 == 7:
                t1 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), h1, 45, m1))
                t1 = self.check(t1)
            else:
                t1 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), h1, 0, m1))
                t1 = self.check(t1)
            t2 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), h2, 0, m2))
            t = self.check(t2) - self.check(t1)
            return t
        elif 27900 <= h1*60*60+m1*60 <= 73800 <= h2*60*60+m2*60 <= 86400:
            t1 = tot(sql6(query1, txt, self.year(), self.month(), self.day(), h1, 21))
            if h1 == 7:
                t2 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), h1, 45, m1))
                t2 = self.check(t2)
            else:
                t2 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), h1, 0, m1))
            t3 = self.check(t1) - self.check(t2)
            if h2 == 20:
                t4 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), h2, 30, m2))
                t4 = self.check(t4)
            else:
                t4 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), h2, 0, m2))
                t4 = self.check(t4)
            t = self.check(t3) + self.check(t4)
            return t
        elif 73800 <= h1*60*60+m1*60 <= 86400 and 73800 <= h2*60*60+m2*60 <= 86400:
            if h1 == 20:
                t1 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), h1, 30, m1))
                t1 = self.check(t1)
            else:
                t1 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), h1, 0, m1))
            t2 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), h2, 0, m2))
            t = self.check(t2) - self.check(t1)
            return t

    def get_total_2(self, txt, d1, d2, h1, h2, m1, m2):
        if h1 * 60 * 60 + m1 * 60 <= 27900 and h2 * 60 * 60 + m2 * 60 <= 27900:
            t1 = tot(sql7(query2, txt, self.year(), self.month(), d1, 7, 0, 45)) - 12600
            t2 = tot(sql7(query2, txt, self.year(), self.month(), d1, h1, 0, m1)) - 12600
            t3 = self.check(t1) - self.check(t2)
            t4 = tot(sql7(query2, txt, self.year(), self.month(), d1, 20, 0, 30))
            t5 = tot(sql7(query2, txt, self.year(), self.month(), d1, 23, 0, 59))
            t6 = tot(sql7(query2, txt, self.year(), self.month(), d2, h2, 0, m2)) - 12600
            t = self.check(t3) + self.check(t4) + self.check(t5) + self.check(t6)
            if d2 - d1 != 1:
                t10 = 0
                d3 = d2 - d1
                for i in range(d3):
                    i += d1
                    if i == d1:
                        pass
                    else:
                        t7 = tot(sql7(query2, txt, self.year(), self.month(), i, 7, 0, 45)) - 12600
                        t8 = tot(sql7(query2, txt, self.year(), self.month(), i, 20, 0, 30))
                        t9 = tot(sql7(query2, txt, self.year(), self.month(), i, 23, 0, 59))
                        t10 += self.check(t7) + self.check(t8) + self.check(t9)
                t += t10
            return t
        elif h1 * 60 * 60 + m1 * 60 <= 27900 <= h2 * 60 * 60 + m2 * 60 <= 73800:
            t1 = tot(sql7(query2, txt, self.year(), self.month(), d1, 7, 0, 45)) - 12600
            t2 = tot(sql7(query2, txt, self.year(), self.month(), d1, h1, 0, m1)) - 12600
            t3 = self.check(t1) - self.check(t2)
            t4 = tot(sql7(query2, txt, self.year(), self.month(), d1, 20, 0, 30))
            t5 = tot(sql7(query2, txt, self.year(), self.month(), d1, 23, 0, 59))
            t6 = tot(sql7(query2, txt, self.year(), self.month(), d2, 7, 0, 45)) - 12600
            t7 = tot(sql7(query2, txt, self.year(), self.month(), d2, h2, 0, m2))
            t = self.check(t3) + self.check(t4) + self.check(t5) + self.check(t6) + self.check(t7)
            if d2 - d1 != 1:
                t10 = 0
                d3 = d2 - d1
                for i in range(d3):
                    i += d1
                    if i == d1:
                        pass
                    else:
                        t7 = tot(sql7(query2, txt, self.year(), self.month(), i, 7, 0, 45)) - 12600
                        t8 = tot(sql7(query2, txt, self.year(), self.month(), i, 20, 0, 30))
                        t9 = tot(sql7(query2, txt, self.year(), self.month(), i, 23, 0, 59))
                        t10 += self.check(t7) + self.check(t8) + self.check(t9)
                t += t10
            return t
        elif h1 * 60 * 60 + m1 * 60 <= 27900 and 73800 <= h2 * 60 * 60 + m2 * 60 <= 86400:
            t1 = tot(sql7(query2, txt, self.year(), self.month(), d1, 7, 0, 45)) - 12600
            t2 = tot(sql7(query2, txt, self.year(), self.month(), d1, h1, 0, m1)) - 12600
            t3 = self.check(t1) - self.check(t2)
            t4 = tot(sql7(query2, txt, self.year(), self.month(), d1, 20, 0, 30))
            t5 = tot(sql7(query2, txt, self.year(), self.month(), d1, 23, 0, 59))
            t6 = tot(sql7(query2, txt, self.year(), self.month(), d2, 7, 0, 45)) - 12600
            t7 = tot(sql7(query2, txt, self.year(), self.month(), d2, 20, 0, 30))
            t8 = tot(sql7(query2, txt, self.year(), self.month(), d2, h2, 0, m2))
            t = self.check(t3) + self.check(t4) + self.check(t5) + self.check(t6) + self.check(t7) + self.check(t8)
            if d2 - d1 != 1:
                t10 = 0
                d3 = d2 - d1
                for i in range(d3):
                    i += d1
                    if i == d1:
                        pass
                    else:
                        t7 = tot(sql7(query2, txt, self.year(), self.month(), i, 7, 0, 45)) - 12600
                        t8 = tot(sql7(query2, txt, self.year(), self.month(), i, 20, 0, 30))
                        t9 = tot(sql7(query2, txt, self.year(), self.month(), i, 23, 0, 59))
                        t10 += self.check(t7) + self.check(t8) + self.check(t9)
                t += t10
            return t
        elif 73800 >= h1 * 60 * 60 + m1 * 60 >= 27900 >= h2 * 60 * 60 + m2 * 60:
            t1 = tot(sql7(query2, txt, self.year(), self.month(), d1, 20, 0, 30))
            t2 = tot(sql7(query2, txt, self.year(), self.month(), d1, h1, 0, m1))
            t3 = self.check(t1) - self.check(t2)
            t4 = tot(sql7(query2, txt, self.year(), self.month(), d1, 23, 0, 59))
            t5 = tot(sql7(query2, txt, self.year(), self.month(), d2, h2, 0, m2)) - 12600
            t = self.check(t3) + self.check(t4) + self.check(t5)
            if d2 - d1 != 1:
                t10 = 0
                d3 = d2 - d1
                for i in range(d3):
                    i += d1
                    if i == d1:
                        pass
                    else:
                        t7 = tot(sql7(query2, txt, self.year(), self.month(), i, 7, 0, 45)) - 12600
                        t8 = tot(sql7(query2, txt, self.year(), self.month(), i, 20, 0, 30))
                        t9 = tot(sql7(query2, txt, self.year(), self.month(), i, 23, 0, 59))
                        t10 += self.check(t7) + self.check(t8) + self.check(t9)
                t += t10
            return t
        elif 27900 <= h1 * 60 * 60 + m1 * 60 <= 73800 and 27900 <= h2 * 60 * 60 + m2 * 60 <= 73800:
            t1 = tot(sql7(query2, txt, self.year(), self.month(), d1, 20, 0, 30))
            t2 = tot(sql7(query2, txt, self.year(), self.month(), d1, h1, 0, m1))
            t3 = self.check(t1) - self.check(t2)
            t4 = tot(sql7(query2, txt, self.year(), self.month(), d1, 23, 0, 59))
            t5 = tot(sql7(query2, txt, self.year(), self.month(), d2, 7, 0, 45)) - 12600
            t6 = tot(sql7(query2, txt, self.year(), self.month(), d2, h2, 0, m2))
            t = self.check(t3) + self.check(t4) + self.check(t5) + self.check(t6)
            if d2 - d1 != 1:
                t10 = 0
                d3 = d2 - d1
                for i in range(d3):
                    i += d1
                    if i == d1:
                        pass
                    else:
                        t7 = tot(sql7(query2, txt, self.year(), self.month(), i, 7, 0, 45)) - 12600
                        t8 = tot(sql7(query2, txt, self.year(), self.month(), i, 20, 0, 30))
                        t9 = tot(sql7(query2, txt, self.year(), self.month(), i, 23, 0, 59))
                        t10 += self.check(t7) + self.check(t8) + self.check(t9)
                t += t10
            return t
        elif 27900 <= h1 * 60 * 60 + m1 * 60 <= 73800 <= h2 * 60 * 60 + m2 * 60 <= 86400:
            t1 = tot(sql7(query2, txt, self.year(), self.month(), d1, 20, 0, 30))
            t2 = tot(sql7(query2, txt, self.year(), self.month(), d1, h1, 0, m1))
            t3 = self.check(t1) - self.check(t2)
            t4 = tot(sql7(query2, txt, self.year(), self.month(), d1, 23, 0, 59))
            t5 = tot(sql7(query2, txt, self.year(), self.month(), d2, 7, 0, 45)) - 12600
            t6 = tot(sql7(query2, txt, self.year(), self.month(), d2, 20, 0, 30))
            t7 = tot(sql7(query2, txt, self.year(), self.month(), d2, h2, 0, m2))
            t = self.check(t3) + self.check(t4) + self.check(t5) + self.check(t6) + self.check(t7)
            if d2 - d1 != 1:
                t10 = 0
                d3 = d2 - d1
                for i in range(d3):
                    i += d1
                    if i == d1:
                        pass
                    else:
                        t7 = tot(sql7(query2, txt, self.year(), self.month(), i, 7, 0, 45)) - 12600
                        t8 = tot(sql7(query2, txt, self.year(), self.month(), i, 20, 0, 30))
                        t9 = tot(sql7(query2, txt, self.year(), self.month(), i, 23, 0, 59))
                        t10 += self.check(t7) + self.check(t8) + self.check(t9)
                t += t10
            return t
        elif 73800 <= h1 * 60 * 60 + m1 * 60 <= 86400 and h2 * 60 * 60 + m2 * 60 <= 27900:
            t1 = tot(sql7(query2, txt, self.year(), self.month(), d1, 23, 0, 59))
            t2 = tot(sql7(query2, txt, self.year(), self.month(), d1, h1, 0, m1))
            t3 = self.check(t1) - self.check(t2)
            t4 = tot(sql7(query2, txt, self.year(), self.month(), d2, h2, 0, m2)) - 12600
            t = self.check(t3) + self.check(t4)
            if d2 - d1 != 1:
                t10 = 0
                d3 = d2 - d1
                for i in range(d3):
                    i += d1
                    if i == d1:
                        pass
                    else:
                        t7 = tot(sql7(query2, txt, self.year(), self.month(), i, 7, 0, 45)) - 12600
                        t8 = tot(sql7(query2, txt, self.year(), self.month(), i, 20, 0, 30))
                        t9 = tot(sql7(query2, txt, self.year(), self.month(), i, 23, 0, 59))
                        t10 += self.check(t7) + self.check(t8) + self.check(t9)
                t += t10
            return t
        elif 86400 >= h1 * 60 * 60 + m1 * 60 >= 73800 >= h2 * 60 * 60 + m2 * 60 >= 27900:
            t1 = tot(sql7(query2, txt, self.year(), self.month(), d1, 23, 0, 59))
            t2 = tot(sql7(query2, txt, self.year(), self.month(), d1, h1, 0, m1))
            t3 = self.check(t1) - self.check(t2)
            t4 = tot(sql7(query2, txt, self.year(), self.month(), d2, 7, 0, 45)) - 12600
            t5 = tot(sql7(query2, txt, self.year(), self.month(), d2, h2, 0, m2))
            t = self.check(t3) + self.check(t4) + self.check(t5)
            if d2 - d1 != 1:
                t10 = 0
                d3 = d2 - d1
                for i in range(d3):
                    i += d1
                    if i == d1:
                        pass
                    else:
                        t7 = tot(sql7(query2, txt, self.year(), self.month(), i, 7, 0, 45)) - 12600
                        t8 = tot(sql7(query2, txt, self.year(), self.month(), i, 20, 0, 30))
                        t9 = tot(sql7(query2, txt, self.year(), self.month(), i, 23, 0, 59))
                        t10 += self.check(t7) + self.check(t8) + self.check(t9)
                t += t10
            return t
        elif 86400 >= h1 * 60 * 60 + m1 * 60 >= 73800 and 86400 >= h2 * 60 * 60 + m2 * 60 >= 73800:
            t1 = tot(sql7(query2, txt, self.year(), self.month(), d1, 23, 0, 59))
            t2 = tot(sql7(query2, txt, self.year(), self.month(), d1, h1, 0, m1))
            t3 = self.check(t1) - self.check(t2)
            t4 = tot(sql7(query2, txt, self.year(), self.month(), d2, 7, 0, 45)) - 12600
            t5 = tot(sql7(query2, txt, self.year(), self.month(), d2, 20, 0, 30))
            t6 = tot(sql7(query2, txt, self.year(), self.month(), d2, h2, 0, m2))
            t = self.check(t3) + self.check(t4) + self.check(t5) + self.check(t6)
            if d2 - d1 != 1:
                t10 = 0
                d3 = d2 - d1
                for i in range(d3):
                    i += d1
                    if i == d1:
                        pass
                    else:
                        t7 = tot(sql7(query2, txt, self.year(), self.month(), i, 7, 0, 45)) - 12600
                        t8 = tot(sql7(query2, txt, self.year(), self.month(), i, 20, 0, 30))
                        t9 = tot(sql7(query2, txt, self.year(), self.month(), i, 23, 0, 59))
                        t10 += self.check(t7) + self.check(t8) + self.check(t9)
                t += t10
            return t

    def get_total_3(self, txt, mon1, mon2, d1, d2, h1, h2, m1, m2):
        if h1 * 60 * 60 + m1 * 60 <= 27900 and h2 * 60 * 60 + m2 * 60 <= 27900:
            t1 = tot(sql7(query2, txt, self.year(), self.month(), d1, 7, 0, 45)) - 12600
            t2 = tot(sql7(query2, txt, self.year(), self.month(), d1, h1, 0, m1)) - 12600
            t3 = self.check(t1) - self.check(t2)
            t4 = tot(sql7(query2, txt, self.year(), self.month(), d1, 20, 0, 30))
            t5 = tot(sql7(query2, txt, self.year(), self.month(), d1, 23, 30, 59))
            t6 = tot(sql7(query2, txt, self.year(), self.month(), d2, h2, 0, m2)) - 12600
            d3 = self.days(mon1) - d1
            t10 = 0
            for i in range(d3):
                i += d1 + 1
                t101 = tot(sql7(query2, txt, self.year(), self.month(), i, 7, 0, 45)) - 12600
                t102 = tot(sql7(query2, txt, self.year(), self.month(), i, 20, 0, 30))
                t103 = tot(sql7(query2, txt, self.year(), self.month(), i, 23, 0, 59))
                t10 += self.check(t101) + self.check(t102) + self.check(t103)
            t = self.check(t3) + self.check(t4) + self.check(t5) + self.check(t10) + self.check(t6)
            if d2 != 1:
                t20 = 0
                for i in range(d2):
                    i += 1
                    t201 = tot(sql7(query2, txt, self.year(), self.month2(), i, 7, 0, 45)) - 12600
                    t202 = tot(sql7(query2, txt, self.year(), self.month2(), i, 20, 0, 30))
                    t203 = tot(sql7(query2, txt, self.year(), self.month2(), i, 23, 0, 59))
                    t20 += self.check(t201) + self.check(t202) + self.check(t203)
                t += self.check(t20)
            if mon2 - mon1 != 1:
                t30 = 0
                mon3 = mon2 - mon1
                for i in range(mon3):
                    i += 1
                    if i == mon1:
                        pass
                    else:
                        for k in range(self.days(i)):
                            k += 1
                            t301 = tot(sql7(query2, txt, self.year(), i, k, 7, 0, 45)) - 12600
                            t302 = tot(sql7(query2, txt, self.year(), i, k, 20, 0, 30))
                            t303 = tot(sql7(query2, txt, self.year(), i, k, 23, 0, 59))
                            t30 += self.check(t301) + self.check(t302) + self.check(t303)
                t += t30
            return t
        elif h1 * 60 * 60 + m1 * 60 <= 27900 <= h2 * 60 * 60 + m2 * 60 <= 73800:
            t1 = tot(sql7(query2, txt, self.year(), self.month(), d1, 7, 0, 45)) - 12600
            t2 = tot(sql7(query2, txt, self.year(), self.month(), d1, h1, 0, m1)) - 12600
            t3 = self.check(t1) - self.check(t2)
            t4 = tot(sql7(query2, txt, self.year(), self.month(), d1, 20, 0, 30))
            t5 = tot(sql7(query2, txt, self.year(), self.month(), d1, 23, 30, 59))
            t6 = tot(sql7(query2, txt, self.year(), self.month(), d2, 7, 0, 45)) - 12600
            t7 = tot(sql7(query2, txt, self.year(), self.month(), d2, h2, 0, m2))
            d3 = self.days(mon1) - d1
            t10 = 0
            for i in range(d3):
                i += d1 + 1
                t101 = tot(sql7(query2, txt, self.year(), self.month(), i, 7, 0, 45)) - 12600
                t102 = tot(sql7(query2, txt, self.year(), self.month(), i, 20, 0, 30))
                t103 = tot(sql7(query2, txt, self.year(), self.month(), i, 23, 0, 59))
                t10 += self.check(t101) + self.check(t102) + self.check(t103)
            t = self.check(t3) + self.check(t4) + self.check(t5) + self.check(t10) + self.check(t6) + self.check(t7)
            if d2 != 1:
                t20 = 0
                for i in range(d2):
                    i += 1
                    t201 = tot(sql7(query2, txt, self.year(), self.month2(), i, 7, 0, 45)) - 12600
                    t202 = tot(sql7(query2, txt, self.year(), self.month2(), i, 20, 0, 30))
                    t203 = tot(sql7(query2, txt, self.year(), self.month2(), i, 23, 0, 59))
                    t20 += self.check(t201) + self.check(t202) + self.check(t203)
                t += self.check(t20)
            if mon2 - mon1 != 1:
                t30 = 0
                mon3 = mon2 - mon1
                for i in range(mon3):
                    i += 1
                    if i == mon1:
                        pass
                    else:
                        for k in range(self.days(i)):
                            k += 1
                            t301 = tot(sql7(query2, txt, self.year(), i, k, 7, 0, 45)) - 12600
                            t302 = tot(sql7(query2, txt, self.year(), i, k, 20, 0, 30))
                            t303 = tot(sql7(query2, txt, self.year(), i, k, 23, 0, 59))
                            t30 += self.check(t301) + self.check(t302) + self.check(t303)
                t += t30
            return t
        elif h1 * 60 * 60 + m1 * 60 <= 27900 and 73800 <= h2 * 60 * 60 + m2 * 60 <= 86400:
            t1 = tot(sql7(query2, txt, self.year(), self.month(), d1, 7, 0, 45)) - 12600
            t2 = tot(sql7(query2, txt, self.year(), self.month(), d1, h1, 0, m1)) - 12600
            t3 = self.check(t1) - self.check(t2)
            t4 = tot(sql7(query2, txt, self.year(), self.month(), d1, 20, 0, 30))
            t5 = tot(sql7(query2, txt, self.year(), self.month(), d1, 23, 30, 59))
            t6 = tot(sql7(query2, txt, self.year(), self.month(), d2, 7, 0, 45)) - 12600
            t7 = tot(sql7(query2, txt, self.year(), self.month(), d2, 20, 0, 30))
            t8 = tot(sql7(query2, txt, self.year(), self.month(), d2, h2, 0, m2))
            d3 = self.days(mon1) - d1
            t10 = 0
            for i in range(d3):
                i += d1 + 1
                t101 = tot(sql7(query2, txt, self.year(), self.month(), i, 7, 0, 45)) - 12600
                t102 = tot(sql7(query2, txt, self.year(), self.month(), i, 20, 0, 30))
                t103 = tot(sql7(query2, txt, self.year(), self.month(), i, 23, 0, 59))
                t10 += self.check(t101) + self.check(t102) + self.check(t103)
            t = self.check(t3) + self.check(t4) + self.check(t5) + self.check(t10) + self.check(t6) + self.check(t7) + \
                self.check(t8)
            if d2 != 1:
                t20 = 0
                for i in range(d2):
                    i += 1
                    t201 = tot(sql7(query2, txt, self.year(), self.month2(), i, 7, 0, 45)) - 12600
                    t202 = tot(sql7(query2, txt, self.year(), self.month2(), i, 20, 0, 30))
                    t203 = tot(sql7(query2, txt, self.year(), self.month2(), i, 23, 0, 59))
                    t20 += self.check(t201) + self.check(t202) + self.check(t203)
                t += self.check(t20)
            if mon2 - mon1 != 1:
                t30 = 0
                mon3 = mon2 - mon1
                for i in range(mon3):
                    i += 1
                    if i == mon1:
                        pass
                    else:
                        for k in range(self.days(i)):
                            k += 1
                            t301 = tot(sql7(query2, txt, self.year(), i, k, 7, 0, 45)) - 12600
                            t302 = tot(sql7(query2, txt, self.year(), i, k, 20, 0, 30))
                            t303 = tot(sql7(query2, txt, self.year(), i, k, 23, 0, 59))
                            t30 += self.check(t301) + self.check(t302) + self.check(t303)
                t += t30
            return t
        elif 73800 >= h1 * 60 * 60 + m1 * 60 >= 27900 >= h2 * 60 * 60 + m2 * 60:
            t1 = tot(sql7(query2, txt, self.year(), self.month(), d1, 20, 0, 30))
            t2 = tot(sql7(query2, txt, self.year(), self.month(), d1, h1, 0, m1))
            t3 = self.check(t1) - self.check(t2)
            t4 = tot(sql7(query2, txt, self.year(), self.month(), d1, 23, 0, 59))
            t5 = tot(sql7(query2, txt, self.year(), self.month(), d2, h2, 0, m2)) - 12600
            d3 = self.days(mon1) - d1
            t10 = 0
            for i in range(d3):
                i += d1 + 1
                t101 = tot(sql7(query2, txt, self.year(), self.month(), i, 7, 0, 45)) - 12600
                t102 = tot(sql7(query2, txt, self.year(), self.month(), i, 20, 0, 30))
                t103 = tot(sql7(query2, txt, self.year(), self.month(), i, 23, 0, 59))
                t10 += self.check(t101) + self.check(t102) + self.check(t103)
            t = self.check(t3) + self.check(t4) + self.check(t5) + self.check(t10)
            if d2 != 1:
                t20 = 0
                for i in range(d2):
                    i += 1
                    t201 = tot(sql7(query2, txt, self.year(), self.month2(), i, 7, 0, 45)) - 12600
                    t202 = tot(sql7(query2, txt, self.year(), self.month2(), i, 20, 0, 30))
                    t203 = tot(sql7(query2, txt, self.year(), self.month2(), i, 23, 0, 59))
                    t20 += self.check(t201) + self.check(t202) + self.check(t203)
                t += self.check(t20)
            if mon2 - mon1 != 1:
                t30 = 0
                mon3 = mon2 - mon1
                for i in range(mon3):
                    i += 1
                    if i == mon1:
                        pass
                    else:
                        for k in range(self.days(i)):
                            k += 1
                            t301 = tot(sql7(query2, txt, self.year(), i, k, 7, 0, 45)) - 12600
                            t302 = tot(sql7(query2, txt, self.year(), i, k, 20, 0, 30))
                            t303 = tot(sql7(query2, txt, self.year(), i, k, 23, 0, 59))
                            t30 += self.check(t301) + self.check(t302) + self.check(t303)
                t += t30
            return t
        elif 27900 <= h1 * 60 * 60 + m1 * 60 <= 73800 and 27900 <= h2 * 60 * 60 + m2 * 60 <= 73800:
            t1 = tot(sql7(query2, txt, self.year(), self.month(), d1, 20, 0, 30))
            t2 = tot(sql7(query2, txt, self.year(), self.month(), d1, h1, 0, m1))
            t3 = self.check(t1) - self.check(t2)
            t4 = tot(sql7(query2, txt, self.year(), self.month(), d1, 23, 0, 59))
            t5 = tot(sql7(query2, txt, self.year(), self.month(), d2, 7, 0, 45)) - 12600
            t6 = tot(sql7(query2, txt, self.year(), self.month(), d2, h2, 0, m2))
            d3 = self.days(mon1) - d1
            t10 = 0
            for i in range(d3):
                i += d1 + 1
                t101 = tot(sql7(query2, txt, self.year(), self.month(), i, 7, 0, 45)) - 12600
                t102 = tot(sql7(query2, txt, self.year(), self.month(), i, 20, 0, 30))
                t103 = tot(sql7(query2, txt, self.year(), self.month(), i, 23, 0, 59))
                t10 += self.check(t101) + self.check(t102) + self.check(t103)
            t = self.check(t3) + self.check(t4) + self.check(t5) + self.check(t10) + self.check(t6)
            if d2 != 1:
                t20 = 0
                for i in range(d2):
                    i += 1
                    t201 = tot(sql7(query2, txt, self.year(), self.month2(), i, 7, 0, 45)) - 12600
                    t202 = tot(sql7(query2, txt, self.year(), self.month2(), i, 20, 0, 30))
                    t203 = tot(sql7(query2, txt, self.year(), self.month2(), i, 23, 0, 59))
                    t20 += self.check(t201) + self.check(t202) + self.check(t203)
                t += self.check(t20)
            if mon2 - mon1 != 1:
                t30 = 0
                mon3 = mon2 - mon1
                for i in range(mon3):
                    i += 1
                    if i == mon1:
                        pass
                    else:
                        for k in range(self.days(i)):
                            k += 1
                            t301 = tot(sql7(query2, txt, self.year(), i, k, 7, 0, 45)) - 12600
                            t302 = tot(sql7(query2, txt, self.year(), i, k, 20, 0, 30))
                            t303 = tot(sql7(query2, txt, self.year(), i, k, 23, 0, 59))
                            t30 += self.check(t301) + self.check(t302) + self.check(t303)
                t += t30
            return t
        elif 27900 <= h1 * 60 * 60 + m1 * 60 <= 73800 <= h2 * 60 * 60 + m2 * 60 <= 86400:
            t1 = tot(sql7(query2, txt, self.year(), self.month(), d1, 20, 0, 30))
            t2 = tot(sql7(query2, txt, self.year(), self.month(), d1, h1, 0, m1))
            t3 = self.check(t1) - self.check(t2)
            t4 = tot(sql7(query2, txt, self.year(), self.month(), d1, 23, 0, 59))
            t5 = tot(sql7(query2, txt, self.year(), self.month(), d2, 7, 0, 45)) - 12600
            t6 = tot(sql7(query2, txt, self.year(), self.month(), d2, 20, 0, 30))
            t7 = tot(sql7(query2, txt, self.year(), self.month(), d2, h2, 0, m2))
            d3 = self.days(mon1) - d1
            t10 = 0
            for i in range(d3):
                i += d1 + 1
                t101 = tot(sql7(query2, txt, self.year(), self.month(), i, 7, 0, 45)) - 12600
                t102 = tot(sql7(query2, txt, self.year(), self.month(), i, 20, 0, 30))
                t103 = tot(sql7(query2, txt, self.year(), self.month(), i, 23, 0, 59))
                t10 += self.check(t101) + self.check(t102) + self.check(t103)
            t = self.check(t3) + self.check(t4) + self.check(t5) + self.check(t10) + self.check(t6) + self.check(t7)
            if d2 != 1:
                t20 = 0
                for i in range(d2):
                    i += 1
                    t201 = tot(sql7(query2, txt, self.year(), self.month2(), i, 7, 0, 45)) - 12600
                    t202 = tot(sql7(query2, txt, self.year(), self.month2(), i, 20, 0, 30))
                    t203 = tot(sql7(query2, txt, self.year(), self.month2(), i, 23, 0, 59))
                    t20 += self.check(t201) + self.check(t202) + self.check(t203)
                t += self.check(t20)
            if mon2 - mon1 != 1:
                t30 = 0
                mon3 = mon2 - mon1
                for i in range(mon3):
                    i += 1
                    if i == mon1:
                        pass
                    else:
                        for k in range(self.days(i)):
                            k += 1
                            t301 = tot(sql7(query2, txt, self.year(), i, k, 7, 0, 45)) - 12600
                            t302 = tot(sql7(query2, txt, self.year(), i, k, 20, 0, 30))
                            t303 = tot(sql7(query2, txt, self.year(), i, k, 23, 0, 59))
                            t30 += self.check(t301) + self.check(t302) + self.check(t303)
                t += t30
            return t
        elif 73800 <= h1 * 60 * 60 + m1 * 60 <= 86400 and h2 * 60 * 60 + m2 * 60 <= 27900:
            t1 = tot(sql7(query2, txt, self.year(), self.month(), d1, 23, 0, 59))
            t2 = tot(sql7(query2, txt, self.year(), self.month(), d1, h1, 0, m1))
            t3 = self.check(t1) - self.check(t2)
            t4 = tot(sql7(query2, txt, self.year(), self.month(), d2, h2, 0, m2)) - 12600
            d3 = self.days(mon1) - d1
            t10 = 0
            for i in range(d3):
                i += d1 + 1
                t101 = tot(sql7(query2, txt, self.year(), self.month(), i, 7, 0, 45)) - 12600
                t102 = tot(sql7(query2, txt, self.year(), self.month(), i, 20, 0, 30))
                t103 = tot(sql7(query2, txt, self.year(), self.month(), i, 23, 0, 59))
                t10 += self.check(t101) + self.check(t102) + self.check(t103)
            t = self.check(t3) + self.check(t4) + self.check(t10)
            if d2 != 1:
                t20 = 0
                for i in range(d2):
                    i += 1
                    t201 = tot(sql7(query2, txt, self.year(), self.month2(), i, 7, 0, 45)) - 12600
                    t202 = tot(sql7(query2, txt, self.year(), self.month2(), i, 20, 0, 30))
                    t203 = tot(sql7(query2, txt, self.year(), self.month2(), i, 23, 0, 59))
                    t20 += self.check(t201) + self.check(t202) + self.check(t203)
                t += self.check(t20)
            if mon2 - mon1 != 1:
                t30 = 0
                mon3 = mon2 - mon1
                for i in range(mon3):
                    i += 1
                    if i == mon1:
                        pass
                    else:
                        for k in range(self.days(i)):
                            k += 1
                            t301 = tot(sql7(query2, txt, self.year(), i, k, 7, 0, 45)) - 12600
                            t302 = tot(sql7(query2, txt, self.year(), i, k, 20, 0, 30))
                            t303 = tot(sql7(query2, txt, self.year(), i, k, 23, 0, 59))
                            t30 += self.check(t301) + self.check(t302) + self.check(t303)
                t += t30
            return t
        elif 86400 >= h1 * 60 * 60 + m1 * 60 >= 73800 >= h2 * 60 * 60 + m2 * 60 >= 27900:
            t1 = tot(sql7(query2, txt, self.year(), self.month(), d1, 23, 0, 59))
            t2 = tot(sql7(query2, txt, self.year(), self.month(), d1, h1, 0, m1))
            t3 = self.check(t1) - self.check(t2)
            t4 = tot(sql7(query2, txt, self.year(), self.month(), d2, 7, 0, 45)) - 12600
            t5 = tot(sql7(query2, txt, self.year(), self.month(), d2, h2, 0, m2))
            d3 = self.days(mon1) - d1
            t10 = 0
            for i in range(d3):
                i += d1 + 1
                t101 = tot(sql7(query2, txt, self.year(), self.month(), i, 7, 0, 45)) - 12600
                t102 = tot(sql7(query2, txt, self.year(), self.month(), i, 20, 0, 30))
                t103 = tot(sql7(query2, txt, self.year(), self.month(), i, 23, 0, 59))
                t10 += self.check(t101) + self.check(t102) + self.check(t103)
            t = self.check(t3) + self.check(t4) + self.check(t5) + self.check(t10)
            if d2 != 1:
                t20 = 0
                for i in range(d2):
                    i += 1
                    t201 = tot(sql7(query2, txt, self.year(), self.month2(), i, 7, 0, 45)) - 12600
                    t202 = tot(sql7(query2, txt, self.year(), self.month2(), i, 20, 0, 30))
                    t203 = tot(sql7(query2, txt, self.year(), self.month2(), i, 23, 0, 59))
                    t20 += self.check(t201) + self.check(t202) + self.check(t203)
                t += self.check(t20)
            if mon2 - mon1 != 1:
                t30 = 0
                mon3 = mon2 - mon1
                for i in range(mon3):
                    i += 1
                    if i == mon1:
                        pass
                    else:
                        for k in range(self.days(i)):
                            k += 1
                            t301 = tot(sql7(query2, txt, self.year(), i, k, 7, 0, 45)) - 12600
                            t302 = tot(sql7(query2, txt, self.year(), i, k, 20, 0, 30))
                            t303 = tot(sql7(query2, txt, self.year(), i, k, 23, 0, 59))
                            t30 += self.check(t301) + self.check(t302) + self.check(t303)
                t += t30
            return t
        elif 86400 >= h1 * 60 * 60 + m1 * 60 >= 73800 and 86400 >= h2 * 60 * 60 + m2 * 60 >= 73800:
            t1 = tot(sql7(query2, txt, self.year(), self.month(), d1, 23, 0, 59))
            t2 = tot(sql7(query2, txt, self.year(), self.month(), d1, h1, 0, m1))
            t3 = self.check(t1) - self.check(t2)
            t4 = tot(sql7(query2, txt, self.year(), self.month(), d2, 7, 0, 45)) - 12600
            t5 = tot(sql7(query2, txt, self.year(), self.month(), d2, 20, 0, 30))
            t6 = tot(sql7(query2, txt, self.year(), self.month(), d2, h2, 0, m2))
            d3 = self.days(mon1) - d1
            t10 = 0
            for i in range(d3):
                i += d1 + 1
                t101 = tot(sql7(query2, txt, self.year(), self.month(), i, 7, 0, 45)) - 12600
                t102 = tot(sql7(query2, txt, self.year(), self.month(), i, 20, 0, 30))
                t103 = tot(sql7(query2, txt, self.year(), self.month(), i, 23, 0, 59))
                t10 += self.check(t101) + self.check(t102) + self.check(t103)
            t = self.check(t3) + self.check(t4) + self.check(t5) + self.check(t6) + self.check(t10)
            if d2 != 1:
                t20 = 0
                for i in range(d2):
                    i += 1
                    t201 = tot(sql7(query2, txt, self.year(), self.month2(), i, 7, 0, 45)) - 12600
                    t202 = tot(sql7(query2, txt, self.year(), self.month2(), i, 20, 0, 30))
                    t203 = tot(sql7(query2, txt, self.year(), self.month2(), i, 23, 0, 59))
                    t20 += self.check(t201) + self.check(t202) + self.check(t203)
                t += self.check(t20)
            if mon2 - mon1 != 1:
                t30 = 0
                mon3 = mon2 - mon1
                for i in range(mon3):
                    i += 1
                    if i == mon1:
                        pass
                    else:
                        for k in range(self.days(i)):
                            k += 1
                            t301 = tot(sql7(query2, txt, self.year(), i, k, 7, 0, 45)) - 12600
                            t302 = tot(sql7(query2, txt, self.year(), i, k, 20, 0, 30))
                            t303 = tot(sql7(query2, txt, self.year(), i, k, 23, 0, 59))
                            t30 += self.check(t301) + self.check(t302) + self.check(t303)
                t += t30
            return t

    def push(self):
        self.update()
        self.get(eng_name, self.text(eng_name))

    def year(self):
        dt = self.dateTimeEdit.dateTime()
        dt_year = dt.toString("yyyy")
        return int(dt_year)

    def year2(self):
        dt = self.dateTimeEdit_2.dateTime()
        dt_year = dt.toString("yyyy")
        return int(dt_year)

    def month(self):
        dt = self.dateTimeEdit.dateTime()
        dt_month = dt.toString('MM')
        return int(dt_month)

    def month2(self):
        dt = self.dateTimeEdit_2.dateTime()
        dt_month = dt.toString('MM')
        return int(dt_month)

    def day(self):
        dt = self.dateTimeEdit.dateTime()
        dt_day = dt.toString('dd')
        return int(dt_day)

    def day2(self):
        dt = self.dateTimeEdit_2.dateTime()
        dt_day = dt.toString('dd')
        return int(dt_day)

    def hour(self):
        dt = self.dateTimeEdit.dateTime()
        dt_hour = dt.toString('hh')
        return int(dt_hour)

    def hour2(self):
        dt = self.dateTimeEdit_2.dateTime()
        dt_hour = dt.toString('hh')
        return int(dt_hour)

    def min(self):
        dt = self.dateTimeEdit.dateTime()
        dt_min = dt.toString('mm')
        return int(dt_min)

    def min2(self):
        dt = self.dateTimeEdit_2.dateTime()
        dt_min = dt.toString('mm')
        return int(dt_min)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Main_Class()
    ex.show()
    sys.exit(app.exec_())
