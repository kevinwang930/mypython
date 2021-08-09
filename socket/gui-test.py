# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:43:44 2020

@author: kevin  
"""


import sys
from PyQt5.QtWidgets import QApplication,QWidget,\
QMainWindow,QLabel,QSplashScreen,QProgressBar
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) is fine.
app = QApplication([])


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        label = QLabel("This is a PyQt5 window!")

        # The `Qt` namespace has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)
splash_pix = QPixmap('qt_logo.png')
splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
# adding progress bar
progressBar = QProgressBar(splash)
progressBar.setGeometry(60, 215, 100, 20)

splash.setMask(splash_pix.mask())


splash.show()
#window = MainWindow()
#window.show() # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()

# Your application won't reach here until you exit and the event
# loop has stopped.