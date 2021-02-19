class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def pr(self):
        print(self.firstname,self.lastname)

class Student(person):
    pass

x=person("John","Doe")
x.pr()