num=int(input())
n =num
nod = len(str(num))
total = 0
while  num > 0:
    ans= (num%10)
    total += ans**nod
    num=num//10
    
if total == n:
        print("Armstrong Number")
else:
    print("Not a Armstrong Number")        
             

