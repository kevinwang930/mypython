# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 17:13:02 2018

@author: kevin
"""
import datetime

class person(object):
    
    def __init__(self, name):
        "Create a person"
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None
    def getName(self):
        """Return self's full name"""
        return self.name
    def getLastname(self):
        return self.lastName
    def setBirthday(self,birthdate):
        self.birthday = birthdate
    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self,other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        return self.name
 
class MITPerson(person):
    nextIdNum = 0 #identification number
    def __init__(self,name):
        person.__init__(self,name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum +=1
    def isStudent(self):
        return isinstance(self,Student)
    def getIdNum(self):
        return self.idNum
    def __lt__(self,other):
        return self.idNum <other.idNum
    
class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self,name,classYear):
        MITPerson.__init__(self,name)
        self.year = classYear
    def getclass(self):
        return self.year
class Grad(Student):
    pass
class TransferStudent(Student):
    def __init__(self,name,fromschool):
        MITPerson.__init__(self,name)
        self.fromschool = fromschool
    def getOldschool(self):
        return self.fromschool
class Grades(object):
    def __init__(self):
        self.students = []
        self.grades ={}
        self.isSorted = True
    def addStudent(self,student):
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
    def addGrade(self,student,grade):
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')
    def getGrades(self,student):
        try:
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')
    def getStudents (self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]
def gradeReport(course):
    """Assumes course is of type Grades"""
    report = ''
    for s in course.getStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot +=g
            numGrades +=1
        try:
            average = tot/numGrades
            report= report +'\n'\
            +str(s)+'\'s mean grade is ' +str(average)
        except ZeroDivisionError:
            report = report + '\n'\
                    +str(s)+' has no grades'
    return report

                
'''
p5=Grad('Buzz Aldrin')
print(p5.nextIdNum)
p6=UG('Billy Beaver', 1984)
print(p6.nextIdNum)
p6.nextIdNum = 10
print(p6.nextIdNum)
print(p5.nextIdNum)
me = MITPerson('Kevin wang')
me.nextIdNum = 6
MITPerson.nextIdNum = 10
print(me.idNum)
him = MITPerson('Donlad J Trump')
print(him.nextIdNum)
her = person('Marilian Mnooro')
print(me.getLastname())
pList = [me,him,her]
for p in pList:
    print(p)
pList.sort()
for p in pList:
    print(p)'''
ug1 = UG('Kevin Wang',2007)
ug2 = UG('Samul Sen',2004)
ug3 = UG('Yong Wang',2001)
g1 = Grad('Lily')
g2 = Grad('Bucky')
sixHundred = Grades()
sixHundred.addStudent(ug1)
sixHundred.addStudent(ug2)
sixHundred.addStudent(g1)
sixHundred.addStudent(g2)
for s in sixHundred.getStudents():
    sixHundred.addGrade(s,75)
sixHundred.addGrade(g1,25)
sixHundred.addGrade(g2,100)
print(sixHundred.getGrades(g2))
print(sixHundred.grades)
sixHundred.addStudent(ug3)
print(gradeReport(sixHundred))





    




