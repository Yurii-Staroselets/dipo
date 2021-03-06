# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(342, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 60, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 91, 17))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 80, 261, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(40, 150, 261, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 220, 181, 71))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "LOGIN"))
        self.label_2.setText(_translate("MainWindow", "PASSWORD"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton.clicked.connect(self.login)

    def login(self):
        login = self.plainTextEdit.toPlainText()
        password = self.plainTextEdit_2.toPlainText()
        db_connection = mysql.connector.connect(
            host="127.0.0.1",
            database='storebd',
            user="root",
            password="TheLastBit2303Yurik!",
            auth_plugin='mysql_native_password')
        db_cursor = db_connection.cursor(buffered=True)
        if db_connection.is_connected() == False:
            db_connection.connect()
        sql = "SELECT * FROM worker_worker INNER JOIN storehouse_storehouse ON " \
              "worker_worker.storehouse_id = storehouse_storehouse.id "
        db_cursor.execute(sql)
        total = db_cursor.rowcount
        print("Total Data Entries:" + str(total))
        db = db_cursor.fetchall()
        rows = 0
        for item in db:
            if item[3] == login:
                if item[4] == password:
                    if item[5] == 1 and item[6] != 1:
                        exec(open('cash.py').read())
                        os.system('python cash.py')
                    if item[5] != 1 and item[6] == 1:
                        exec(open('manager.py').read())
                        os.system('python manager.py')
                    if item[5] == 1 and item[6] == 1:
                        print("SuperUSER")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
