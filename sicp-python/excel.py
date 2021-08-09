# -*- coding: utf-8 -*-
"""
Created on Thu May 10 23:15:49 2018

@author: kevin
"""
import time
import win32com.client as win32
def excel():
    """"""
    xl = win32.gencache.EnsureDispatch('Excel.Application')
    ss = xl.Workbooks.Add()
    sh = ss.ActiveSheet
 
    xl.Visible = True
    time.sleep(1)
 
    sh.Cells(1,1).Value = 'Hacking Excel with Python Demo'
    sh.Range("A1").Copy(sh.Range("g1"))
 
    time.sleep(1)
    for i in range(2,8):
        sh.Cells(i,1).Value = 'Line %d' % i
        time.sleep(1)
    #ss.Save
    ss.Close(False)
    xl.Application.Quit()
 
if __name__ == "__main__":
    excel()