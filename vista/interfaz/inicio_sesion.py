# -*- coding: utf-8 -*-

from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QHBoxLayout
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QGridLayout
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QApplication

import sys


class InicioSesion(QDialog):

	def __init__(self, parent=None):
		super(InicioSesion, self).__init__(parent)

		self.setWindowTitle("Bienvenido a la Empresa Zet ")
		self.resize(300,400)

		layout_vertical = QVBoxLayout()

		#Labels y LineEdits en donde se ingresan los datos
		self.usuario_lbl = QLabel("<b>USUARIO   </b>")
		self.usuario_edit = QLineEdit()
		cod = "Ingresa tu Usuario"
		self.usuario_edit.setPlaceholderText(cod)

		self.password_lbl = QLabel("<b>PASSWORD </b>")
		self.password_edit = QLineEdit()
		pre = "Ingres tu Password"
		self.password_edit.setPlaceholderText(pre)

		#BOTONES
		self.boton_aceptar = QPushButton("aceptar")
		self.boton_aceptar.setToolTip("Iniciar Sesion")
		self.boton_cancelar = QPushButton("Cancelar")
		self.boton_cancelar.setToolTip("salir")

		#Grid Layout de resultados
		grilla = QGridLayout()
		grilla.addWidget(self.boton_cancelar, 3, 6)
		grilla.addWidget(self.boton_aceptar, 3, 7)

		#Layout horizontal - Ingreso de Datos
		layout_horizontal = QHBoxLayout()
		layout_horizontal.addWidget(self.usuario_lbl)
		layout_horizontal.addWidget(self.usuario_edit)

		layout_horizontal1 = QHBoxLayout()
		layout_horizontal1.addWidget(self.password_lbl)
		layout_horizontal1.addWidget(self.password_edit)

		layout_vertical.addLayout(layout_horizontal)
		layout_vertical.addLayout(layout_horizontal1)
		
		layout_vertical.addLayout(grilla)

		self.setLayout(layout_vertical)

		#conexion de botones
		self.boton_aceptar.clicked.connect(self.obtener_datos)
		self.boton_cancelar.clicked.connect(self.salir)

	def obtener_datos(self):
		"""se encarga de obtener los datos y enviar a los metodos correspondientes """

		usuario = self.usuario_edit.text()
		self.mostrar_usuario(usuario)

		password = self.password_edit.text()
		self.mostrar_password(precio)

	def salir(self):
		""" Nos permite salir del sistema """
		sys.exit(app)
		