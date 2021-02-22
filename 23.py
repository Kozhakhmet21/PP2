class per:
    x=3
    y=7
    def sum(self):
        return self.x+self.y

a=per()
a.x=11
a.y=12
print(a.x,a.y)
print(a.sum())