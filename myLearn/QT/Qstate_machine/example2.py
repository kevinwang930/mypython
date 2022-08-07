from PySide2.QtCore import (Signal, QPointF, QPoint, QPropertyAnimation, QRect,
                          QRectF, QState, QEasingCurve, QStateMachine, Qt)
from PySide2.QtWidgets import (QApplication, QGraphicsScene, QGraphicsWidget,
                             QGraphicsView, QPushButton, QDialog, QFormLayout)
from PySide2.QtGui import QPixmap, QPainterPath, QPainter
import sys


class Button(QGraphicsWidget):

    clicked = Signal()

    def __init__(self, parent_arg=None):
        super(Button, self).__init__(parent_arg)

    def mousePressEvent(self, ev):
        self.clicked.emit()
        self.update()

    def boundingRect(self):
        return QRectF(0, 0, 100, 50)

    # def shape(self):
    #     path=QPainterPath()
    #     path.addEllipse(self.boundingRect())
    #     return path

    def paint(self, painter, option, widget):
        r = self.boundingRect()
        painter.setPen(Qt.darkGray)
        painter.setBrush(Qt.yellow)
        painter.drawEllipse(r)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    button = Button()
    #所有的状态都有一个共同的父亲节点
    machine = QStateMachine()

    state1 = QState(machine)
    state2 = QState(machine)
    state3 = QState(machine)

    #状态中的矩形区域是将原来控件的原点与目标的中的（x,y）两点相对齐
    state1.assignProperty(button, 'geometry', QRect(0, 0, 100, 50))
    state2.assignProperty(button, 'geometry', QRect(100, 0, 100, 50))
    state3.assignProperty(button, 'geometry', QRect(200, 0, 100, 50))

    state1.addTransition(button.clicked, state2)

    state2.addTransition(button.clicked, state3)

    state3.addTransition(button.clicked, state1)

    machine.setInitialState(state2)
    machine.start()

    scene = QGraphicsScene(0, 0, 300, 100)
    scene.addItem(button)

    view = QGraphicsView(scene)
    view.show()

    button.show()
    sys.exit(app.exec_())
