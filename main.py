import sys
import datetime
import pymysql
from PyQt5 import QtWidgets, QtCore
from MyGUI import Ui_MainWindow


class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.start_button)
        self.ui.pushButton_4.clicked.connect(self.stop_button)
        self.ui.pushButton_5.clicked.connect(self.plan_button)
        self.ui.pushButton_6.clicked.connect(self.setup_button)
        self.ui.pushButton_7.clicked.connect(self.auto_serv_button)
        self.ui.pushButton_8.clicked.connect(self.breaking_button)
        self.ui.pushButton_9.clicked.connect(self.material_button)
        self.ui.pushButton_10.clicked.connect(self.task_button)
        self.ui.pushButton_11.clicked.connect(self.ppr_button)
        self.ui.pushButton_12.clicked.connect(self.model_button)
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
        self.cursor = self.connection.cursor()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer2 = QtCore.QTimer(self)
        self.timer2.timeout.connect(self.update_timer_2)
        self.secondary_counter = 0
        self.main_counter = 0
        self.plan_counter = 0
        self.setup_counter = 0
        self.auto_serv_counter = 0
        self.ppr_counter = 0
        self.break_counter = 0
        self.material_counter = 0
        self.task_counter = 0
        self.model_counter = 0

    def start_button(self):
        self.main_counter = 0
        self.ui.label.setText("Рабочая смена:" + " %02d:%02d:%02d" % (
            self.main_counter / 3600, (self.main_counter / 60) % 60, self.main_counter % 60))
        self.timer.start(1000)
        try:
            action = 'start'
            self.sending_to_mysql(action)
        except pymysql.err.ProgrammingError:
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

    def update_timer(self):
        self.main_counter += 1
        if self.main_counter >= 0:
            self.ui.label.setText("Рабочая смена:" + " %02d:%02d:%02d" % (
                self.main_counter / 3600, (self.main_counter / 60) % 60, self.main_counter % 60))
        else:
            self.timer.stop()

    def stop_button(self):
        self.timer.stop()
        self.timer2.stop()
        self.ui.label_2.clear()
        self.ui.label_3.clear()
        try:
            action = 'stop'
            self.sending_to_mysql(action)
        except pymysql.err.ProgrammingError:
            QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
        self.secondary_counter = 0
        self.main_counter = 0
        self.plan_counter = 0
        self.setup_counter = 0
        self.auto_serv_counter = 0
        self.ppr_counter = 0
        self.break_counter = 0
        self.material_counter = 0
        self.task_counter = 0
        self.model_counter = 0
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

    def plan_button(self):
        text = 'Плановый перерыв:'
        if self.secondary_counter == 0:
            self.ui.label_2.setText(text)
            self.ui.label_3.setText(" %02d:%02d:%02d" % (
                self.secondary_counter / 3600, (self.secondary_counter / 60) % 60, self.secondary_counter % 60))
            self.timer2.start(1000)
            try:
                action = 'start_plan_counter'
                self.sending_to_mysql(action)
            except pymysql.err.ProgrammingError:
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
            self.plan_counter = self.secondary_counter
            action = 'stop_plan_counter'
            try:
                self.sending_to_mysql(action)
            except pymysql.err.ProgrammingError:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.secondary_counter = 0
            self.plan_counter = 0
            self.ui.label_2.clear()
            self.ui.label_3.clear()
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

    def update_timer_2(self):
        self.secondary_counter += 1
        if self.secondary_counter >= 0:
            self.ui.label_3.setText(" %02d:%02d:%02d" % (
                self.secondary_counter / 3600, (self.secondary_counter / 60) % 60, self.secondary_counter % 60))
        else:
            self.timer2.stop()

    def setup_button(self):
        text = 'Переналадка, перенастройка:'
        if self.secondary_counter == 0:
            self.ui.label_2.setText(text)
            self.ui.label_3.setText(" %02d:%02d:%02d" % (
                self.secondary_counter / 3600, (self.secondary_counter / 60) % 60, self.secondary_counter % 60))
            self.timer2.start(1000)
            try:
                action = 'start_setup'
                self.sending_to_mysql(action)
            except pymysql.err.ProgrammingError:
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
            self.setup_counter = self.secondary_counter
            action = 'stop_setup'
            try:
                self.sending_to_mysql(action)
            except pymysql.err.ProgrammingError:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.secondary_counter = 0
            self.setup_counter = 0
            self.ui.label_2.clear()
            self.ui.label_3.clear()
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

    def auto_serv_button(self):
        text = 'Автономное обслуживание:'
        if self.secondary_counter == 0:
            self.ui.label_2.setText(text)
            self.ui.label_3.setText(" %02d:%02d:%02d" % (
                self.secondary_counter / 3600, (self.secondary_counter / 60) % 60, self.secondary_counter % 60))
            self.timer2.start(1000)
            try:
                action = 'start_auto_service'
                self.sending_to_mysql(action)
            except pymysql.err.ProgrammingError:
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
            self.auto_serv_counter = self.secondary_counter
            action = 'stop_auto_service'
            try:
                self.sending_to_mysql(action)
            except pymysql.err.ProgrammingError:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.secondary_counter = 0
            self.auto_serv_counter = 0
            self.ui.label_2.clear()
            self.ui.label_3.clear()
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

    def breaking_button(self):
        text = 'Поломка оборудования:'
        if self.secondary_counter == 0:
            self.ui.label_2.setText(text)
            self.ui.label_3.setText(" %02d:%02d:%02d" % (
                self.secondary_counter / 3600, (self.secondary_counter / 60) % 60, self.secondary_counter % 60))
            self.timer2.start(1000)
            try:
                action = 'start_break'
                self.sending_to_mysql(action)
            except pymysql.err.ProgrammingError:
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
            self.break_counter = self.secondary_counter
            action = 'stop_break'
            try:
                self.sending_to_mysql(action)
            except pymysql.err.ProgrammingError:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.secondary_counter = 0
            self.break_counter = 0
            self.ui.label_2.clear()
            self.ui.label_3.clear()
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

    def material_button(self):
        text = 'Отсутствие материалов:'
        if self.secondary_counter == 0:
            self.ui.label_2.setText(text)
            self.ui.label_3.setText(" %02d:%02d:%02d" % (
                self.secondary_counter / 3600, (self.secondary_counter / 60) % 60, self.secondary_counter % 60))
            self.timer2.start(1000)
            try:
                action = 'start_material'
                self.sending_to_mysql(action)
            except pymysql.err.ProgrammingError:
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
            self.material_counter = self.secondary_counter
            action = 'stop_material'
            try:
                self.sending_to_mysql(action)
            except pymysql.err.ProgrammingError:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.secondary_counter = 0
            self.material_counter = 0
            self.ui.label_2.clear()
            self.ui.label_3.clear()
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

    def task_button(self):
        text = 'Отсутствие задания:'
        if self.secondary_counter == 0:
            self.ui.label_2.setText(text)
            self.ui.label_3.setText(" %02d:%02d:%02d" % (
                self.secondary_counter / 3600, (self.secondary_counter / 60) % 60, self.secondary_counter % 60))
            self.timer2.start(1000)
            try:
                action = 'start_task'
                self.sending_to_mysql(action)
            except pymysql.err.ProgrammingError:
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
            self.task_counter = self.secondary_counter
            action = 'stop_task'
            try:
                self.sending_to_mysql(action)
            except pymysql.err.ProgrammingError:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.secondary_counter = 0
            self.task_counter = 0
            self.ui.label_2.clear()
            self.ui.label_3.clear()
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

    def ppr_button(self):
        text = 'ППР:'
        if self.secondary_counter == 0:
            self.ui.label_2.setText(text)
            self.ui.label_3.setText(" %02d:%02d:%02d" % (
                self.secondary_counter / 3600, (self.secondary_counter / 60) % 60, self.secondary_counter % 60))
            self.timer2.start(1000)
            try:
                action = 'start_ppr'
                self.sending_to_mysql(action)
            except pymysql.err.ProgrammingError:
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
            self.ppr_counter = self.secondary_counter
            action = 'stop_ppr'
            try:
                self.sending_to_mysql(action)
            except pymysql.err.ProgrammingError:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.secondary_counter = 0
            self.ppr_counter = 0
            self.ui.label_2.clear()
            self.ui.label_3.clear()
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

    def model_button(self):
        text = 'Изготовление макетов:'
        if self.secondary_counter == 0:
            self.ui.label_2.setText(text)
            self.ui.label_3.setText(" %02d:%02d:%02d" % (
                self.secondary_counter / 3600, (self.secondary_counter / 60) % 60, self.secondary_counter % 60))
            self.timer2.start(1000)
            try:
                action = 'start_model'
                self.sending_to_mysql(action)
            except pymysql.err.ProgrammingError:
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
            self.model_counter = self.secondary_counter
            action = 'stop_model'
            try:
                self.sending_to_mysql(action)
            except pymysql.err.ProgrammingError:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.secondary_counter = 0
            self.model_counter = 0
            self.ui.label_2.clear()
            self.ui.label_3.clear()
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

    def sending_to_mysql(self, action):
        sql = 'INSERT INTO worktime (name, action, totaltime, plantime, setup, autoserv, ppr, break, material,' \
                   'task, maket, secs, minutes, hours, day, month, year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,' \
                   ' %s, %s, %s, %s, %s, %s, %s, %s)'
        val1 = 'Laser1'
        val2 = action
        val3 = self.main_counter
        val4 = self.plan_counter
        val5 = self.setup_counter
        val6 = self.auto_serv_counter
        val7 = self.ppr_counter
        val8 = self.break_counter
        val9 = self.material_counter
        val10 = self.task_counter
        val11 = self.model_counter
        val12 = datetime.datetime.strftime(datetime.datetime.now(), "%S")
        val13 = datetime.datetime.strftime(datetime.datetime.now(), "%M")
        val14 = datetime.datetime.strftime(datetime.datetime.now(), "%H")
        val15 = datetime.datetime.strftime(datetime.datetime.now(), "%d")
        val16 = datetime.datetime.strftime(datetime.datetime.now(), "%m")
        val17 = datetime.datetime.strftime(datetime.datetime.now(), "%Y")
        self.cursor.execute(sql, (val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12, val13,
                                  val14, val15, val16, val17))
        self.connection.commit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
