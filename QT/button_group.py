from PySide2.QtWidgets import QApplication, QPushButton,QButtonGroup,QMainWindow,QHBoxLayout,QWidget
from PySide2.QtCore import QState,QStateMachine,SIGNAL
class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        w = QWidget()

        hbox = QHBoxLayout()

        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)


        w.setLayout(hbox)
        self.setCentralWidget(w)
        self.bp = QButtonGroup()
        self.bp.addButton(okButton,id=0)
        self.bp.addButton(cancelButton,id = 1)
        machine = QStateMachine(self)
        s_start = QState(machine)
        s_next = QState(machine)
        s_next.entered.connect(self.test1)
        s_start.addTransition(okButton.clicked, s_next)
        machine.setInitialState(s_start)
        machine.start()
    def test1(self,*arg):
        print('this is test')
app = QApplication()
mw = MainWindow()
mw.show()
app.exec_()