# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:25:19 2020

@author: kevin
"""


from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl

app = QApplication([])
view = QQuickView()
url = QUrl("view.qml")

view.setSource(url)
view.show()
app.exec_()