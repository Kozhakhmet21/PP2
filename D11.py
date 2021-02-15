def IsPrime(n):
    for i in range(2,int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True
 
a = input()
i = 2
while i < a+1:
    ch1 = i
    while IsPrime(ch1) == True and a % ch1 == 0:
        a /= ch1
        print ch1
    i += 1