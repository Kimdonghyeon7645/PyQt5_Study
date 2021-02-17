import sys
import os
# import site
# site.addsitedir('/usr/local/lib/python2.7/site-packages')
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

app = QtWidgets.QApplication(sys.argv)
view = QtWebEngineWidgets.QWebEngineView()

# view.settings().setAttribute(QtWebEng.QWebSettings.LocalContentCanAccessRemoteUrls, True)

# f = open('html/test.html', 'r')
#
# html = f.read()
# f.close()

# print(os.path.abspath(__file__))
# path = os.path.abspath(__file__)
# print()

# view.setHtml(html)
# view.setHtml(html, baseUrl=QtCore.QUrl().fromLocalFile(os.path.split(os.path.abspath(__file__))))

# view.setUrl()
# view.set
# view.load(QtCore.QUrl('http://'))

view.load(QtCore.QUrl().fromLocalFile(
    os.path.split(os.path.abspath(__file__))[0]+r'\html\test.html'
))

view.show()
sys.exit(app.exec_())
