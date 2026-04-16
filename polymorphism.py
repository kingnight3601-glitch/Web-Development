class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"i am a cat and my name is {self.name} and i am {self.age} years old")
    def make_sound(self):
        print("meow")
class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"i am a dog and my name is {self.name} and i am {self.age} years old")    
    def make_sound(self):
        print("bark") 
cat1=cat("tom",3)
dog1=dog("jack",5)    
for animal in (cat1,dog1):
    animal.info()
    animal.make_sound()


class computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print(f"selling price{self.__maxprice}")   
    def setmaxprice(self,price):
        self.__maxprice=price
c = computer()
c.sell()
c.__maxprice=1000
c.sell()
c.setmaxprice(1000)
c.sell()




        