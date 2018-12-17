from PySide import QtCore, QtGui
import sys

class Root(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.layout = QtGui.QHBoxLayout()
		self.setLayout(self.layout)
		
		self.label = QtGui.QLabel('Hello, world!', self)
		self.button = QtGui.QPushButton(parent=self)
		QtCore.QObject.connect(self.button, QtCore.SIGNAL("clicked()"), app, QtCore.SLOT("quit()"))
		
		self.layout.addWidget(self.label)
		self.layout.addWidget(self.button)


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	root = Root()
	root.show()
	sys.exit(app.exec_())
