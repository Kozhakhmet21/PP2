class person:
    def __init__(self,fname,lname):
        print("parent's constuctor")
        self.firstname=fname
        self.lastname=lname

    def pr(self):
        print(self.firstname,self.lastname)

class student(person):
    def __init__(self,fname,lname):
        print("child's constuctor")
        person.__init__(self,fname,lname) #Buny zhazbai qate bolady,bul osy functianyn oryndaluyn qadagalaidy

x=student("John","Smith")
x.pr()