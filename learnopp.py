import datetime
class Employee:
    
    pay_rising = 0.2
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.mail=first + '.'+last+'gmail.com'
        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def pay_increase(self):
        self.pay += int(self.pay * self.pay_rising) # اینجا یمتونیم از ااین یکی کدم استفاده کنیم ولی ااگر بخوایم تکی یه افزایش حقوق داشته باشیم نمیتوننیم جا به جا کن ببین تغییرات 
        #self.pay += int(self.pay * Employee.pay_rising) overwrite
    @classmethod
    def set_rise(cls,amnt):
        cls.pay_rising=amnt   
    @classmethod
    def from_str_emp(cls,emp_str):
        first , last , pay = emp_str.split('_')
        return cls (first,last,pay)
    @staticmethod
    def is_working(day):
        if day.weekday()==3 or day.weekday()==4:
            return False
        return True
    
    
    
class Developer (Employee):
    def __init__(self,first,last,pay,prog_lang):
        Employee.__init__(self,filter,last,pay)
        self.prog_lang=prog_lang
        
class Manager :
    def __init__(self,first,last,pay,employees=None):
        #Employees.__init__(self,first,last,pay)
        super.__init__(self,first,last,pay)
        if employees is None :
            self.employees=[]
        else:
            self.employees=employees
            
    def add_emps(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emp(self):
        for emp in self.employees:
            print("__",emp.fullname())
        
        
            
emp1=Employee('hamid','hamidi',2000)
emp2=Employee('hasan','hasani',2500)
print(Employee.fullname(emp1))
print(emp2.fullname())
# Employee.pay_rising=0.6
# emp1.__class__.pay_rising=0.9
# Employee.set_rise(0.45)
# emp1.set_rise(0.45)
# emp1.pay_rising = 0.15
# emp3_str= " hamid_hamidi_6000"
# emp4_str=" zahara_mohamdi_3000"
# emp5_str=" sara_irni_8000"

# new_emp3=Employee.from_str_emp(emp3_str)
# new_emp4=Employee.from_str_emp(emp4_str)
# new_emp5=Employee.from_str_emp(emp5_str)
# my_date=datetime.date(2020,2,4)
# print(Employee.is_working(my_date))
# print(new_emp3.pay)

# print(Employee.pay_rising)
# print(emp1.pay_rising)
# print(emp2.pay_rising)
# emp1.pay_increase()
# emp2.pay_increase()
# print(emp1.pay)
# print(emp2.pay)
# print(Employee.__dict__)
# # print(emp1.__dict__)
# # print(emp2.__dict__)    