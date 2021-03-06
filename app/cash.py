# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kasa.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import time

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from datetime import datetime


class Ui_MainWindow(object):
    last_id = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 1041, 581))
        self.tabWidget.setObjectName("tabWidget")
        self.kasa = QtWidgets.QWidget()
        self.kasa.setEnabled(True)
        self.kasa.setObjectName("kasa")
        self.pushButton_3 = QtWidgets.QPushButton(self.kasa)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 470, 121, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.kasa)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 470, 121, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.kasa)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 470, 121, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.kasa)
        self.label.setGeometry(QtCore.QRect(440, 490, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.kasa)
        self.label_2.setGeometry(QtCore.QRect(530, 490, 67, 17))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.kasa)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(10, 30, 191, 31))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.tabWidget.addTab(self.kasa, "")
        self.Orders = QtWidgets.QWidget()
        self.Orders.setObjectName("Orders")
        self.tableWidget = QtWidgets.QTableWidget(self.Orders)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 1021, 491))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.pushButton = QtWidgets.QPushButton(self.Orders)
        self.pushButton.setGeometry(QtCore.QRect(10, 500, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Orders)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 500, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.Orders)
        self.plainTextEdit.setGeometry(QtCore.QRect(130, 510, 191, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.Orders)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(460, 510, 191, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.tabWidget.addTab(self.Orders, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.loaddata()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "New Client"))
        self.pushButton_4.setText(_translate("MainWindow", "Payed"))
        self.pushButton_5.setText(_translate("MainWindow", "ADD Product"))
        self.label.setText(_translate("MainWindow", "Total Payed:"))
        self.label_2.setText(_translate("MainWindow", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.kasa), _translate("MainWindow", "Cash Register"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Full Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Phone "))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Order Created"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Order Updated"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Total Payed"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Order Key"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "StoreHouse"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Product"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton.clicked.connect(self.findbyname)
        self.pushButton_2.setText(_translate("MainWindow", "Order Complite"))
        self.pushButton_2.clicked.connect(self.Order_Complite)
        self.pushButton_3.clicked.connect(self.new_Client)
        self.pushButton_5.clicked.connect(self.add_product_in_carts)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Orders), _translate("MainWindow", "Orders"))

    def Order_Complite(self):
        id = self.plainTextEdit_2.toPlainText()
        db_connection = mysql.connector.connect(
            host="127.0.0.1",
            database='storebd',
            user="root",
            password="TheLastBit2303Yurik!",
            auth_plugin='mysql_native_password')
        db_cursor = db_connection.cursor(buffered=True)
        if db_connection.is_connected() == False:
            db_connection.connect()
        print("Updating")
        Update = f"UPDATE `storebd`.`orders_order` SET `billing_status` = '1' WHERE (`id` = '{id}');"
        db_cursor.execute(Update)
        db_connection.commit()
        self.loaddata()

    def loaddata(self):
        db_connection = mysql.connector.connect(
            host="127.0.0.1",
            database='storebd',
            user="root",
            password="TheLastBit2303Yurik!",
            auth_plugin='mysql_native_password')
        db_cursor = db_connection.cursor(buffered=True)
        if db_connection.is_connected() == False:
            db_connection.connect()
        sql = "SELECT * FROM orders_orderitem INNER JOIN orders_order ON " \
              "orders_orderitem.order_id = orders_order.id " \
              "INNER JOIN store_product ON orders_orderitem.product_id =  store_product.id " \
              "INNER JOIN storehouse_storehouse ON orders_order.Storehouse_id = storehouse_storehouse.id"
        db_cursor.execute(sql)
        total = db_cursor.rowcount
        print("Total Data Entries:" + str(total))
        db = db_cursor.fetchall()
        rows = 0
        self.tableWidget.setRowCount(len(db))
        for item in db:
            self.tableWidget.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(item[0])))
            self.tableWidget.setItem(rows, 1, QtWidgets.QTableWidgetItem(str(item[6])))
            self.tableWidget.setItem(rows, 2, QtWidgets.QTableWidgetItem(str(item[7])))
            self.tableWidget.setItem(rows, 3, QtWidgets.QTableWidgetItem(str(item[8])))
            self.tableWidget.setItem(rows, 4, QtWidgets.QTableWidgetItem(str(item[9])))
            self.tableWidget.setItem(rows, 5, QtWidgets.QTableWidgetItem(str(item[10])))
            self.tableWidget.setItem(rows, 6, QtWidgets.QTableWidgetItem(str(item[11])))
            self.tableWidget.setItem(rows, 7, QtWidgets.QTableWidgetItem(str(item[12])))
            self.tableWidget.setItem(rows, 8, QtWidgets.QTableWidgetItem(str(item[28])))
            self.tableWidget.setItem(rows, 9, QtWidgets.QTableWidgetItem(str(item[16])))
            rows += 1

    def findbyname(self):
        name = self.plainTextEdit.toPlainText()
        db_connection = mysql.connector.connect(
            host="127.0.0.1",
            database='storebd',
            user="root",
            password="TheLastBit2303Yurik!",
            auth_plugin='mysql_native_password')
        db_cursor = db_connection.cursor(buffered=True)
        if db_connection.is_connected() == False:
            db_connection.connect()
        sql = "SELECT * FROM orders_orderitem INNER JOIN orders_order ON " \
              "orders_orderitem.order_id = orders_order.id " \
              "INNER JOIN store_product ON orders_orderitem.product_id =  store_product.id " \
              "INNER JOIN storehouse_storehouse ON orders_order.Storehouse_id = storehouse_storehouse.id " \
              "where full_name='" + name + "'"
        db_cursor.execute(sql)
        total = db_cursor.rowcount
        print("Total Data Entries:" + str(total))
        db = db_cursor.fetchall()
        rows = 0
        self.tableWidget.setRowCount(len(db))
        for item in db:
            self.tableWidget.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(item[0])))
            self.tableWidget.setItem(rows, 1, QtWidgets.QTableWidgetItem(str(item[6])))
            self.tableWidget.setItem(rows, 2, QtWidgets.QTableWidgetItem(str(item[7])))
            self.tableWidget.setItem(rows, 3, QtWidgets.QTableWidgetItem(str(item[8])))
            self.tableWidget.setItem(rows, 4, QtWidgets.QTableWidgetItem(str(item[9])))
            self.tableWidget.setItem(rows, 5, QtWidgets.QTableWidgetItem(str(item[10])))
            self.tableWidget.setItem(rows, 6, QtWidgets.QTableWidgetItem(str(item[11])))
            self.tableWidget.setItem(rows, 7, QtWidgets.QTableWidgetItem(str(item[12])))
            self.tableWidget.setItem(rows, 8, QtWidgets.QTableWidgetItem(str(item[28])))
            self.tableWidget.setItem(rows, 9, QtWidgets.QTableWidgetItem(str(item[16])))
            rows += 1

    def new_Client(self):
        db_connection = mysql.connector.connect(
            host="127.0.0.1",
            database='storebd',
            user="root",
            password="TheLastBit2303Yurik!",
            auth_plugin='mysql_native_password')
        db_cursor = db_connection.cursor(buffered=True)
        if db_connection.is_connected() == False:
            db_connection.connect()
        sql = "SELECT * FROM storebd.orders_order;"
        db_cursor.execute(sql)
        total = db_cursor.rowcount
        print("Total Data Entries:" + str(total))
        db = db_cursor.fetchall()
        last_id = 0
        last_order_key = 0
        for item in db:
            last_id = item[0]
            last_order_key = item[6]
        last_id += 1
        last_order_key += "1"
        print("Create NEW CLIENT")
        create_order = f"INSERT INTO `storebd`.`orders_order` (`id`, `full_name`, `phone_numb`, `created`, " \
                       f"`updated`, `total_paid`, `order_key`, `billing_status`, `Storehouse_id`, `user_id`) " \
                       f"VALUES ('{last_id}', '????????????????', '0000', '{datetime.now()}', '{datetime.now()}', '0', " \
                       f"'{last_order_key}', '0', '1', '1');"
        db_cursor.execute(create_order)
        db_connection.commit()

    def add_product_in_carts(self):
        product_bar = self.plainTextEdit_3.toPlainText()
        db_connection = mysql.connector.connect(
            host="127.0.0.1",
            database='storebd',
            user="root",
            password="TheLastBit2303Yurik!",
            auth_plugin='mysql_native_password')
        db_cursor = db_connection.cursor(buffered=True)
        if db_connection.is_connected() == False:
            db_connection.connect()
        sql = "SELECT * FROM storebd.orders_order;"
        db_cursor.execute(sql)
        total = db_cursor.rowcount
        print("Total Data Entries:" + str(total))
        db = db_cursor.fetchall()
        last_id = 0
        last_paid = 0
        for item in db:
            last_id = item[0]
            last_paid = item[5]
        db_connection = mysql.connector.connect(
            host="127.0.0.1",
            database='storebd',
            user="root",
            password="TheLastBit2303Yurik!",
            auth_plugin='mysql_native_password')
        db_cursor = db_connection.cursor(buffered=True)
        if db_connection.is_connected() == False:
            db_connection.connect()
        sql = "SELECT * FROM store_product where barcode='" + product_bar + "'"
        db_cursor.execute(sql)
        total = db_cursor.rowcount
        print("Total Data Entries:" + str(total))
        db = db_cursor.fetchall()
        prod_id = 0
        prod_price = 0
        for item in db:
            prod_id = item[0]
            prod_price = item[5]

        sql = "SELECT * FROM storebd.orders_orderitem;"
        db_cursor.execute(sql)
        total = db_cursor.rowcount
        print("Total Data Entries:" + str(total))
        db = db_cursor.fetchall()
        id = 0
        for item in db:
            id = item[0]
        id += 1
        print(id, prod_price, "1", last_id, prod_id)
        add_cart = f"INSERT INTO `storebd`.`orders_orderitem` (`id`, `price`, `quantity`, `order_id`, `product_id`) VALUES ('{id}', '{prod_price}', '1', '{last_id}', '{prod_id}');"
        db_cursor.execute(add_cart)
        db_connection.commit()
        last_paid = last_paid + prod_price
        Update = f"UPDATE `storebd`.`orders_order` SET `total_paid` = '{last_paid}' WHERE (`id` = '{last_id}');"
        db_cursor.execute(Update)
        db_connection.commit()
        self.last_id = last_id
        self.label_2.setText(str(last_paid))
        self.pushButton_4.clicked.connect(self.payed)

    def payed(self):
        last_id = self.last_id
        db_connection = mysql.connector.connect(
            host="127.0.0.1",
            database='storebd',
            user="root",
            password="TheLastBit2303Yurik!",
            auth_plugin='mysql_native_password')
        db_cursor = db_connection.cursor(buffered=True)
        db_connection.connect()
        Update = f"UPDATE `storebd`.`orders_order` SET `billing_status` = '1' WHERE (`id` = '{last_id}');"
        db_cursor.execute(Update)
        db_connection.commit()
        print("PAYED COMPLITE")
        self.loaddata()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
