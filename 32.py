class fib:
    def __init__(self,limit):
        self.limit=limit
    def __iter__(self):
        self.x=0
        self.y=1
        self.cnt=1
        return self
    def __next__(self):
        if self.cnt>self.limit:
            raise StopIteration

        a,b=self.x,self.y
        self.x,self.y=self.y,self.x+self.y
        self.cnt+=1
        return a+b
a=fib(10)
for i in a:
    print(i)