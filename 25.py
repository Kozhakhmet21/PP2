class person:
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname
    def show(self):
        print(f"{self.name} {self.lastname}")

a=person("Alex","Clarkson")
a.show()