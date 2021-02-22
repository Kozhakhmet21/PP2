class person:
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname
    def show(self):
        print(f"{self.name} {self.lastname}")

class student(person):
    def __init__(self,name,lastname,age,city):
        super().__init__(name,lastname)
        self.age=age
        self.city=city
    def show(self):
        super().show()
        print(f"{self.age} {self.city}")

a=student("Jerry","Olison",26,"Boston")
a.show()