# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:22:07 2020

@author: kevin
"""


import sys
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel("Hello World!")
label.show()
app.exec_()