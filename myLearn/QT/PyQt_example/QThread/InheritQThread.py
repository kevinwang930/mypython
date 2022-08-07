
# -*- coding: utf-8 -*-

"""
Created on 2018年3月9日
@author: Irony
@site: https://pyqt5.com , https://github.com/892768447
@email: 892768447@qq.com
@file: InheritQThread
@description: 继承QThread
"""
import threading
from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QWidget, QVBoxLayout, QProgressBar, QPushButton


__Author__ = 'By: Irony\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class Worker(QThread):

    valueChanged = Signal(int)  # 值变化信号

    def run(self):
        print('thread id', int(threading.current_thread().ident))
        for i in range(1, 101):
            # print('value', i)
            self.valueChanged.emit(i)
            QThread.msleep(100)


class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self)
        self.progressBar = QProgressBar(self)
        self.progressBar.setRange(0, 100)
        layout.addWidget(self.progressBar)
        layout.addWidget(QPushButton('开启线程', self, clicked=self.onStart))

        # 当前线程id
        print('main id', int(threading.current_thread().ident))

        # 子线程
        self._thread = Worker(self)
        # self._thread.finished.connect(self._thread.deleteLater)
        self._thread.valueChanged.connect(self.progressBar.setValue)

    def onStart(self):
        print('main id', int(threading.current_thread().ident))
        self._thread.start()  # 启动线程

    def closeEvent(self, event):
        if self._thread.isRunning():
            self._thread.quit()
            # 强制
            # self._thread.terminate()
        del self._thread
        super(Window, self).closeEvent(event)


if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
