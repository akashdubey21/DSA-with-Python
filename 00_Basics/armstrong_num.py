# Problem Statement:
# Given an integer number as input, check whether the number is an Armstrong Number.
# An Armstrong number is a number that is equal to the sum of its digits each raised
# to the power of the total number of digits.

# Algorithm:
# 1. Take an integer input from the user and store it in 'num'.
# 2. Store the original number in 'n' for comparison.
# 3. Calculate the number of digits using len(str(num)) and store it in 'nod'.
# 4. Initialize 'total' to 0 to store the sum of powered digits.
# 5. While 'num' is greater than 0:
#    a. Extract the last digit using modulus operator (% 10).
#    b. Raise the digit to the power 'nod' and add it to 'total'.
#    c. Remove the last digit from 'num' using integer division (// 10).
# 6. Compare 'total' with the original number.
# 7. If both are equal, print "Armstrong Number"; otherwise, print "Not an Armstrong Number".

# Time Complexity (TC):
# O(n), where n is the number of digits in the input number.

num = int(input())
n = num
nod = len(str(num))
total = 0

while num > 0:
    ans = num % 10
    total += ans ** nod
    num = num // 10

if total == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
