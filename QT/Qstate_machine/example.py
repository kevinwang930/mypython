from PySide2.QtWidgets import QPushButton,QApplication
from PySide2.QtCore import QState,QStateMachine,QFinalState,Signal

app = QApplication()

button = QPushButton()

class CState(QState):
    def __init__(self,parent = None,entryFunc=None,exitFunc=None) -> None:
        super().__init__(parent)
        self.entryFunc = entryFunc
        self.exitFunc = exitFunc

    def onEntry(self,event):
        print(event.sender())

def statemachine():
    machine = QStateMachine()
    s = QState(machine)
    s1 = CState(s)
    s2 = CState(s)
    s1.assignProperty(button, "text", "Click me")  
    s2.assignProperty(button, "text", "Clicked")
    s1.addTransition(button.clicked, s2)
    s2.addTransition(button.clicked, s1)
    s.setInitialState(s1)
    machine.setInitialState(s)
    return machine
a = statemachine()
a.start()





button.show()
app.exec_()
