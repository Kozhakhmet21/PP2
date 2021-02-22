class number:
    def __iter__(self):
        self.x=1
        return self
    def __next__(self):
        y=self.x
        self.x+=1
        return y
a=number()
it=iter(a)
print(next(it))
print(next(it)) 
print(next(it)) 
print(next(it)) 
print(next(it)) 
print(next(it)) 