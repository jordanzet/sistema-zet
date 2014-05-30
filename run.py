from PyQt4 import QtCore, QtGui
import sys

class MiVentana(QtGui.QWidget):
    def __init__(self, padre = None):
        super(MiVentana, self).__init__(padre)
        self.button = QtGui.QPushButton("Hola",self)
        self.connect(self.button, QtCore.SIGNAL("clicked()"), self.say_hello)
        self.show()

    def say_hello(self,**kwargs):
        print "Bienvenido al sistema!"

app = QtGui.QApplication(sys.argv)

v = MiVentana()
v.resize(1200, 600)
v.setWindowTitle('Sistema de Inventario Zet')
v.show()
app.exec_()




