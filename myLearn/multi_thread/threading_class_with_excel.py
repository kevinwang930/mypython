import threading
from project.excelBase import xl
xl.Visible = False

class excelThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.xlapp = xl

  def run(self):
    counter = 2
    self.xlapp.Visible = True

t = excelThread()
t.start()
t.join()
