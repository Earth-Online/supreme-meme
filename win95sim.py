import sys
 
from PyQt4.QtWebKit import QWebView
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
 
app = QApplication(sys.argv)
 
browser = QWebView()
browser.load(QUrl(r"https://dd86k.github.io/win98websim/win98.html"))
browser.show()
 
app.exec_()
