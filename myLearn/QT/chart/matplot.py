
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# import matplotlib
# matplotlib.use('Qt5Agg') #Render to PySide/PyQt Canvas
# print(matplotlib.rcParams.keys())
# matplotlib.rcParams['backend.qt5']='PySide2'

from matplotlib.figure import Figure
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import *
app = QApplication([])
# generate the plot
fig = Figure(figsize=(600,600), dpi=72, facecolor=(1,1,1), edgecolor=(0,0,0))
ax = fig.add_subplot(111)
# Add data:
ax.plot([0,1])
# generate the canvas to display the plot
canvas = FigureCanvas(fig)
# Add a button
button = QPushButton("I'm still just a button man")
button.setMaximumWidth(200)
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(canvas)
window.setLayout(layout)
window.show()
app.exec_()