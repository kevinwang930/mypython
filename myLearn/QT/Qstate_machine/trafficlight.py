from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


class LightWidget(QWidget):
    def __init__(self, color):
        super(LightWidget, self).__init__()
        self.color = color
        self.onVal = False

    def isOn(self):
        return self.onVal

    def setOn(self, on):
        if self.onVal == on:
            return
        self.onVal = on
        self.update()

    @Slot()
    def turnOff(self):
        self.setOn(False)

    @Slot()
    def turnOn(self):
        self.setOn(True)

    def paintEvent(self, e):
        if not self.onVal:
            return
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self.color)
        painter.drawEllipse(0, 0, self.width(), self.height())

    on = Property(bool, isOn, setOn)


class TrafficLightWidget(QWidget):
    def __init__(self):
        super(TrafficLightWidget, self).__init__()
        vbox = QVBoxLayout(self)
        self.redLight = LightWidget(Qt.red)
        vbox.addWidget(self.redLight)
        self.yellowLight = LightWidget(Qt.yellow)
        vbox.addWidget(self.yellowLight)
        self.greenLight = LightWidget(Qt.green)
        vbox.addWidget(self.greenLight)
        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.black)
        self.setPalette(pal)
        self.setAutoFillBackground(True)


def createLightState(light, duration, parent=None):
    lightState = QState(parent)
    timer = QTimer(lightState)
    timer.setInterval(duration)
    timer.setSingleShot(True)
    timing = QState(lightState)
    timing.entered.connect(light.turnOn)
    timing.entered.connect(timer.start)
    timing.exited.connect(light.turnOff)
    done = QFinalState(lightState)
    timing.addTransition(timer, SIGNAL('timeout()'), done)
    lightState.setInitialState(timing)
    return lightState


class TrafficLight(QWidget):
    def __init__(self):
        super(TrafficLight, self).__init__()
        vbox = QVBoxLayout(self)
        widget = TrafficLightWidget()
        vbox.addWidget(widget)
        vbox.setContentsMargins(0, 0, 0, 0)

        machine = QStateMachine(self)
        redLight = createLightState(widget.redLight, 1000)
        redLight.setObjectName('red')
        yellowLight = createLightState(widget.yellowLight, 1000)
        redLight.setObjectName('yellow')
        greenLight = createLightState(widget.greenLight, 1000)
        greenLight.setObjectName('green')

        redLight.addTransition(
            redLight, SIGNAL('finished()'), greenLight)
        yellowLight.addTransition(
            yellowLight, SIGNAL('finished()'), redLight)
        greenLight.addTransition(
            greenLight, SIGNAL('finished()'), yellowLight)


        machine.addState(redLight)
        machine.addState(yellowLight)
        machine.addState(greenLight)

        machine.setInitialState(greenLight)
        machine.start()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    widget = TrafficLight()
    widget.resize(110, 300)
    widget.show()
    sys.exit(app.exec_())
