class fun:
    def f(self,a,b):
        return self.x+self.y+a+b

a=fun()
a.x=4
a.y=8
print(a.x,a.y)
print(a.f(7,8))