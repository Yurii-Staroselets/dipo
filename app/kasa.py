# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kasa.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.order_table = QtWidgets.QTableView(self.centralwidget)
        self.order_table.setGeometry(QtCore.QRect(0, 10, 781, 431))
        self.order_table.setObjectName("order_table")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 460, 89, 25))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menukasa = QtWidgets.QMenu(self.menubar)
        self.menukasa.setObjectName("menukasa")
        self.menukasa_2 = QtWidgets.QMenu(self.menubar)
        self.menukasa_2.setObjectName("menukasa_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menukasa.menuAction())
        self.menubar.addAction(self.menukasa_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "connect"))
        self.pushButton.clicked.connect(self.connect_to_bd)
        self.menukasa.setTitle(_translate("MainWindow", "order"))
        self.menukasa_2.setTitle(_translate("MainWindow", "kasa"))

    def connect_to_bd(self):
        db_connection = mysql.connector.connect(
            host="127.0.0.1",
            database='storebd',
            user="root",
            password="TheLastBit2303Yurik!",
            auth_plugin='mysql_native_password')
        db_cursor = db_connection.cursor(buffered=True)
        if db_connection.is_connected() == False:
            db_connection.connect()
        sql = "SELECT * FROM orders_order"
        db_cursor.execute(sql)
        total = db_cursor.rowcount
        print("Total Data Entries:" + str(total))
        rows = db_cursor.fetchall()
        for row in rows:
            self.order_table.showRow(1)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
