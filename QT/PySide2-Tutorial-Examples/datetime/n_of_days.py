

from PySide2.QtCore import QDate, Qt

now = QDate.currentDate()

d = QDate(1945, 5, 7)

print(f'Days in month: {now.daysInMonth()}')
print(f'Days in year: {d.daysInYear()}')
