import sys
import datetime
import pymysql
from PyQt5 import QtWidgets, QtCore
from Factory.MyGUI import Ui_MainWindow


class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.pushButton_3_clicked)
        self.ui.pushButton_4.clicked.connect(self.pushButton_4_clicked)
        self.ui.pushButton_5.clicked.connect(self.pushButton_5_clicked)
        self.ui.pushButton_6.clicked.connect(self.pushButton_6_clicked)
        self.ui.pushButton_7.clicked.connect(self.pushButton_7_clicked)
        self.ui.pushButton_8.clicked.connect(self.pushButton_8_clicked)
        self.ui.pushButton_9.clicked.connect(self.pushButton_9_clicked)
        self.ui.pushButton_10.clicked.connect(self.pushButton_10_clicked)
        self.ui.pushButton_11.clicked.connect(self.pushButton_11_clicked)
        self.ui.pushButton_12.clicked.connect(self.pushButton_12_clicked)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_5.setEnabled(False)
        self.ui.pushButton_6.setEnabled(False)
        self.ui.pushButton_7.setEnabled(False)
        self.ui.pushButton_8.setEnabled(False)
        self.ui.pushButton_9.setEnabled(False)
        self.ui.pushButton_10.setEnabled(False)
        self.ui.pushButton_11.setEnabled(False)
        self.ui.pushButton_12.setEnabled(False)
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='mydb',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.mycursor = self.connection.cursor()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateTimer)
        self.timer2 = QtCore.QTimer(self)
        self.timer2.timeout.connect(self.updateTimer2)
        self.counter = 0
        self.my_counter = 0
        self.plancounter = 0
        self.setupcounter = 0
        self.autoservcounter = 0
        self.pprcounter = 0
        self.breakcounter = 0
        self.matcounter = 0
        self.taskcounter = 0
        self.maketcounter = 0
        self.text = ''

    def pushButton_3_clicked(self):
        self.my_counter = 0
        self.ui.label.setText("Рабочая смена:" + " %02d:%02d:%02d" % (
            self.my_counter / 3600, (self.my_counter / 60) % 60, self.my_counter % 60))
        self.timer.start(1000)
        try:
            self.action = 'start'
            self.sendtomysql()
        except:
            QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(True)
        self.ui.pushButton_5.setEnabled(True)
        self.ui.pushButton_6.setEnabled(True)
        self.ui.pushButton_7.setEnabled(True)
        self.ui.pushButton_8.setEnabled(True)
        self.ui.pushButton_9.setEnabled(True)
        self.ui.pushButton_10.setEnabled(True)
        self.ui.pushButton_11.setEnabled(True)
        self.ui.pushButton_12.setEnabled(True)
        self.ui.frame_2.setStyleSheet("background-color: rgb(0, 200, 0);")

    def updateTimer(self):
        self.my_counter += 1
        if self.my_counter >= 0:
            self.ui.label.setText("Рабочая смена:" + " %02d:%02d:%02d" % (
                self.my_counter / 3600, (self.my_counter / 60) % 60, self.my_counter % 60))
        else:
            self.timer.stop()

    def pushButton_4_clicked(self):
        self.timer.stop()
        self.timer2.stop()
        self.ui.label_2.clear()
        try:
            self.action = 'stop'
            self.sendtomysql()
        except:
            QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
        self.counter = 0
        self.my_counter = 0
        self.plancounter = 0
        self.setupcounter = 0
        self.autoservcounter = 0
        self.pprcounter = 0
        self.breakcounter = 0
        self.matcounter = 0
        self.taskcounter = 0
        self.maketcounter = 0
        self.ui.pushButton_3.setEnabled(True)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_5.setEnabled(False)
        self.ui.pushButton_6.setEnabled(False)
        self.ui.pushButton_7.setEnabled(False)
        self.ui.pushButton_8.setEnabled(False)
        self.ui.pushButton_9.setEnabled(False)
        self.ui.pushButton_10.setEnabled(False)
        self.ui.pushButton_11.setEnabled(False)
        self.ui.pushButton_12.setEnabled(False)
        self.ui.frame_2.setStyleSheet("background-color: rgb(255, 255, 0);")

    def pushButton_5_clicked(self):
        self.text = 'Плановый перерыв:'
        if self.counter == 0:
            self.ui.label_2.setText(self.text + " %02d:%02d:%02d" % (
                self.counter / 3600, (self.counter / 60) % 60, self.counter % 60))
            self.timer2.start(1000)
            try:
                self.action = 'start_plan_counter'
                self.sendtomysql()
            except:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_5.setEnabled(True)
            self.ui.pushButton_6.setEnabled(False)
            self.ui.pushButton_7.setEnabled(False)
            self.ui.pushButton_8.setEnabled(False)
            self.ui.pushButton_9.setEnabled(False)
            self.ui.pushButton_10.setEnabled(False)
            self.ui.pushButton_11.setEnabled(False)
            self.ui.pushButton_12.setEnabled(False)
            self.ui.frame_2.setStyleSheet("background-color: rgb(200, 0, 0);")
        else:
            self.timer2.stop()
            self.plancounter = self.counter
            self.action = 'stop_plan_counter'
            try:
                self.sendtomysql()
            except:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.counter = 0
            self.plancounter = 0
            self.ui.label_2.clear()
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_5.setEnabled(True)
            self.ui.pushButton_6.setEnabled(True)
            self.ui.pushButton_7.setEnabled(True)
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_9.setEnabled(True)
            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_11.setEnabled(True)
            self.ui.pushButton_12.setEnabled(True)
            self.ui.frame_2.setStyleSheet("background-color: rgb(0, 200, 0);")

    def updateTimer2(self):
        self.counter += 1
        if self.counter >= 0:
            self.ui.label_2.setText(self.text + " %02d:%02d:%02d" % (
                self.counter / 3600, (self.counter / 60) % 60, self.counter % 60))
        else:
            self.timer2.stop()

    def pushButton_6_clicked(self):
        self.text = 'Переналадка, перенастройка:'
        if self.counter == 0:
            self.ui.label_2.setText(self.text + " %02d:%02d:%02d" % (
                self.counter / 3600, (self.counter / 60) % 60, self.counter % 60))
            self.timer2.start(1000)
            try:
                self.action = 'start_setup'
                self.sendtomysql()
            except:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_5.setEnabled(False)
            self.ui.pushButton_6.setEnabled(True)
            self.ui.pushButton_7.setEnabled(False)
            self.ui.pushButton_8.setEnabled(False)
            self.ui.pushButton_9.setEnabled(False)
            self.ui.pushButton_10.setEnabled(False)
            self.ui.pushButton_11.setEnabled(False)
            self.ui.pushButton_12.setEnabled(False)
            self.ui.frame_2.setStyleSheet("background-color: rgb(200, 0, 0);")
        else:
            self.timer2.stop()
            self.setupcounter = self.counter
            self.action = 'stop_setup'
            try:
                self.sendtomysql()
            except:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.counter = 0
            self.setupcounter = 0
            self.ui.label_2.clear()
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_5.setEnabled(True)
            self.ui.pushButton_6.setEnabled(True)
            self.ui.pushButton_7.setEnabled(True)
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_9.setEnabled(True)
            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_11.setEnabled(True)
            self.ui.pushButton_12.setEnabled(True)
            self.ui.frame_2.setStyleSheet("background-color: rgb(0, 200, 0);")

    def pushButton_7_clicked(self):
        self.text = 'Автономное обслуживание:'
        if self.counter == 0:
            self.ui.label_2.setText(self.text + " %02d:%02d:%02d" % (
                self.counter / 3600, (self.counter / 60) % 60, self.counter % 60))
            self.timer2.start(1000)
            try:
                self.action = 'start_auto_service'
                self.sendtomysql()
            except:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_5.setEnabled(False)
            self.ui.pushButton_6.setEnabled(False)
            self.ui.pushButton_7.setEnabled(True)
            self.ui.pushButton_8.setEnabled(False)
            self.ui.pushButton_9.setEnabled(False)
            self.ui.pushButton_10.setEnabled(False)
            self.ui.pushButton_11.setEnabled(False)
            self.ui.pushButton_12.setEnabled(False)
            self.ui.frame_2.setStyleSheet("background-color: rgb(200, 0, 0);")
        else:
            self.timer2.stop()
            self.autoservcounter = self.counter
            self.action = 'stop_auto_service'
            try:
                self.sendtomysql()
            except:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.counter = 0
            self.autoservcounter = 0
            self.ui.label_2.clear()
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_5.setEnabled(True)
            self.ui.pushButton_6.setEnabled(True)
            self.ui.pushButton_7.setEnabled(True)
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_9.setEnabled(True)
            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_11.setEnabled(True)
            self.ui.pushButton_12.setEnabled(True)
            self.ui.frame_2.setStyleSheet("background-color: rgb(0, 200, 0);")

    def pushButton_8_clicked(self):
        self.text = 'Поломка оборудования:'
        if self.counter == 0:
            self.ui.label_2.setText(self.text + " %02d:%02d:%02d" % (
                self.counter / 3600, (self.counter / 60) % 60, self.counter % 60))
            self.timer2.start(1000)
            try:
                self.action = 'start_break'
                self.sendtomysql()
            except:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_5.setEnabled(False)
            self.ui.pushButton_6.setEnabled(False)
            self.ui.pushButton_7.setEnabled(False)
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_9.setEnabled(False)
            self.ui.pushButton_10.setEnabled(False)
            self.ui.pushButton_11.setEnabled(False)
            self.ui.pushButton_12.setEnabled(False)
            self.ui.frame_2.setStyleSheet("background-color: rgb(200, 0, 0);")
        else:
            self.timer2.stop()
            self.breakcounter = self.counter
            self.action = 'stop_break'
            try:
                self.sendtomysql()
            except:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.counter = 0
            self.breakcounter = 0
            self.ui.label_2.clear()
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_5.setEnabled(True)
            self.ui.pushButton_6.setEnabled(True)
            self.ui.pushButton_7.setEnabled(True)
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_9.setEnabled(True)
            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_11.setEnabled(True)
            self.ui.pushButton_12.setEnabled(True)
            self.ui.frame_2.setStyleSheet("background-color: rgb(0, 200, 0);")

    def pushButton_9_clicked(self):
        self.text = 'Отсутствие материалов:'
        if self.counter == 0:
            self.ui.label_2.setText(self.text + " %02d:%02d:%02d" % (
                self.counter / 3600, (self.counter / 60) % 60, self.counter % 60))
            self.timer2.start(1000)
            try:
                self.action = 'start_material'
                self.sendtomysql()
            except:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_5.setEnabled(False)
            self.ui.pushButton_6.setEnabled(False)
            self.ui.pushButton_7.setEnabled(False)
            self.ui.pushButton_8.setEnabled(False)
            self.ui.pushButton_9.setEnabled(True)
            self.ui.pushButton_10.setEnabled(False)
            self.ui.pushButton_11.setEnabled(False)
            self.ui.pushButton_12.setEnabled(False)
            self.ui.frame_2.setStyleSheet("background-color: rgb(200, 0, 0);")
        else:
            self.timer2.stop()
            self.matcounter = self.counter
            self.action = 'stop_material'
            try:
                self.sendtomysql()
            except:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.counter = 0
            self.matcounter = 0
            self.ui.label_2.clear()
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_5.setEnabled(True)
            self.ui.pushButton_6.setEnabled(True)
            self.ui.pushButton_7.setEnabled(True)
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_9.setEnabled(True)
            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_11.setEnabled(True)
            self.ui.pushButton_12.setEnabled(True)
            self.ui.frame_2.setStyleSheet("background-color: rgb(0, 200, 0);")

    def pushButton_10_clicked(self):
        self.text = 'Отсутствие задания:'
        if self.counter == 0:
            self.ui.label_2.setText(self.text + " %02d:%02d:%02d" % (
                self.counter / 3600, (self.counter / 60) % 60, self.counter % 60))
            self.timer2.start(1000)
            try:
                self.action = 'start_task'
                self.sendtomysql()
            except:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_5.setEnabled(False)
            self.ui.pushButton_6.setEnabled(False)
            self.ui.pushButton_7.setEnabled(False)
            self.ui.pushButton_8.setEnabled(False)
            self.ui.pushButton_9.setEnabled(False)
            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_11.setEnabled(False)
            self.ui.pushButton_12.setEnabled(False)
            self.ui.frame_2.setStyleSheet("background-color: rgb(200, 0, 0);")
        else:
            self.timer2.stop()
            self.taskcounter = self.counter
            self.action = 'stop_task'
            try:
                self.sendtomysql()
            except:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.counter = 0
            self.taskcounter = 0
            self.ui.label_2.clear()
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_5.setEnabled(True)
            self.ui.pushButton_6.setEnabled(True)
            self.ui.pushButton_7.setEnabled(True)
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_9.setEnabled(True)
            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_11.setEnabled(True)
            self.ui.pushButton_12.setEnabled(True)
            self.ui.frame_2.setStyleSheet("background-color: rgb(0, 200, 0);")

    def pushButton_11_clicked(self):
        self.text = 'ППР:'
        if self.counter == 0:
            self.ui.label_2.setText(self.text + " %02d:%02d:%02d" % (
                self.counter / 3600, (self.counter / 60) % 60, self.counter % 60))
            self.timer2.start(1000)
            try:
                self.action = 'start_ppr'
                self.sendtomysql()
            except:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_5.setEnabled(False)
            self.ui.pushButton_6.setEnabled(False)
            self.ui.pushButton_7.setEnabled(False)
            self.ui.pushButton_8.setEnabled(False)
            self.ui.pushButton_9.setEnabled(False)
            self.ui.pushButton_10.setEnabled(False)
            self.ui.pushButton_11.setEnabled(True)
            self.ui.pushButton_12.setEnabled(False)
            self.ui.frame_2.setStyleSheet("background-color: rgb(200, 0, 0);")
        else:
            self.timer2.stop()
            self.pprcounter = self.counter
            self.action = 'stop_ppr'
            try:
                self.sendtomysql()
            except:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.counter = 0
            self.pprcounter = 0
            self.ui.label_2.clear()
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_5.setEnabled(True)
            self.ui.pushButton_6.setEnabled(True)
            self.ui.pushButton_7.setEnabled(True)
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_9.setEnabled(True)
            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_11.setEnabled(True)
            self.ui.pushButton_12.setEnabled(True)
            self.ui.frame_2.setStyleSheet("background-color: rgb(0, 200, 0);")

    def pushButton_12_clicked(self):
        self.text = 'Изготовление макетов:'
        if self.counter == 0:
            self.ui.label_2.setText(self.text + " %02d:%02d:%02d" % (
                self.counter / 3600, (self.counter / 60) % 60, self.counter % 60))
            self.timer2.start(1000)
            try:
                self.action = 'start_model'
                self.sendtomysql()
            except:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_5.setEnabled(False)
            self.ui.pushButton_6.setEnabled(False)
            self.ui.pushButton_7.setEnabled(False)
            self.ui.pushButton_8.setEnabled(False)
            self.ui.pushButton_9.setEnabled(False)
            self.ui.pushButton_10.setEnabled(False)
            self.ui.pushButton_11.setEnabled(False)
            self.ui.pushButton_12.setEnabled(True)
            self.ui.frame_2.setStyleSheet("background-color: rgb(200, 0, 0);")
        else:
            self.timer2.stop()
            self.maketcounter = self.counter
            self.action = 'stop_model'
            try:
                self.sendtomysql()
            except:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.counter = 0
            self.maketcounter = 0
            self.ui.label_2.clear()
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_5.setEnabled(True)
            self.ui.pushButton_6.setEnabled(True)
            self.ui.pushButton_7.setEnabled(True)
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_9.setEnabled(True)
            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_11.setEnabled(True)
            self.ui.pushButton_12.setEnabled(True)
            self.ui.frame_2.setStyleSheet("background-color: rgb(0, 200, 0);")

    def sendtomysql(self):
        self.sql = 'INSERT INTO worktime (name, action, totaltime, plantime, setup, autoserv, ppr, break, material,' \
                   'task, maket, secs, minutes, hours, day, month, year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,' \
                   ' %s, %s, %s, %s, %s, %s, %s, %s)'
        self.val1 = 'Laser L77'
        self.val2 = self.action
        self.val3 = self.my_counter
        self.val4 = self.plancounter
        self.val5 = self.setupcounter
        self.val6 = self.autoservcounter
        self.val7 = self.pprcounter
        self.val8 = self.breakcounter
        self.val9 = self.matcounter
        self.val10 = self.taskcounter
        self.val11 = self.maketcounter
        self.val12 = datetime.datetime.strftime(datetime.datetime.now(), "%S")
        self.val13 = datetime.datetime.strftime(datetime.datetime.now(), "%M")
        self.val14 = datetime.datetime.strftime(datetime.datetime.now(), "%H")
        self.val15 = datetime.datetime.strftime(datetime.datetime.now(), "%d")
        self.val16 = datetime.datetime.strftime(datetime.datetime.now(), "%m")
        self.val17 = datetime.datetime.strftime(datetime.datetime.now(), "%Y")
        self.mycursor.execute(self.sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6,
                                         self.val7, self.val8, self.val9, self.val10, self.val11, self.val12,
                                         self.val13, self.val14, self.val15, self.val16, self.val17))
        self.connection.commit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
