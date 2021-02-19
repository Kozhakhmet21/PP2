class person:
    def __init__(self,fname,lname):
        print("parent's constuctor")
        self.firstname=fname
        self.lastname=lname

    def pr(self):
        print(self.firstname,self.lastname)

class student(person):
    pass #Osylai zhazyb ketuge bolad, buns ignorit etedy
x=student("John","Smith")
x.pr()