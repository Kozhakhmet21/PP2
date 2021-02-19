class person:
    def __init__(self,fname,lname):
        print("parents const.")
        self.firstname=fname
        self.lastname=lname

    def pr(self):
        print(self.firstname,self.lastname)

class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduation=year

    def pr(self):
        print(self.firstname,self.lastname,self.graduation)

    def welcome(self):
        print("Welcome",self.firstname,self.lastname,"to the class of",self.graduation)

x=student("Joe","Clark",2020)
x.welcome()
x.pr()