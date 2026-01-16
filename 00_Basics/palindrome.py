num=int(input())
n =num
rev = 0
while  n > 0:
    ans= (n%10)
    rev = (rev*10) + ans
    n=n//10
    
if rev == num:
        print("Palindrome")
else:
    print("Not a Palindrome")        
             

