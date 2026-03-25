class student:
    grade=10
    print("hi i am a student of class",grade)
od=student()

class student:
    name="mini"
    age=20
    def introduction(self):
        print("hi i am a student")
    def details(self):
        print("my name is",self.name)
        print("i am",self.age,"years old")
od=student()
od.introduction()
od.details()        
 
fatima=student()
fatima.introduction()
fatima.details()


class Parrot:
    species="bird"
    def __init__(self,name,age):

        self.name=name
        self.age=age
    def introduction(self):
        print("hi i am",self.name)
        print("i am",self.age,"years old")
            
blue=Parrot("blue",3)
woo=Parrot("woo",5)
blue.introduction()
woo.introduction()





