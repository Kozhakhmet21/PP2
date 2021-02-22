class fib:
    def __init__(self,limit):
        self.limit=limit
    def __iter__(self):
        self.x=0
        self.y=1
        return self
    def __next__(self):
        if self.y+self.x>self.limit:
            raise StopIteration
        a,b=self.x,self.y
        self.x,self.y=self.y,self.x+self.y
        return a+b
a=fib(100)
for x in a:
    print(x)