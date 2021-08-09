from project.excelCom import xl
from project.app_logger import appLogger as logger
from win32com.client import WithEvents
import msvcrt
import pythoncom
import time
import sys
import types

def TestExcel():
    class ExcelEvents:
        def __init__(self,log = logger) -> None:
            super().__init__()
            self.logger = log

        def OnNewWorkbook(self, wb):
            self.logger.info('new workbook created')

        def OnWorkbookActivate(self,wb):
            print('workbook activated')

    class WorkbookEvents:
        def OnActivate(self):
            print("workbook OnActivate")

        def OnBeforeRightClick(self, Target, Cancel):
            print("It's a Worksheet Event")

        def OnBeforeClose(self,Cancel):
            print("close workbook")



    xl.Visible = True
    WithEvents(xl,ExcelEvents)
    book = xl.Workbooks.Add()
    WithEvents(book, WorkbookEvents)
    book.Activate()
    book.Close()
    print("Have book", book)

    time.sleep(3)
    #    sheet = e.Worksheets(1)
    #    sheet = DispatchWithEvents(sheet, WorksheetEvents)

    
if __name__ == "__main__":
    TestExcel()

