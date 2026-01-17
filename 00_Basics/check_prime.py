# Problem Statement:
# Given an integer number as input, check whether the number is a Prime number.
# A prime number has exactly two distinct factors: 1 and itself.

# Algorithm:
# 1. Take an integer input from the user and store it in 'num'.
# 2. Initialize an empty list 'ans' to store the factors of the number.
# 3. Iterate from 1 to 'num' (inclusive).
# 4. For each value 'i', check if 'num' is divisible by 'i'.
# 5. If divisible, add 'i' to the factors list.
# 6. If the total number of factors is exactly 2, print "Prime";
#    otherwise, print "Not Prime".

# Time Complexity (TC):
# O(n), where n is the value of the input number.

num = int(input())
ans = []

for i in range(1, num + 1):
    if num % i == 0:
        ans.append(i)

if len(ans) == 2:
    print("Prime")
else:
    print("Not Prime")
