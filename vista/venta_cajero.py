# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

class Ui_Form(object):

	def setupUi(self, Form):
		Form.setObjectName("Cajero - Ventas de Productos")
		Form.resize(921, 583)

		self.lineEdit = QtGui.QLineEdit(Form)
		self.lineEdit.setGeometry(QtCore.QRect(90, 90, 281, 21))
		self.lineEdit.setObjectName("lineEdit")

		self.pushButton = QtGui.QPushButton(Form)
		self.pushButton.setGeometry(QtCore.QRect(730, 170, 51, 51))
		self.pushButton.setObjectName("pushButton")

		self.pushButton_2 = QtGui.QPushButton(Form)
		self.pushButton_2.setGeometry(QtCore.QRect(730, 350, 101, 51))
		self.pushButton_2.setObjectName("pushButton_2")

		self.pushButton_3 = QtGui.QPushButton(Form)
		self.pushButton_3.setGeometry(QtCore.QRect(850, 350, 51, 51))
		self.pushButton_3.setObjectName("pushButton_3")

		self.pushButton_4 = QtGui.QPushButton(Form)
		self.pushButton_4.setGeometry(QtCore.QRect(850, 290, 51, 51))
		self.pushButton_4.setObjectName("pushButton_4")

		self.pushButton_5 = QtGui.QPushButton(Form)
		self.pushButton_5.setGeometry(QtCore.QRect(790, 290, 51, 51))
		self.pushButton_5.setObjectName("pushButton_5")

		self.pushButton_6 = QtGui.QPushButton(Form)
		self.pushButton_6.setGeometry(QtCore.QRect(730, 290, 51, 51))
		self.pushButton_6.setObjectName("pushButton_6")

		self.pushButton_7 = QtGui.QPushButton(Form)
		self.pushButton_7.setGeometry(QtCore.QRect(850, 230, 51, 51))
		self.pushButton_7.setObjectName("pushButton_7")

		self.pushButton_8 = QtGui.QPushButton(Form)
		self.pushButton_8.setGeometry(QtCore.QRect(790, 230, 51, 51))
		self.pushButton_8.setObjectName("pushButton_8")

		self.pushButton_9 = QtGui.QPushButton(Form)
		self.pushButton_9.setGeometry(QtCore.QRect(730, 230, 51, 51))
		self.pushButton_9.setObjectName("pushButton_9")

		self.pushButton_10 = QtGui.QPushButton(Form)
		self.pushButton_10.setGeometry(QtCore.QRect(850, 170, 51, 51))
		self.pushButton_10.setObjectName("pushButton_10")

		self.pushButton_11 = QtGui.QPushButton(Form)
		self.pushButton_11.setGeometry(QtCore.QRect(790, 170, 51, 51))
		self.pushButton_11.setObjectName("pushButton_11")

		self.lineEdit_2 = QtGui.QLineEdit(Form)
		self.lineEdit_2.setGeometry(QtCore.QRect(30, 190, 61, 27))
		self.lineEdit_2.setText("")
		self.lineEdit_2.setObjectName("lineEdit_2")

		self.label = QtGui.QLabel(Form)
		self.label.setGeometry(QtCore.QRect(260, 10, 21, 17))
		self.label.setObjectName("label")

		self.pushButton_12 = QtGui.QPushButton(Form)
		self.pushButton_12.setGeometry(QtCore.QRect(560, 10, 101, 27))
		self.pushButton_12.setObjectName("pushButton_12")

		self.label_2 = QtGui.QLabel(Form)
		self.label_2.setGeometry(QtCore.QRect(190, 10, 66, 17))
		self.label_2.setObjectName("label_2")

		self.label_3 = QtGui.QLabel(Form)
		self.label_3.setGeometry(QtCore.QRect(720, 90, 61, 20))
		self.label_3.setObjectName("label_3")

		self.label_4 = QtGui.QLabel(Form)
		self.label_4.setGeometry(QtCore.QRect(290, 10, 31, 20))
		self.label_4.setObjectName("label_4")

		self.label_5 = QtGui.QLabel(Form)
		self.label_5.setGeometry(QtCore.QRect(330, 10, 41, 20))
		self.label_5.setObjectName("label_5")

		self.label_6 = QtGui.QLabel(Form)
		self.label_6.setGeometry(QtCore.QRect(410, 10, 51, 21))
		self.label_6.setObjectName("label_6")

		self.label_7 = QtGui.QLabel(Form)
		self.label_7.setGeometry(QtCore.QRect(480, 10, 51, 21))
		self.label_7.setObjectName("label_7")

		self.label_8 = QtGui.QLabel(Form)
		self.label_8.setGeometry(QtCore.QRect(30, 90, 61, 20))
		self.label_8.setObjectName("label_8")

		self.label_9 = QtGui.QLabel(Form)
		self.label_9.setGeometry(QtCore.QRect(550, 90, 41, 20))
		self.label_9.setObjectName("label_9")

		self.lineEdit_3 = QtGui.QLineEdit(Form)
		self.lineEdit_3.setGeometry(QtCore.QRect(590, 90, 113, 21))
		self.lineEdit_3.setObjectName("lineEdit_3")

		self.label_10 = QtGui.QLabel(Form)
		self.label_10.setGeometry(QtCore.QRect(30, 60, 51, 20))
		self.label_10.setObjectName("label_10")

		self.lineEdit_4 = QtGui.QLineEdit(Form)
		self.lineEdit_4.setGeometry(QtCore.QRect(780, 90, 113, 21))
		self.lineEdit_4.setObjectName("lineEdit_4")

		self.label_11 = QtGui.QLabel(Form)
		self.label_11.setGeometry(QtCore.QRect(390, 90, 31, 20))
		self.label_11.setObjectName("label_11")

		self.lineEdit_5 = QtGui.QLineEdit(Form)
		self.lineEdit_5.setGeometry(QtCore.QRect(420, 90, 113, 21))
		self.lineEdit_5.setObjectName("lineEdit_5")

		self.verticalLayoutWidget_2 = QtGui.QWidget(Form)
		self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 60, 891, 21))
		self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

		self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
		self.verticalLayout_2.setMargin(0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")

		self.label_12 = QtGui.QLabel(Form)
		self.label_12.setGeometry(QtCore.QRect(30, 130, 71, 17))
		self.label_12.setObjectName("label_12")

		self.label_13 = QtGui.QLabel(Form)
		self.label_13.setGeometry(QtCore.QRect(640, 160, 71, 17))
		self.label_13.setObjectName("label_13")

		self.label_14 = QtGui.QLabel(Form)
		self.label_14.setGeometry(QtCore.QRect(220, 160, 91, 17))
		self.label_14.setObjectName("label_14")

		self.label_15 = QtGui.QLabel(Form)
		self.label_15.setGeometry(QtCore.QRect(30, 160, 71, 17))
		self.label_15.setObjectName("label_15")

		self.label_16 = QtGui.QLabel(Form)
		self.label_16.setGeometry(QtCore.QRect(530, 160, 71, 17))
		self.label_16.setObjectName("label_16")

		self.label_17 = QtGui.QLabel(Form)
		self.label_17.setGeometry(QtCore.QRect(100, 160, 71, 17))
		self.label_17.setObjectName("label_17")

		self.label_18 = QtGui.QLabel(Form)
		self.label_18.setGeometry(QtCore.QRect(400, 160, 71, 17))
		self.label_18.setObjectName("label_18")

		self.verticalLayoutWidget_4 = QtGui.QWidget(Form)
		self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 130, 891, 21))
		self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")

		self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
		self.verticalLayout_4.setMargin(0)
		self.verticalLayout_4.setObjectName("verticalLayout_4")

		self.lineEdit_6 = QtGui.QLineEdit(Form)
		self.lineEdit_6.setGeometry(QtCore.QRect(400, 190, 113, 27))
		self.lineEdit_6.setText("")
		self.lineEdit_6.setObjectName("lineEdit_6")

		self.lineEdit_7 = QtGui.QLineEdit(Form)
		self.lineEdit_7.setGeometry(QtCore.QRect(220, 190, 171, 27))
		self.lineEdit_7.setText("")
		self.lineEdit_7.setObjectName("lineEdit_7")

		self.lineEdit_8 = QtGui.QLineEdit(Form)
		self.lineEdit_8.setGeometry(QtCore.QRect(100, 190, 111, 27))
		self.lineEdit_8.setText("")
		self.lineEdit_8.setObjectName("lineEdit_8")

		self.lineEdit_9 = QtGui.QLineEdit(Form)
		self.lineEdit_9.setGeometry(QtCore.QRect(640, 190, 61, 27))
		self.lineEdit_9.setText("")
		self.lineEdit_9.setObjectName("lineEdit_9")

		self.label_19 = QtGui.QLabel(Form)
		self.label_19.setGeometry(QtCore.QRect(730, 450, 91, 17))
		self.label_19.setObjectName("label_19")

		self.lineEdit_10 = QtGui.QLineEdit(Form)
		self.lineEdit_10.setGeometry(QtCore.QRect(530, 190, 91, 27))
		self.lineEdit_10.setText("")
		self.lineEdit_10.setObjectName("lineEdit_10")

		self.pushButton_13 = QtGui.QPushButton(Form)
		self.pushButton_13.setGeometry(QtCore.QRect(540, 230, 151, 31))
		self.pushButton_13.setObjectName("pushButton_13")

		self.gridLayoutWidget_2 = QtGui.QWidget(Form)
		self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 160, 691, 21))
		self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

		self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
		self.gridLayout_2.setMargin(0)
		self.gridLayout_2.setObjectName("gridLayout_2")

		self.tableWidget = QtGui.QTableWidget(Form)
		self.tableWidget.setGeometry(QtCore.QRect(20, 280, 691, 281))
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setColumnCount(6)
		self.tableWidget.setRowCount(8)

		item = QtGui.QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(0, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(1, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(2, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(3, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(4, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(5, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(6, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(7, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(0, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(1, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(2, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(3, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(4, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(5, item)
		
		self.pushButton_14 = QtGui.QPushButton(Form)
		self.pushButton_14.setGeometry(QtCore.QRect(730, 500, 171, 41))
		self.pushButton_14.setObjectName("pushButton_14")

		self.label_20 = QtGui.QLabel(Form)
		self.label_20.setGeometry(QtCore.QRect(820, 450, 71, 17))
		self.label_20.setObjectName("label_20")

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle("Cajero - Ventas de Productos")
		self.pushButton.setText("1")
		self.pushButton_2.setText("0")
		self.pushButton_3.setText(".")
		self.pushButton_4.setText("9")
		self.pushButton_5.setText("8")
		self.pushButton_6.setText("7")
		self.pushButton_7.setText("6")
		self.pushButton_8.setText("5")
		self.pushButton_9.setText("4")
		self.pushButton_10.setText("3")
		self.pushButton_11.setText("2")
		self.label.setText("14 ")
		self.pushButton_12.setText("cerrar sesion")
		self.label_2.setText("Domingo")
		self.label_3.setText("Telefono")
		self.label_4.setText("Abril")
		self.label_5.setText("2014")
		self.label_6.setText("cajero : ")
		self.label_7.setText("Jordan")
		self.label_8.setText("Nombre")
		self.label_9.setText("Email")
		self.label_10.setText("Cliente")
		self.label_11.setText("RUC")
		self.label_12.setText("Productos")
		self.label_13.setText("Total")
		self.label_14.setText("Descripción")
		self.label_15.setText("cantidad")
		self.label_16.setText("precio")
		self.label_17.setText("Nombre")
		self.label_18.setText("codigo")
		self.label_19.setText("Total Neto:")
		self.pushButton_13.setText("Agregar Producto")

		item = self.tableWidget.verticalHeaderItem(0)
		item.setText("1")
		item = self.tableWidget.verticalHeaderItem(1)
		item.setText("2")
		item = self.tableWidget.verticalHeaderItem(2)
		item.setText("3")
		item = self.tableWidget.verticalHeaderItem(3)
		item.setText("4")
		item = self.tableWidget.verticalHeaderItem(4)
		item.setText("5")
		item = self.tableWidget.verticalHeaderItem(5)
		item.setText("6")
		item = self.tableWidget.verticalHeaderItem(6)
		item.setText("7")
		item = self.tableWidget.verticalHeaderItem(7)
		item.setText("8")
		item = self.tableWidget.horizontalHeaderItem(0)
		item.setText("codigo")
		item = self.tableWidget.horizontalHeaderItem(1)
		item.setText("descripcion")
		item = self.tableWidget.horizontalHeaderItem(2)
		item.setText("nombre")
		item = self.tableWidget.horizontalHeaderItem(3)
		item.setText("cantidad")
		item = self.tableWidget.horizontalHeaderItem(4)
		item.setText("precio")
		item = self.tableWidget.horizontalHeaderItem(5)
		item.setText("total")
		self.pushButton_14.setText("Imprimir Boleta")
		self.label_20.setText("150")


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Form = QtGui.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())

