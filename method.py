# class testclass:
#     def __init__(self):
#         return " i am  a construoctor method"
#     def instancemethod(self):
#         return " i am a instance method"
#     @classmethod
#     def classmethod(cls):
#         return " i am a class method"
#     @staticmethod
#     def staticmethod():
#         return " i am a static method"
# from datetime import date
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     @classmethod
#     def my_classmethod(cls,name,birthdate):
#         return cls(name,date.today().year-birthdate)
#     @staticmethod
#     def is_adult(my_age):
#         return my_age>18
    
    
# person1=Person("hamid",27)
# print(person1.name , person1.age)
# person2=Person.my_classmethod('hamid',1993)
# print(person2.name,person2.age)
# print(person1.is_adult(27))



# class person:
#     def __init__(self,name,id):
#         self.name=name
#         self.idnumber=id
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
        
# class Employee(person):
#     def __init__(self,name,id,salary,post):
#         self.salary=salary
#         self.post=post 
#         person.__init__(self,name,id)
#     def print_details(self):
#         print(self.name,self.idnumber,self.salary,self.post)
        
# e=Employee('hamid',30,3000,'manger')
# e.display()
# e.print_details()
class sup1:
    def __init__(self):
        self.name1='ali'
        print('in dup1')
class sup2:
    def __init__(self):
        self.name2='hamid'
        print("in sup2")
        
class sub(sup1,sup2):
    def __init__(self):
        sup1.__init__(self)
        sup2.__init__(self)
        print('in subclass')
    def print_name(self):
        print(self.name1,self.name2)
        
ob=sub()
ob.print_name()