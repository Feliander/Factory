from PyQt5 import QtWidgets, QtCore
import datetime

def dat():
    StartTime = QtWidgets.QDateTimeEdit(widget)
    StartTime.setCalendarPopup(True)
    StartTime.setObjectName("StartTime")
    QtWidgets.gridLayout.addWidget(StartTime, 0, 0, 1, 3)
    StartTime.setDate(QtCore.QDate(datetime.now()-timedelta(days=7)))
    StartTime.setTime(QtCore.QTime.currentTime())

    dt = StartTime.dateTime()
    # dt.toString("dd.MM.yyyy hh:mm:ss.zzz"))
    dt_string = dt.toString(StartTime.displayFormat())
    print(dt_string)



