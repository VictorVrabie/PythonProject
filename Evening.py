import random


# EXCERCISE 5
class Customer(object):
    def __init__(self, typeC):
        self.typeC = typeC
        if self.typeC == "Returning" :
            self.bet = 10
            self.budget = random.randint(100,300)
        elif self.typeC == "New" :
            self.budget = random.randint(200,300)
            self.bet = random.randint(0,int((self.budget)/3))
        else:
            self.budget = random.randint(200,500)
            self.bet = random.randint(0,int(self.budget))

def CustomerTypes(total, returning, bachelor):
        ret = int(total * (returning/100))
        bch = int(total * (bachelor/100))
        new = total - (ret + bch)
        list = []
        list.extend(["Returning" for i in range(ret)])
        list.extend(["New" for i in range(new)])
        list.extend(["Bachelor" for i in range(bch)])
        return(zip(range(total),list))


x=list(CustomerTypes(10,40,50))


y=list(zip([x[i][0] for i in range(len(x))],
      [Customer(x[i][1]).budget for i in range(len(x))],
      [Customer(x[i][1]).bet for i in range(len(x))]))

print(list(y))










#     def averagegrade(self):
#         sum = 0
#         for student in self.studentslist:
#             sum += student.grade
#         return float(sum/len(self.studentslist))
#
#     def givegrades(self):
#         return False
#
# class Workshop(Class):
#
#     def givegrades(self):
#
#         for student in self.studentslist:
#             student.gradeStudent(self.teacher)
#
#         for index, student in enumerate(self.studentslist):
#             if index %2 ==0:
#                 if index+1 < len(self.studentslist):
#                     student.grade = (student.grade + self.studentslist[index+1].grade)/2
#             else:
#                 student.grade = self.studentslist[index-1].grade
#
# class Lecture(Class):
#
#     def givegrades(self):
#
#         for student in self.studentslist:
#             student.gradeStudent(self.teacher)
#
# from random import randint
#
# class Teacher(object):
#
#
#     def __init__(self, strictness):
#         self.strictness = strictness
#
#
# class Student(object):
#     def __init__(self, intelect):
#         self.intelect = intelect
#     def gradeStudent(self, teacher):
#         self.grade  = self.intelect * (1-teacher.strictness) * float(randint(5,10)/10.0)
#
# class ErasmusStudent(Student):
#     def gradeStudent(self, teacher):
#            self.grade  = self.intelect * (1-teacher.strictness*0.8) * float(randint(5,10)/10.0)