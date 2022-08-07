from pathlib import Path
import pytest


excelPath = Path(Path(__file__).parents[0],'example.xlsx')
excelPathCreate = Path(Path(__file__).parents[0], 'example1.xlsx')




@pytest.fixture(scope='module')
def workbook():
    from project.excel import workbook
    return workbook


@pytest.fixture(scope='module')
def xl():
    from project.excel import xl
    xl.Visible = True
    return xl

@pytest.fixture(scope='module')
def xlapp():
    from project.desktop import xlapp
    from project.excel import xl
    # xl.Visible = True
    yield xlapp
    xlapp.close()

def test_isExcelFile():
    from project.excel.excelFunc import isExcelFile
    path = Path(Path(__file__).parents[0], 'example.XLSX')
    assert isExcelFile(path) == True



def test_workbookCreate(workbook):
    wb = workbook()
    wb.saveReplace(excelPathCreate)
    wb.close()

def test_workbookOpen(workbook):
    wb = workbook(excelPath)
    a = wb._workbook.Sheets(1).Range('A1').Value
    assert a == 1
    wb.close()


def test_excelGetWorkbookClass(xlapp):
    c = xlapp.getworkbookClass('B001')
    assert c.__name__ == 'workbook_B001'

def test_excelGetWorkbooks(xlapp):
    xlapp.getWorkbooks()
    wb = xlapp.workbooks[0]
    for o in wb.orders:
        o.supplier.insertSupplierToDb()
        # logging.info(o.supplier.supplierNo)



