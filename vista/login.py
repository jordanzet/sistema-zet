# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui


class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(320, 240)
		self.buttonBox = QtGui.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(-310, 200, 621, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.pushButton = QtGui.QPushButton(Dialog)
		self.pushButton.setGeometry(QtCore.QRect(80, 30, 141, 27))
		self.pushButton.setObjectName("pushButton")
		self.pushButton_2 = QtGui.QPushButton(Dialog)
		self.pushButton_2.setGeometry(QtCore.QRect(80, 150, 141, 27))
		self.pushButton_2.setObjectName("pushButton_2")
		self.pushButton_3 = QtGui.QPushButton(Dialog)
		self.pushButton_3.setGeometry(QtCore.QRect(80, 90, 141, 27))
		self.pushButton_3.setObjectName("pushButton_3")

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle("Sistema Zet")
		self.pushButton.setText("Administrador")
		self.pushButton_2.setText("Cajero")
		self.pushButton_3.setText("Jefe de Inventario")


def loginuser():
	import sys
	app = QtGui.QApplication(sys.argv)
	Dialog = QtGui.QDialog()
	ui = Ui_Dialog()
	ui.setupUi(Dialog)
	Dialog.show()
	sys.exit(app.exec_())