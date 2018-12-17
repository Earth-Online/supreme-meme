from PySide import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
root = QtGui.QWidget()
root.resize(800, 600)

#label = QtGui.QLabel('Hello, world!', root)
button = QtGui.QPushButton(parent=root)

QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), app, QtCore.SLOT("quit()"))

root.show()
sys.exit(app.exec_())
