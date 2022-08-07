import sys
from PySide2 import QtWidgets

i = 0
class Message(QtWidgets.QMainWindow):

    def __init__(self):
          # 如果希望窗口内嵌于其他部件，可添加parent参数
        super(Message, self).__init__()
         # 调用初始化方法
        self.initUI()

    def initUI(self):
         # 设置窗口的所在位置，以左上角为原点，x轴300, y轴300, 宽250, 长150
        self.setGeometry(300, 300, 250, 150)
         # 给窗口一个标题名，你将会在标题栏看到这个名字
        self.setWindowTitle('Message box')

    # def closeEvent(self, event):
    #     # message为窗口标题
    #      # Are you sure to quit?窗口显示内容
    #     # QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No窗口按钮部件
    #      # QtWidgets.QMessageBox.No默认焦点停留在NO上
    #     reply = QtWidgets.QMessageBox.question(self, 'Message',"Are you sure to quit?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
    #     # 判断返回结果处理相应事项
    #     if reply == QtWidgets.QMessageBox.Yes:
    #          event.accept()
    #     else:
    #          event.ignore()
    def onClose(self):
        def closeEvent(event):
            # message为窗口标题
            # Are you sure to quit?窗口显示内容
            # QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No窗口按钮部件
            # QtWidgets.QMessageBox.No默认焦点停留在NO上
            reply = QtWidgets.QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            # 判断返回结果处理相应事项
            if reply == QtWidgets.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

        return closeEvent


def closeEvent1(event):
    global i
    print('close event activated')
    if i > 3:
        event.accept()
    else:
        i = i + 1
        event.ignore()

def main():
     # 创建qt的主应用
     app = QtWidgets.QApplication(sys.argv)
     # 实例化自己写的类
     ex = Message()
     ex.closeEvent = closeEvent1
     ex.show()
     # 应用关闭时返回0,sys关闭进程
     sys.exit(app.exec_())


if __name__ == '__main__':
     main()
