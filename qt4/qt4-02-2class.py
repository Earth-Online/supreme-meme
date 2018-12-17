from PySide import QtCore, QtGui
import sys

class Root(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		label = QtGui.QLabel('Hello, world!', self)
		#button = QtGui.QPushButton(parent=self)
		#QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), app, QtCore.SLOT("quit()"))


app = QtGui.QApplication(sys.argv)
root = Root()
#root.resize(800, 600)
root.show()
sys.exit(app.exec_())