class person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class employe(person):
    def __init__(self, name, idnumber,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,idnumber)
a=employe('Sidra',1519608,50000,'intern')    
a.display()   

class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)
class student(person):
    def __init__(self,fname,lname,year):
        person.__init__(self,fname,lname)
        self.graduationyear=year
x=student("sidra","khan",2024)  
print(x.graduationyear)      

from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("i can walk and run")
class snake(animal):
    def move(self):
        print("i can crawl")
class dog(animal):
    def move(self):
        print("i can bark  and run") 
class lion(animal):
    def move(self):
        print("i can roar and run")
h=human()
h.move()
s=snake()
s.move()
d=dog()
d.move()
l=lion()
l.move()                               

        

                    
    