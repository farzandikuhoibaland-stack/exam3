# p1
# part1 ....
# class Book:
#     def __init__(self, id, title, year, price):
#         self.id=id
#         self.title=title
#         self.year=year
#         self.price=price

# class BookRepository(Book):
#     def __init__(self, id, title, year, price):
#         super().__init__(id, title, year, price)
#         self.next_id=1


#     def create(self, data):
#         self.next_id+=1
#         return f'{self.title}-{self.year}-{self.price}-{self.next_id}'
     
    
#     def update(self, id, data):
#         self.next_id+=1
#         return f'{self.title}-{self.year}-{self.price}-{self.next_id}'
     
    
#     def delete(self, id):
#         self.next_id+=1
#         return f'{self.title}-{self.year}-{self.price}-{self.next_id}'
     
    
#     def get_by_id(self, id):
#         self.next_id+=1
#         return f'{self.title}-{self.year}-{self.price}-{self.next_id}'
     
    
#     def get_all():
#         return 
    

# # part2 ....
# class Author:
#     def __init__(self, id, title, year, price):
#         self.id=id
#         self.title=title
#         self.year=year
#         self.price=price

# class AuthorRepository(Book):
#     def __init__(self, id, title, year, price):
#         super().__init__(id, title, year, price)
#         self.next_id=1


#     def create(self, data):
#         self.next_id+=1
#         return f'{self.title}-{self.year}-{self.price}-{self.next_id}'
     
    
#     def update(self, id, data):
#         self.next_id+=1
#         return f'{self.title}-{self.year}-{self.price}-{self.next_id}'
     
    
#     def delete(self, id):
#         self.next_id+=1
#         return f'{self.title}-{self.year}-{self.price}-{self.next_id}'
     
    
#     def get_by_id(self, id):
#         self.next_id+=1
#         return f'{self.title}-{self.year}-{self.price}-{self.next_id}'
     
    
#     def get_all():
#         return 





# p2 done
# class Publication:
#     def __init__(self,title,year):
#         self.title=title
#         self.year=year

#     def get_info(self):
#         return f'title: {self.title}, year: {self.year}'
    

# class Book(Publication):
#     def __init__(self, title, year, pages):
#         super().__init__(title, year)
#         self.pages=pages

#     def check(self):
#         if isinstance(self.title, Publication):
#             return True
#         else:
#             return False

#     def get_info(self):
#         return f'Book: {self.title}({self.year}), pages:{self.pages}'
    

# class Magazine(Publication):
#     def __init__(self, title, year, issue_number):
#         super().__init__(title, year)
#         self.issue_number=issue_number


#     def get_info(self):
#          return f'Magazine: {self.title}({self.year}), issue#:{self.issue_number}'

# b=Book('Clean Code', 2008, 464)
# m=Magazine('Forbes', 2024, 7)

# print(b.get_info())
# print(m.get_info())
# print(b.check())



# p3 done
# class BankAccount:
#     def __init__(self,owner, initial_balance=0):
#         self.__owner=owner
#         self.__balance=initial_balance
    

#     def get_balance(self):
#         return f'na vashem schetu: {self.__balance}'
    
#     def get_owner(self):
#         return f'moi dengi eto mamini dengi: {self.__owner}'

#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             return f'uspeshno guzasht, seychas: {self.__balance}'
#         else:
#             return 'ne'
        
#     def withdraw(self,amount):
#         if 0<amount<self.__balance:
#             self.__balance-=amount
#             return f'sum raft, ostalos: {self.__balance}'
#         else:
#             return'namerasad sum'
        

# b=BankAccount('buvajon', 100)
# print(b.deposit(50))
# print(b.withdraw(200))
# print(b.withdraw(30))
# print(b.get_balance())
# print(b.get_owner())

# # b.balance=100000  explanation: ne rabotaet potomu chto u menya obj 
# # nazivaetsya b a ne account, nu i potomu chto barobar 
# # mozhno kadan togda kogda @property ispolzuem

        

# p4 done with bonus
# class Shape:
#     def __init__(self, name):
#         self.name=name

#     def area(self):
#         return 0
    
#     def describe(self):
#         return f'{self.name}: area = {s.area():.2f}'
    

# class Circle(Shape):

#     def __init__(self, name, radius):
#         super().__init__(name)
#         self.radius=radius
#         self.p=3.14

#     def area(self):
#         return self.p * self.radius**2
    
#     def describe(self):
#         return f'{self.name}: area = {c.area():.2f}'
    
# class Rectangle(Shape):
#     def __init__(self, name, width, height):
#         super().__init__(name)
#         self.width=width
#         self.height=height

#     def area(self):
#         return self.width*self.height
    
#     def describe(self):
#         return f'{self.name}: area = {r.area():.2f}'
    
# class Trinagle(Shape):
#     def __init__(self, name, base, height):
#         super().__init__(name)
#         self.base=base
#         self.height=height

#     def area(self):
#         return self.base*self.height*0.5
    
#     def describe(self):
#         return f'{self.name}: area = {t.area():.2f}'
    
# class Square(Shape):
#     def __init__(self, name, side):
#         super().__init__(name)
#         self.side=side

#     def area(self):
#         return self.side**2
    
#     def describe(self):
#         return f'{self.name}: area = {sq.area():.2f}'
    
# s=Shape('shape')
# c=Circle('circle',3)
# r=Rectangle('rec',4,5)
# t=Trinagle('tri', 6,2)
# sq=Square('sq', 4)
# print(c.describe())
# print(r.describe())
# print(t.describe())
# print(sq.describe())

# Shape=[c.area(), r.area(), t.area(), s.area()]
# total_area=0
# for shape in Shape:
#     total_area+=shape
# print(f'Total area = {total_area:.2f}')


# p5 done
# from abc import ABC, abstractclassmethod
# class Employee(ABC):
#     def __init__(self, name):
#         self.__name=name

#     def getter(self):
#         return self.__name
    
#     def setter(self, new_name):
#         self.__name=new_name
#         return self.__name
    
#     def calculate_salary(self):
#         return 0

#     def show_info(self):
#         return f"{self.__name}: salary = {e.calculate_salary()}"
    


# class FullTimeEmployee(Employee):
#     def __init__(self, name, monthly_salary):
#         super().__init__(name)
#         self.__name=name
#         self.__monthly_salalry=monthly_salary

#     def getter(self):
#         return self.__name
    
#     def setter(self, new_name):
#         self.__name=new_name
#         return self.__name

#     def get_f(self):
#         return self.__monthly_salary
    
#     def set_f(self, new_f):
#         self.__monthly_salary=new_f
#         return self.__monthly_salary

#     def calculate_salary(self):
#         return self.__monthly_salalry
        
#     def show_info(self):
#         return f"{self.__name}: salary = {f.calculate_salary()}"



# class PartTimeEmployee(Employee):
#     def __init__(self, name, hourly_rate, hours_worked):
#         super().__init__(name)
#         self.__name=name
#         self.__hourly_rate=hourly_rate
#         self.__hours_worked=hours_worked

#     def getter(self):
#         return self.__name
    
#     def setter(self, new_name):
#         self.__name=new_name
#         return self.__name

#     def get_p1(self):
#         return self.__hourly_rate
    
#     def set_p1(self, new_p1):
#         self.__hourly_rate=new_p1
#         return self.__hourly_rate
    

#     def get_p2(self):
#         return self.__hours_worked
    
#     def set_p2(self, new_p2):
#         self.__hours_worked=new_p2
#         return self.__hours_worked

#     def calculate_salary(self):
#         return self.__hourly_rate*self.__hours_worked

#     def show_info(self):
#         return f"{self.__name}: salary = {p.calculate_salary()}"

# e=Employee('n')
# f=FullTimeEmployee("Anna", 3000)
# p=PartTimeEmployee("Bob", 20, 80)
# print(f.show_info())
# print(p.show_info())

# employees=[f.calculate_salary(), p.calculate_salary()]
# total_payroll=0
# for e in employees:
#     total_payroll+=e

# print(f'Total payroll: {total_payroll}')

