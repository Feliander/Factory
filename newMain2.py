import sys
from PyQt5 import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib import pyplot as plt
from MyGUI2 import Ui_MainWindow
import mysql.connector


mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='pOtatO228',
        database='mydb'
    )
mycursor = mydb.cursor()


total = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
            'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
            'SUM(task), SUM(maket) FROM worktime'

laser77 = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
              'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
              'SUM(task), SUM(maket) FROM worktime WHERE name = \'Laser L77\''

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


def graph(sql, name):
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        total = x[0]
        plan = x[1]
        setup = x[2]
        autoserv = x[3]
        ppr = x[4]
        br = x[5]
        material = x[6]
        task = x[7]
        maket = x[8]
        pieces = (total, plan, setup, autoserv, ppr, br, material, task, maket)
        cols = ('#00aa00', '#ff5500', '#5500ff', '#ff00ff', '#aa0000', '#848400', '#309090', '#6d6da3', '#0000ff')
        fig, axes = plt.subplots()
        owners = ['Работа', 'Плановый перерыв', 'Переналадка/Перенастройка',
                  'Автономное обслуживание', 'ППР', 'Поломка оборудования', 'Отсутствие материалов',
                  'Отсутствие задания', 'Изготовление макетов']
        axes.pie(pieces,
                 colors=cols,
                 wedgeprops={'lw': 0.5, 'ls': '-', 'edgecolor': "k"},)
        plt.legend(owners, loc='best', bbox_to_anchor=(0, 1), title='Легенда')
        axes.set_title(name)
        return fig, axes


class Example(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.comboBox.activated[str].connect(self.act)
        self.companovka = QtWidgets.QVBoxLayout(self.widget_2)
        self.canvas = prepare_canvas(graph(total, 'Участок полноcтью'), layout=self.companovka)
        self.pushButton.clicked.connect(self.push)
        self.pushButton.setText('Ввести SQL запрос')
        self.lbl(total, 'Участок полноcтью')
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.dateTimeEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())

    def year(self):
        dt = self.dateTimeEdit.dateTime()
        self.dt_year = dt.toString("yyyy")
        return self.dt_year

    def year2(self):
        dt = self.dateTimeEdit_2.dateTime()
        self.dt_year = dt.toString("yyyy")
        return self.dt_year

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
        if (self.year2() == '2020' and self.year() == '2020'):
            self.total = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
                            'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
                            'SUM(task), SUM(maket) FROM worktime WHERE year = \'2020\''
            return self.total
        elif (self.year2() == '2019' and self.year() == '2020'):
            self.total = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
                            'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
                            'SUM(task), SUM(maket) FROM worktime WHERE (year = \'2019\') AND (year = \'2020\')'
            return self.total

    def act(self, text):
        if text == 'Лазер №1':
            self.update()
            self.canvas = prepare_canvas(graph(self.laser20, 'Лазер №1'), layout=self.companovka)
            self.lbl(self.laser20, 'Лазер №1')
        elif text == 'Лазер №2':
            self.update()
            self.canvas = prepare_canvas(graph(self.laser77, 'Лазер №2'), layout=self.companovka)
            self.lbl(self.laser77, 'Лазер №2')
        elif text == 'Участок полностью':
            try:
                self.update()
                self.canvas = prepare_canvas(graph(self.totall(), 'Участок полностью'), layout=self.companovka)
                self.lbl(self.totall(), 'Участок полностью')
            except:
                self.canvas = prepare_canvas(graph(total, 'Участок полноcтью'), layout=self.companovka)
                QtWidgets.QMessageBox.information(None, 'Message', 'Информации за данный промежуток не существует!')


    def push(self):
        tex, ok = QtWidgets.QInputDialog.getText(None, 'Запрос', 'Введите SQL запрос, например:',
                                       text='SELECT SUM(totaltime) FROM worktime WHERE name = \'Laser L20\'')
        try:
            if ok:
                mycursor.execute(tex)
                myresult = mycursor.fetchall()
                try:
                    for x in myresult:
                        tot = x[0]
                    QtWidgets.QMessageBox.information(None, 'Результат запроса',
                                              'Результат: ' + " %02d ч %02d м %02d с " %
                                              (tot / 3600, (tot / 60) % 60, tot % 60))
                except:
                    flatten = [str(item) for sub in myresult for item in sub]
                    QtWidgets.QMessageBox.information(None, 'Результат запроса',
                                                      'Результат: ' + str(flatten))

        except:
            QtWidgets.QMessageBox.information(None, 'Результат запроса', 'Ошибка!')

    def update(self):
        self.companovka.removeWidget(self.canvas)
        self.canvas.deleteLater()
        self.canvas = None

    def lbl(self, sql, txt):
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            total = x[0]
            plan = x[1]
            setup = x[2]
            autoserv = x[3]
            ppr = x[4]
            br = x[5]
            material = x[6]
            task = x[7]
            maket = x[8]
        self.label_3.setText(txt)
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