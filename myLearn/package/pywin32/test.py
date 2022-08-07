import win32com.client as client
xl = client.gencache.EnsureDispatch('Excel.Application')
xl.Visible = True
workbook = xl.Workbooks.Add()
sheet = workbook.Worksheets(1)
raw = [[1,2,3,4],[5,6,7,8]]
tuple1= (1,2,3,4)
sheet.Range('A1:D2').Value = raw
sheet.Range(Cell1=sheet.Cells(3,1),Cell2=sheet.Range('d4')).Value = raw
sheet.Range('A5:d5').Value = tuple1
