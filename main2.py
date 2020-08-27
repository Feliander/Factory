import sys
from PyQt5 import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib import pyplot as plt
from Factory.MyGUI2 import Ui_MainWindow
import pymysql

mydb = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='mydb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
mycursor = mydb.cursor()

# total = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
#         'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
#         'SUM(task), SUM(maket) FROM worktime'

total = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
        'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
        'SUM(task), SUM(maket) FROM worktime ' \
        'WHERE year BETWEEN (%s) AND (%s) ' \
        'AND month BETWEEN (%s) AND (%s) ' \
        'AND day BETWEEN (%s) AND (%s)' \
        'AND hours BETWEEN (%s) AND (%s)' \
        'AND minutes BETWEEN (%s) AND (%s)'

total1 = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
         'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
         'SUM(task), SUM(maket) FROM worktime ' \
         'WHERE year BETWEEN (%s) AND (%s)' \
         ''

laser77 = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
          'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
          'SUM(task), SUM(maket) FROM worktime ' \
          'WHERE name = \'Laser L77\''

laser20 = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
          'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
          'SUM(task), SUM(maket) FROM worktime WHERE name = \'Laser L20\''


class MyMplCanavas(FigureCanvasQTAgg):
    def __init__(self, fig):
        FigureCanvasQTAgg.__init__(self, fig)


def prepare_canvas(gra, layout=None):
    fig, axes = gra
    canvas = MyMplCanavas(fig)
    layout.addWidget(canvas)
    return canvas


def graph(sql, val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, name):
    mycursor.execute(sql, (val1, val2, val3, val4, val5, val6, val7, val8, val9, val10))
    result = mycursor.fetchall()
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
        self.companovka = QtWidgets.QVBoxLayout(self.widget_2)
        self.canvas = prepare_canvas(graph(total, 2019, 2020, 1, 12, 1, 31, 0, 24, 0, 60, 'Участок полноcтью'),
                                     layout=self.companovka)
        self.lbl(total, 2019, 2020, 1, 12, 1, 31, 0, 24, 0, 60, 'Участок полноcтью')
        self.pushButton.clicked.connect(self.push)
        self.pushButton.setText('Ввести SQL запрос')
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.dateTimeEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())

    def zero(self):
        self.canvas = prepare_canvas(graph(total, 2019, 2020, 1, 12, 1, 31, 0, 24, 0, 60, 'Участок полноcтью'),
                                     layout=self.companovka)
        self.lbl(total, 2019, 2020, 1, 12, 1, 31, 0, 24, 0, 60, 'Участок полноcтью')
        QtWidgets.QMessageBox.information(None, 'Ошибка', 'Информации за данный промежуток не существует.\n\n'
                                                          'Будут отображены данные всего участка'
                                                          ' за всё время.')

    def year(self):
        dt = self.dateTimeEdit.dateTime()
        dt_year = dt.toString("yyyy")
        return dt_year

    def year2(self):
        dt = self.dateTimeEdit_2.dateTime()
        dt_year = dt.toString("yyyy")
        return dt_year

    def month(self):
        dt = self.dateTimeEdit.dateTime()
        dt_month = dt.toString('MM')
        return dt_month

    def month2(self):
        dt = self.dateTimeEdit_2.dateTime()
        dt_month = dt.toString('MM')
        return dt_month

    def day(self):
        dt = self.dateTimeEdit.dateTime()
        dt_day = dt.toString('dd')
        return dt_day

    def day2(self):
        dt = self.dateTimeEdit_2.dateTime()
        dt_day = dt.toString('dd')
        return dt_day

    def hour(self):
        dt = self.dateTimeEdit.dateTime()
        dt_hour = dt.toString('hh')
        return dt_hour

    def hour2(self):
        dt = self.dateTimeEdit_2.dateTime()
        dt_hour = dt.toString('hh')
        return dt_hour

    def min(self):
        dt = self.dateTimeEdit.dateTime()
        dt_min = dt.toString('mm')
        return dt_min

    def min2(self):
        dt = self.dateTimeEdit_2.dateTime()
        dt_min = dt.toString('mm')
        return dt_min

    def totall(self):
        pass

    def act(self, text):
        if text == 'Лазер №1':
            self.update()
            try:
                self.canvas = prepare_canvas(graph(laser20, int(self.year()), int(self.year2()), int(self.month()),
                                                   int(self.month2()), int(self.day()), int(self.day2()),
                                                   int(self.hour()), int(self.hour2()), int(self.min()),
                                                   int(self.min2()), 'Лазер №1'),
                                             layout=self.companovka)
                self.lbl(laser20, int(self.year()), int(self.year2()), int(self.month()), int(self.month2()),
                         int(self.day()), int(self.day2()), int(self.hour()), int(self.hour2()), int(self.min()),
                         int(self.min2()), 'Лазер №1')
            except ValueError:
                self.zero()
        elif text == 'Лазер №2':
            self.update()
            try:
                self.canvas = prepare_canvas(graph(laser77, int(self.year()), int(self.year2()), int(self.month()),
                                                   int(self.month2()), int(self.day()), int(self.day2()),
                                                   int(self.hour()), int(self.hour2()), int(self.min()),
                                                   int(self.min2()), 'Лазер №2'),
                                             layout=self.companovka)
                self.lbl(laser77, int(self.year()), int(self.year2()), int(self.month()), int(self.month2()),
                         int(self.day()), int(self.day2()), int(self.hour()), int(self.hour2()), int(self.min()),
                         int(self.min2()), 'Лазер №2')
            except ValueError:
                self.zero()
        elif text == 'Участок полностью':
            self.update()
            try:
                self.canvas = prepare_canvas(graph(total, int(self.year()), int(self.year2()), int(self.month()),
                                                   int(self.month2()), int(self.day()), int(self.day2()),
                                                   int(self.hour()), int(self.hour2()), int(self.min()),
                                                   int(self.min2()), 'Участок полностью'), layout=self.companovka)
                self.lbl(total, int(self.year()), int(self.year2()), int(self.month()), int(self.month2()),
                         int(self.day()), int(self.day2()), int(self.hour()), int(self.hour2()), int(self.min()),
                         int(self.min2()), 'Участок полностью')
            except ValueError:
                self.zero()

    def push(self):
        QtWidgets.QMessageBox.information(None, 'year', self.year())
        QtWidgets.QMessageBox.information(None, 'month', self.month())
        QtWidgets.QMessageBox.information(None, 'day', self.day())
        QtWidgets.QMessageBox.information(None, 'hours', self.hour())
        QtWidgets.QMessageBox.information(None, 'minutes', self.min())
        QtWidgets.QMessageBox.information(None, 'year2', self.year2())
        QtWidgets.QMessageBox.information(None, 'month2', self.month2())
        QtWidgets.QMessageBox.information(None, 'day2', self.day2())
        QtWidgets.QMessageBox.information(None, 'hours2', self.hour2())
        QtWidgets.QMessageBox.information(None, 'minutes2', self.min2())
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

    def update(self):
        self.companovka.removeWidget(self.canvas)
        self.canvas.deleteLater()
        self.canvas = None

    def lbl(self, sql, val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, txt):
        mycursor.execute(sql, (val1, val2, val3, val4, val5, val6, val7, val8, val9, val10))
        result = mycursor.fetchall()
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
        self.label_3.setText(txt)
        self.label_2.setText('Работа:')
        self.label_5.setText("%02d ч %02d м %02d с " %
                             (totall / 3600, (totall / 60) % 60, totall % 60))
        self.label_6.setText('Плановый перерыв:')
        self.label_14.setText("%02d ч %02d м %02d с " %
                              (plan / 3600, (plan / 60) % 60, plan % 60))
        self.label_7.setText('Переналадка/перенастройка:')
        self.label_15.setText("%02d ч %02d м %02d с " %
                              (setup / 3600, (setup / 60) % 60, setup % 60))
        self.label_8.setText('Автономное обслуживание:')
        self.label_16.setText("%02d ч %02d м %02d с " %
                              (autoserv / 3600, (autoserv / 60) % 60, autoserv % 60))
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
                              (maket / 3600, (maket / 60) % 60, maket % 60))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
