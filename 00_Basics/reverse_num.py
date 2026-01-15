num=int(input())
rev = 0
while  num > 0:
    ans= (num%10)
    rev = (rev*10) + ans
    num=num//10
    
print(rev)


