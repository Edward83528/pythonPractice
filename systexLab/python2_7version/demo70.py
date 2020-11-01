class Emp:
    pass


class Engineer(Emp):
    pass


class PM(Emp):
    pass


class HR(Emp):
    pass

emp1 = Emp()
engineer1 = Engineer()
pm1 = PM()
hr1 = HR()
staffs = [(emp1,"Employee1"), (engineer1, "Enginer1"),(pm1, "Project Manager1"), (hr1, "Human Resource")]
emp_classes = [Emp, PM, HR, Engineer]

for staff, name in staffs:
    for emp_class in emp_classes:
        isA = isinstance(staff, emp_class)
        message1 = 'is a' if isA else 'is not a'
        print name , message1, emp_class.__name__

for class1 in emp_classes:
    for class2 in emp_classes:
        isSubclass = issubclass(class1, class2)
        message1 = '{0} a subclass of'.format('is' if isSubclass else 'is not')
        print class1.__name__,message1,class2.__name__