import sys
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib import pyplot as plt
from Factory.MyGUI3 import Ui_MainWindow
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


class MyMplCanavas(FigureCanvasQTAgg):
    def __init__(self, fig):
        FigureCanvasQTAgg.__init__(self, fig)


Total = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
            'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
            'SUM(task), SUM(maket) FROM worktime'

Laser20 = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
            'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
            'SUM(task), SUM(maket) FROM worktime WHERE name = \'Laser L20\''

Laser77 = 'SELECT SUM(totaltime), SUM(plantime), SUM(setup),' \
                    'SUM(autoserv), SUM(ppr), SUM(break), SUM(material),' \
                    'SUM(task), SUM(maket) FROM worktime WHERE name = \'Laser L77\''


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
        fig, axes = plt.subplots()
        owners = ['Работа', 'Плановый перерыв', 'Переналадка/Перенастройка',
                  'Автономное обслуживание', 'ППР', 'Поломка оборудования', 'Отсутствие материалов',
                  'Отсутствие задания', 'Изготовление макетов']
        axes.pie(pieces)
        plt.legend(owners, loc='best', bbox_to_anchor=(0, 1), title='Легенда')
        axes.set_title(name)
        return fig, axes


class Example(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.comboBox.activated[str].connect(self.act)
        self.comboBox.addItem('Total')
        self.companovka = QtWidgets.QVBoxLayout(self.widget_2)
        self.canvas = prepare_canvas(graph(Total, 'Участок полноcтью'), layout=self.companovka)
        self.pushButton.clicked.connect(self.push)
        self.pushButton.setText('Ввести SQL запрос')

    def push(self):
        tex, ok = QtWidgets.QInputDialog.getText(None, 'Запрос', 'Введите SQL запрос',
                                       text='SELECT SUM(totaltime) FROM worktime WHERE name = \'Laser L20\'')
        if ok:
            mycursor.execute(tex)
            myresult = mycursor.fetchall()
            for x in myresult:
                tot = x[0]
            QtWidgets.QMessageBox.information(None, 'Результат запроса',
                                              'Результат: ' + " %02d ч %02d м %02d с " %
                                              (tot / 3600, (tot / 60) % 60, tot % 60))

    def act(self, text):
        if text == 'Laser 20':
            self.update()
            self.canvas = prepare_canvas(graph(Laser20, 'Лазер L20'), layout=self.companovka)
            self.lbl(Laser20, 'Лазер L20')
        elif text == 'Laser 77':
            self.update()
            self.canvas = prepare_canvas(graph(Laser77, 'Лазер L77'), layout=self.companovka)
            self.lbl(Laser77, 'Лазер L77')
        elif text == 'Total':
            self.update()
            self.canvas = prepare_canvas(graph(Total, 'Участок полностью'), layout=self.companovka)
            self.lbl(Total, 'Участок полностью')

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
        self.label_2.setText('Работа:' + " %02d ч %02d м %02d с " %
                             (total / 3600, (total / 60) % 60, total % 60))
        self.label_4.setText('Плановый перерыв:' + " %02d ч %02d м %02d с " %
                             (plan / 3600, (plan / 60) % 60, plan % 60))
        self.label_5.setText('Переналадка/перенастройка:' + " %02d ч %02d м %02d с " %
                             (setup / 3600, (setup / 60) % 60, setup % 60))
        self.label_6.setText('Автономное обслуживание:' + " %02d ч %02d м %02d с " %
                             (autoserv / 3600, (autoserv / 60) % 60, autoserv % 60))
        self.label_7.setText('ППР:' + " %02d ч %02d м %02d с " %
                             (ppr / 3600, (ppr / 60) % 60, ppr % 60))
        self.label_8.setText('Поломка оборудования:' + " %02d ч %02d м %02d с " %
                             (br / 3600, (br / 60) % 60, br % 60))
        self.label_9.setText('Отсутствие материалов:' + " %02d ч %02d м %02d с " %
                             (material / 3600, (material / 60) % 60, material % 60))
        self.label_10.setText('Отсутствие задания:' + " %02d ч %02d м %02d с " %
                             (task / 3600, (task / 60) % 60, task % 60))
        self.label_11.setText('Изготовление макетов:' + " %02d ч %02d м %02d с " %
                              (maket / 3600, (maket / 60) % 60, maket % 60))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())