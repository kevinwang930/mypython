from PySide2 import QtCore, QtGui, QtWidgets
from Power_bar import PowerBar
import sys

app = QtWidgets.QApplication([])
volume = PowerBar(10)
volume.show()
sys.exit(app.exec_()) 