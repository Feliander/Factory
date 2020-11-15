import sys
from PyQt5 import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib import pyplot as plt
from Factory.MyGUI2 import Ui_MainWindow
import pymysql

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
         'SUM(task), SUM(maket) FROM worktime WHERE (name = %s) AND (year = (%s)) AND (month = (%s)) AND (day = (%s)) ' \
         'AND (hours BETWEEN (%s) AND (%s))'

query2 = 'SELECT MAX(totaltime), SUM(plantime), SUM(setup), SUM(autoserv), SUM(ppr), SUM(break), SUM(material), ' \
         'SUM(task), SUM(maket) FROM worktime WHERE (name = %s) AND (year = (%s)) AND (month = (%s)) ' \
         'AND (day = (%s)) AND (hours = (%s)) AND (minutes BETWEEN (%s) AND (%s))'

query3 = 'SELECT MAX(totaltime), SUM(plantime), SUM(setup), SUM(autoserv), SUM(ppr), SUM(break), SUM(material), ' \
         'SUM(task), SUM(maket) FROM worktime WHERE (name = %s) AND (year = (%s)) AND (month = (%s)) ' \
         'AND (day BETWEEN (%s) AND (%s))'


class MyMplCanvas(FigureCanvasQTAgg):
    def __init__(self, fig):
        FigureCanvasQTAgg.__init__(self, fig)


def prepare_canvas(gra, layout=None):
    fig, axes = gra
    canvas = MyMplCanvas(fig)
    layout.addWidget(canvas)
    return canvas


def sql5(query, val1, val2, val3, val4, val5):
    my_cursor.execute(query, (val1, val2, val3, val4, val5))


def sql6(query, val1, val2, val3, val4, val5, val6):
    my_cursor.execute(query, (val1, val2, val3, val4, val5, val6))


def sql7(query, val1, val2, val3, val4, val5, val6, val7):
    my_cursor.execute(query, (val1, val2, val3, val4, val5, val6, val7))


def tot(sql):
    result = my_cursor.fetchall()
    my_result = (result[0])
    t1 = ()
    t2 = ()
    t3 = ()
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


class Example(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.comboBox.activated[str].connect(self.act)
        self.composition = QtWidgets.QVBoxLayout(self.widget_2)
        self.canvas = prepare_canvas(graph('Графика нет, выберите дату', 10, 10, 10, 10, 10, 10, 10, 10, 10),
                                     layout=self.composition)
        self.prepare_label('Графика нет, выберите дату')
        self.pushButton.clicked.connect(self.push)
        self.pushButton.setText('Ввести SQL запрос')
        self.dateTimeEdit.setCalendarPopup(True)
        # self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(2020, 1, 1, 0, 0, 0))
        self.dateTimeEdit_2.setCalendarPopup(True)
        # self.dateTimeEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateTimeEdit_2.setDateTime(QtCore.QDateTime(2020, 1, 1, 23, 59, 0))

    def prepare_label(self, txt, total_1=10, plan=10, setup=10, auto_serv=10, ppr1=10, br=10, material=10, task=10,
                      model=10):
        self.label_3.setText(txt)
        self.label_2.setText('Работа:')
        self.label_5.setText("%02d ч %02d м %02d с " %
                             (total_1 / 3600, (total_1 / 60) % 60, total_1 % 60))
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

    def act(self, text):
        self.update()
        if text == 'Лазер №1':
            txt = 'Laser1'
            self.total(txt, text)
        elif text == 'Лазер №2':
            txt = 'Laser2'
            self.total(txt, text)
        elif text == 'Пробивка №1':
            txt = 'Punch1'
            self.total(txt, text)
        elif text == 'Пробивка №2':
            txt = 'Punch2'
            self.total(txt, text)
        elif text == 'Гибка №1':
            txt = 'Bend1'
            self.total(txt, text)
        elif text == 'Гибка №2':
            txt = 'Bend2'
            self.total(txt, text)
        elif text == 'Сварка №1':
            txt = 'Weld1'
            self.total(txt, text)
        elif text == 'Сварка №2':
            txt = 'Weld2'
            self.total(txt, text)
        elif text == 'Сварочный робот №1':
            txt = 'Weld_Robot1'
            self.total(txt, text)
        elif text == 'Сварочный робот №2':
            txt = 'Weld_Robot2'
            self.total(txt, text)
        elif text == 'Сборка №1':
            txt = 'Assembly1'
            self.total(txt, text)
        elif text == 'Сборка №2':
            txt = 'Assembly2'
            self.total(txt, text)
        elif text == 'Зачистка №1':
            txt = 'Cleaning1'
            self.total(txt, text)
        elif text == 'Зачистка №2':
            txt = 'Cleaning2'
            self.total(txt, text)

    def total(self, txt, text):
        if self.year() == self.year2():
            if self.month() == self.month2():
                if self.day() == self.day2():
                    if self.hour() == self.hour2():
                        if self.min() <= self.min2():
                            t = tot(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(),
                                         self.min2()))
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
                            self.canvas = prepare_canvas(graph(text, self.check(t), self.check(p), self.check(s),
                                                               self.check(a), self.check(r), self.check(b),
                                                               self.check(m), self.check(k), self.check(d)),
                                                         layout=self.composition)
                            self.prepare_label(text, self.check(t), self.check(p), self.check(s), self.check(a),
                                               self.check(r), self.check(b), self.check(m), self.check(k),
                                               self.check(d))
                            if self.check(t) == 0:
                                self.update()
                                self.zero()
                            else:
                                self.explanation1(txt)
                        else:
                            self.zero2()
                    elif self.hour() <= self.hour2():
                        t1 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 60))
                        t2 = tot(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1,
                                      self.hour2() - 1))
                        t3 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour2(), 0, self.min2()))
                        t = self.check(t1) + self.check(t2) + self.check(t3)
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
                        if self.check(t) == 0:
                            self.update()
                            self.zero()
                        else:
                            self.explanation0(txt)
                    else:
                        self.zero2()
                elif self.day() <= self.day2():
                    t1 = tot(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 60))
                    t2 = tot(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1, 24))
                    t3 = tot(sql5(query3, txt, self.year(), self.month(), self.day() + 1, self.day2() - 1))
                    t4 = tot(sql6(query1, txt, self.year(), self.month(), self.day2(), 0, self.hour2()))
                    t5 = tot(sql7(query2, txt, self.year(), self.month(), self.day2(), self.hour2(), 0, self.min2()))
                    t = self.check(t1) + self.check(t2) + self.check(t3) + self.check(t4) + self.check(t5)
                    self.canvas = prepare_canvas(graph(text, self.check(t), 10, 10, 10, 10, 10, 10, 10, 10),
                                                 layout=self.composition)
                    self.prepare_label(text, self.check(t), 10, 10, 10, 10, 10, 10, 10, 10)
                else:
                    self.zero2()
            else:
                self.zero()
        else:
            self.zero()

    def explanation0(self, txt):
        t_1 = self.check(tot(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(), 60)))
        t_2 = self.check(tot(sql6(query1, txt, self.year(), self.month(), self.day(), self.hour() + 1,
                                  self.hour2() - 1)))
        t_3 = self.check(tot(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour2(), 0, self.min2())))
        t_4 = t_1 + t_2 + t_3
        explanation = 'Запрос разделён на три части.' \
                      '\n\nПервый запрос:' \
                      '\nВыбрать всё необходимое где дата равна:' \
                      '\n' + self.check2(str(self.day())) + '.' + self.check2(str(self.month())) + '.' + \
                      str(self.year()) + ' ' + self.check2(str(self.hour())) + ' часов' \
                      '\nИ минуты в промежутке между: ' + self.check2(str(self.min())) + ' и 60' \
                      '\nРабота: ' + ("%02d ч %02d м %02d с " % (t_1 / 3600, (t_1 / 60) % 60, t_1 % 60)) + \
                      ' или ' + str(t_1) + ' секунд'\
                      '\n\nВторой запрос:' \
                      '\nВыбрать всё необходимое где дата равна:' + \
                      '\n' + self.check2(str(self.day())) + '.' + self.check2(str(self.month())) + '.' + \
                      str(self.year()) + \
                      '\nИ часы в промежутке между: ' + self.check2(str(self.hour() + 1)) + ':00 и ' \
                      + self.check2(str(self.hour2() - 1)) + ':00' + \
                      '\nРабота: ' + ("%02d ч %02d м %02d с " % (t_2 / 3600, (t_2 / 60) % 60, t_2 % 60)) + \
                      ' или ' + str(t_2) + ' секунд'\
                      '\n\nТретий запрос:' \
                      '\nВыбрать всё необходимое где дата равна:' + \
                      '\n' + self.check2(str(self.day())) + '.' + self.check2(str(self.month())) + '.' + \
                      str(self.year()) + ' ' + self.check2(str(self.hour2())) + ' часов'\
                      '\nИ минуты в промежутке между: 0 и ' + self.check2(str(self.min2())) + \
                      '\nРабота: ' + ("%02d ч %02d м %02d с " % (t_3 / 3600, (t_3 / 60) % 60, t_3 % 60)) + \
                      ' или ' + str(t_3) + ' секунд'\
                      '\n\nРабота всего: ' + ("%02d ч %02d м %02d с " %
                                              (t_4 / 3600, (t_4 / 60) % 60, t_4 % 60)) + \
                      ' или ' + str(t_4) + ' секунд'
        QtWidgets.QMessageBox.information(None, 'Удачный запрос', explanation)

    def explanation1(self, txt):
        t = self.check(tot(sql7(query2, txt, self.year(), self.month(), self.day(), self.hour(), self.min(),
                                self.min2())))
        explanation = 'Запрос состоит из одной части.' \
                      '\n\nВыбрать всё необходимое где дата равна:' \
                      '\n' + self.check2(str(self.day())) + '.' + self.check2(str(self.month())) + '.' + \
                      str(self.year()) + ' ' + self.check2(str(self.hour())) + ' часов' \
                      '\nИ минуты в промежутке между: ' + self.check2(str(self.min())) + ' и ' + \
                      self.check2(str(self.min2())) + \
                      '\nРабота: ' + ("%02d ч %02d м %02d с " % (t / 3600, (t / 60) % 60, t % 60)) + \
                      ' или ' + str(t) + ' секунд'
        QtWidgets.QMessageBox.information(None, 'Удачный запрос', explanation)

    @staticmethod
    def check2(val):
        if val == '0':
            val = '00'
        elif len(val) == 1:
            val = '0' + val
        return val

    @staticmethod
    def check(val):
        if val is None:
            val = 0
        return val

    def push(self):
        QtWidgets.QMessageBox.information(None, 'year', str(self.year()))
        QtWidgets.QMessageBox.information(None, 'month', str(self.month()))
        QtWidgets.QMessageBox.information(None, 'day', str(self.day()))
        QtWidgets.QMessageBox.information(None, 'hours', str(self.hour()))
        QtWidgets.QMessageBox.information(None, 'minutes', str(self.min()))
        QtWidgets.QMessageBox.information(None, 'year2', str(self.year2()))
        QtWidgets.QMessageBox.information(None, 'month2', str(self.month2()))
        QtWidgets.QMessageBox.information(None, 'day2', str(self.day2()))
        QtWidgets.QMessageBox.information(None, 'hours2', str(self.hour2()))
        QtWidgets.QMessageBox.information(None, 'minutes2', str(self.min2()))
        # tex, ok = QtWidgets.QInputDialog.getText(None, 'Запрос', 'Введите SQL запрос, например:',
        #                                        text='SELECT SUM(totaltime) FROM worktime WHERE name = \'Laser L20\'')
        # try:
        #     if ok:
        #         mycursor.execute(tex)
        #         myresult = mycursor.fetchall()
        #         try:
        #             for x in myresult:
        #                 tot = x[0]
        #             QtWidgets.QMessageBox.information(None, 'Результат запроса',
        #                                               'Результат: ' + " %02d ч %02d м %02d с " %
        #                                               (tot / 3600, (tot / 60) % 60, tot % 60))
        #         except:
        #             flatten = [str(item) for sub in myresult for item in sub]
        #             QtWidgets.QMessageBox.information(None, 'Результат запроса',
        #                                               'Результат: ' + str(flatten))
        #
        # except:
        #     QtWidgets.QMessageBox.information(None, 'Результат запроса', 'Ошибка!')

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
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
