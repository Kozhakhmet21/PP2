class person:
    def __init__(self,fname,lname):
        print("parents")
        self.firstname=fname
        self.lastname=lname
    def pr(self):
        print(self.firstname,self.lastname)

class student(person):
    def __init__(self,fname,lname):
        print("child")
        person.__init__(self,fname,lname)


x = student("Joe","Harris")
x.pr()