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
        self.set_enabled_false()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer2 = QtCore.QTimer(self)
        self.timer2.timeout.connect(self.update_timer_2)
        try:
            self.connection = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                db='mydb',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.connection.cursor()
        except pymysql.err.OperationalError:
            QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
        self.secondary_counter = 0
        self.main_counter = 0

    def set_enabled_false(self):
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_5.setEnabled(False)
        self.ui.pushButton_6.setEnabled(False)
        self.ui.pushButton_7.setEnabled(False)
        self.ui.pushButton_8.setEnabled(False)
        self.ui.pushButton_9.setEnabled(False)
        self.ui.pushButton_10.setEnabled(False)
        self.ui.pushButton_11.setEnabled(False)
        self.ui.pushButton_12.setEnabled(False)

    def set_enabled_true(self):
        self.ui.pushButton_4.setEnabled(True)
        self.ui.pushButton_5.setEnabled(True)
        self.ui.pushButton_6.setEnabled(True)
        self.ui.pushButton_7.setEnabled(True)
        self.ui.pushButton_8.setEnabled(True)
        self.ui.pushButton_9.setEnabled(True)
        self.ui.pushButton_10.setEnabled(True)
        self.ui.pushButton_11.setEnabled(True)
        self.ui.pushButton_12.setEnabled(True)

    def update_timer(self):
        self.main_counter += 1
        if self.main_counter >= 0:
            self.ui.label.setText("Рабочая смена:" + " %02d:%02d:%02d" % (
                self.main_counter / 3600, (self.main_counter / 60) % 60, self.main_counter % 60))
        else:
            self.timer.stop()

    def update_timer_2(self):
        self.secondary_counter += 1
        if self.secondary_counter >= 0:
            self.ui.label_3.setText("%02d:%02d:%02d" % (
                self.secondary_counter / 3600, (self.secondary_counter / 60) % 60, self.secondary_counter % 60))
        else:
            self.timer2.stop()

    def sending_to_mysql(self, action, plan=0, setup=0, auto_serv=0, ppr=0, breaking=0, material=0,
                         task=0, model=0):
        sql = "INSERT INTO worktime (name, action, totaltime, plantime, setup, autoserv, ppr, break, material," \
              "task, maket, secs, minutes, hours, day, month, year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s," \
              " %s, %s, %s, %s, %s, %s, %s, %s)"
        val1 = 'Laser1'
        val2 = action
        val3 = self.main_counter
        val4 = plan
        val5 = setup
        val6 = auto_serv
        val7 = ppr
        val8 = breaking
        val9 = material
        val10 = task
        val11 = model
        val12 = datetime.datetime.strftime(datetime.datetime.now(), "%S")
        val13 = datetime.datetime.strftime(datetime.datetime.now(), "%M")
        val14 = datetime.datetime.strftime(datetime.datetime.now(), "%H")
        val15 = datetime.datetime.strftime(datetime.datetime.now(), "%d")
        val16 = datetime.datetime.strftime(datetime.datetime.now(), "%m")
        val17 = datetime.datetime.strftime(datetime.datetime.now(), "%Y")
        try:
            self.cursor.execute(sql, (val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12, val13,
                                      val14, val15, val16, val17))
            self.connection.commit()
        except AttributeError:
            QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')

    def start_button(self):
        self.ui.label.setText("Рабочая смена:" + " %02d:%02d:%02d" % (
            self.main_counter / 3600, (self.main_counter / 60) % 60, self.main_counter % 60))
        self.timer.start(1000)
        try:
            self.sending_to_mysql(action='start')
        except pymysql.err.ProgrammingError:
            QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
        self.ui.pushButton_3.setEnabled(False)
        self.set_enabled_true()
        self.ui.frame_2.setStyleSheet("background-color: rgb(0, 200, 0);")

    def stop_button(self):
        self.timer.stop()
        self.timer2.stop()
        self.ui.label_2.clear()
        self.ui.label_3.clear()
        try:
            self.sending_to_mysql(action='stop')
        except pymysql.err.ProgrammingError:
            QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
        self.secondary_counter = 0
        self.main_counter = 0
        self.ui.pushButton_3.setEnabled(True)
        self.set_enabled_false()
        self.ui.frame_2.setStyleSheet("background-color: rgb(255, 255, 0);")

    def template_button(self, text, action1):
        if self.secondary_counter == 0:
            self.ui.label_2.setText(text)
            self.ui.label_3.setText("%02d:%02d:%02d" % (
                self.secondary_counter / 3600, (self.secondary_counter / 60) % 60, self.secondary_counter % 60))
            self.timer2.start(1000)
            try:
                self.sending_to_mysql(action1)
            except pymysql.err.ProgrammingError:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.set_enabled_false()
            self.ui.frame_2.setStyleSheet("background-color: rgb(200, 0, 0);")
        else:
            self.timer2.stop()
            self.ui.label_2.clear()
            self.ui.label_3.clear()
            self.set_enabled_true()
            self.ui.frame_2.setStyleSheet("background-color: rgb(0, 200, 0);")

    def plan_button(self):
        self.template_button('Плановый перерыв:', 'start_plan_counter')
        self.ui.pushButton_5.setEnabled(True)
        if self.secondary_counter > 0:
            try:
                self.sending_to_mysql('stop_plan_counter', plan=self.secondary_counter)
            except pymysql.err.ProgrammingError:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.secondary_counter = 0

    def setup_button(self):
        self.template_button('Переналадка, перенастройка:', 'start_setup')
        self.ui.pushButton_6.setEnabled(True)
        if self.secondary_counter > 0:
            try:
                self.sending_to_mysql('stop_setup', setup=self.secondary_counter)
            except pymysql.err.ProgrammingError:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.secondary_counter = 0

    def auto_serv_button(self):
        self.template_button('Автономное обслуживание:', 'start_auto_service')
        self.ui.pushButton_7.setEnabled(True)
        if self.secondary_counter > 0:
            try:
                self.sending_to_mysql('stop_auto_service', auto_serv=self.secondary_counter)
            except pymysql.err.ProgrammingError:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.secondary_counter = 0

    def breaking_button(self):
        self.template_button('Поломка оборудования:', 'start_break')
        self.ui.pushButton_8.setEnabled(True)
        if self.secondary_counter > 0:
            try:
                self.sending_to_mysql('stop_break', breaking=self.secondary_counter)
            except pymysql.err.ProgrammingError:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.secondary_counter = 0

    def material_button(self):
        self.template_button('Отсутствие материалов:', 'start_material')
        self.ui.pushButton_9.setEnabled(True)
        if self.secondary_counter > 0:
            try:
                self.sending_to_mysql('stop_material', material=self.secondary_counter)
            except pymysql.err.ProgrammingError:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.secondary_counter = 0

    def task_button(self):
        self.template_button('Отсутствие задания:', 'start_task')
        self.ui.pushButton_10.setEnabled(True)
        if self.secondary_counter > 0:
            try:
                self.sending_to_mysql('stop_task', task=self.secondary_counter)
            except pymysql.err.ProgrammingError:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.secondary_counter = 0

    def ppr_button(self):
        self.template_button('ППР:', 'start_ppr')
        self.ui.pushButton_11.setEnabled(True)
        if self.secondary_counter > 0:
            try:
                self.sending_to_mysql('stop_ppr', ppr=self.secondary_counter)
            except pymysql.err.ProgrammingError:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.secondary_counter = 0

    def model_button(self):
        self.template_button('Изготовление макетов:', 'start_model')
        self.ui.pushButton_12.setEnabled(True)
        if self.secondary_counter > 0:
            try:
                self.sending_to_mysql('stop_model', model=self.secondary_counter)
            except pymysql.err.ProgrammingError:
                QtWidgets.QMessageBox.information(None, 'Message', 'MySQL server connection isn\'t exist!')
            self.secondary_counter = 0


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
