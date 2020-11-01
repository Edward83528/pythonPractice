class Emp:
    gradeLevel = 6

    def startWork(self):
        pass

    def endWork(self):
        pass


class RD(Emp):
    pass


class PM(Emp):
    pass

print Emp.gradeLevel, RD.gradeLevel, PM.gradeLevel
RD.gradeLevel = 7
print Emp.gradeLevel, RD.gradeLevel, PM.gradeLevel
Emp.gradeLevel = 8
print Emp.gradeLevel, RD.gradeLevel, PM.gradeLevel

