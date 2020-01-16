# -*- coding: utf-8 -*-
"""
類別
"""
class Student():
    def setName(self,name):
        self.name=name;
    def showName(self):
        print(self.name);
stu1=Student();
stu2=Student();
stu3=Student();
stu1.setName('Tom');
stu2.setName('Harry');
stu3.setName('Peter');
stu1.showName();
stu2.showName();
stu3.showName();
