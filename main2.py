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

total = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
        'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
        'SUM(task), SUM(maket) FROM worktime'

simple = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
         'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
         'SUM(task), SUM(maket) FROM worktime ' \
         'WHERE (year = (%s))' \
         'AND (month = (%s))' \
         'AND (day = (%s))' \
         'AND (hours = (%s))' \
         'AND (minutes = (%s))'

simple2 = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
          'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
          'SUM(task), SUM(maket) FROM worktime ' \
          'WHERE (year = (%s))' \
          'AND (month = (%s))' \
          'AND (day = (%s))' \
          'AND (hours = (%s))' \
          'AND (minutes BETWEEN (%s) AND (%s))'

simple3 = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
          'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
          'SUM(task), SUM(maket) FROM worktime ' \
          'WHERE (year = (%s))' \
          'AND (month = (%s))' \
          'AND (day = (%s))' \
          'AND (hours BETWEEN (%s) AND (%s))' \
          'AND (minutes = (%s))'

simple4 = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
          'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
          'SUM(task), SUM(maket) FROM worktime ' \
          'WHERE (year = (%s))' \
          'AND (month = (%s))' \
          'AND (day = (%s))' \
          'AND (hours BETWEEN (%s) AND (%s))' \
          'AND (minutes BETWEEN (%s) AND (%s))'


class MyMplCanvas(FigureCanvasQTAgg):
    def __init__(self, fig):
        FigureCanvasQTAgg.__init__(self, fig)


def prepare_canvas(gra, layout=None):
    fig, axes = gra
    canvas = MyMplCanvas(fig)
    layout.addWidget(canvas)
    return canvas


def query0(sql):
    my_cursor.execute(sql)


def query2(sql, val1, val2):
    my_cursor.execute(sql, (val1, val2))


def query5(sql, val1, val2, val3, val4, val5):
    my_cursor.execute(sql, (val1, val2, val3, val4, val5))


def query6(sql, val1, val2, val3, val4, val5, val6):
    my_cursor.execute(sql, (val1, val2, val3, val4, val5, val6))


def query7(sql, val1, val2, val3, val4, val5, val6, val7):
    my_cursor.execute(sql, (val1, val2, val3, val4, val5, val6, val7))


def graph(query, name):
    result = my_cursor.fetchall()
    myresult = (result[0])
    totall = myresult.get('SUM(totaltime)')
    plan = myresult.get('SUM(plantime)')
    setup = myresult.get('SUM(setup)')
    autoserv = myresult.get('SUM(autoserv)')
    ppr = myresult.get('SUM(ppr)')
    br = myresult.get('SUM(break)')
    material = myresult.get('SUM(material)')
    task = myresult.get('SUM(task)')
    maket = myresult.get('SUM(maket)')
    pieces = (totall, plan, setup, autoserv, ppr, br, material, task, maket)
    cols = ('#00aa00', '#ff5500', '#5500ff', '#ff00ff', '#aa0000', '#848400', '#309090', '#6d6da3', '#0000ff')
    fig, axes = plt.subplots()
    owners = ['Работа', 'Плановый перерыв', 'Переналадка/Перенастройка',
              'Автономное обслуживание', 'ППР', 'Поломка оборудования', 'Отсутствие материалов',
              'Отсутствие задания', 'Изготовление макетов']
    axes.pie(pieces,
             colors=cols,
             wedgeprops={'lw': 0.5, 'ls': '-', 'edgecolor': "k"}, )
    plt.legend(owners, loc='best', bbox_to_anchor=(0, 1), title='Легенда')
    axes.set_title(name)
    return fig, axes


class Example(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.comboBox.activated[str].connect(self.act)
        self.composition = QtWidgets.QVBoxLayout(self.widget_2)
        self.prepare_canvas(query0(total), 'Участок полноcтью')
        self.prepare_label(query0(total), 'Участок полноcтью')
        self.pushButton.clicked.connect(self.push)
        self.pushButton.setText('Ввести SQL запрос')
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.dateTimeEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())

    def prepare_canvas(self, query, txt):
        self.canvas = prepare_canvas(graph(query, txt), layout=self.composition)

    def prepare_label(self, query, txt):
        result = my_cursor.fetchall()
        my_result = (result[0])
        total_1 = my_result.get('SUM(totaltime)')
        plan = my_result.get('SUM(plantime)')
        setup = my_result.get('SUM(setup)')
        auto_serv = my_result.get('SUM(autoserv)')
        ppr = my_result.get('SUM(ppr)')
        br = my_result.get('SUM(break)')
        material = my_result.get('SUM(material)')
        task = my_result.get('SUM(task)')
        model = my_result.get('SUM(maket)')
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
                              (ppr / 3600, (ppr / 60) % 60, ppr % 60))
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
        self.prepare_canvas(query0(total), 'Участок полноcтью')
        self.prepare_label(query0(total), 'Участок полноcтью')
        QtWidgets.QMessageBox.information(None, 'Ошибка', 'Информации за данный промежуток не существует.\n\n'
                                                          'Будут отображены данные всего участка'
                                                          ' за всё время.')

    def act(self, text):
        if text == 'Участок полностью':
            self.update()
            try:
                self.total()
            except ValueError:
                self.zero()

    def total(self):
        if self.year() == self.year2():
            if self.month() == self.month2():
                if self.day() == self.day2():
                    if self.hour() == self.hour2():
                        if self.min() == self.min2():
                            self.prepare_canvas(query5(simple, self.year(), self.month(), self.day(),
                                                       self.hour(), self.min()), 'Участок полностью')
                            self.prepare_label(query5(simple, self.year(), self.month(), self.day(),
                                                      self.hour(), self.min()), 'Участок полноcтью')
                        elif self.min() <= self.min2():
                            self.prepare_canvas(query6(simple2, self.year(), self.month(), self.day(),
                                                       self.hour(), self.min(), self.min2()), 'Участок полностью')
                            self.prepare_label(query6(simple2, self.year(), self.month(), self.day(),
                                                      self.hour(), self.hour2(), self.min()), 'Участок полноcтью')
                    elif self.hour() <= self.hour2():
                        if self. min() == self.min2():
                            self.prepare_canvas(query6(simple3, self.year(), self.month(), self.day(),
                                                       self.hour(), self.min(), self.min2()), 'Участок полностью')
                            self.prepare_label(query6(simple3, self.year(), self.month(), self.day(),
                                                      self.hour(), self.hour2(), self.min()), 'Участок полноcтью')
                        elif self.min() <= self.min2():
                            self.prepare_canvas(query7(simple4, self.year(), self.month(), self.day(),
                                                       self.hour(), self.hour2(), self.min(), self.min2()),
                                                'Участок полностью')
                            self.prepare_label(query7(simple4, self.year(), self.month(), self.day(),
                                                      self.hour(), self.hour2(), self.hour2(), self.min()),
                                               'Участок полноcтью')
            elif self.month() > self.month2():
                self.zero()
        elif self.year() > self.year2():
            self.zero()

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
