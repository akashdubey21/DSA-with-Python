# Problem Statement:
# Given an integer number as input, reverse the digits of the number
# and print the reversed integer.

# Algorithm:
# 1. Take an integer input from the user.
# 2. Initialize a variable 'rev' to store the reversed number.
# 3. While the number is greater than 0:
#    a. Extract the last digit using modulus operator (% 10).
#    b. Append the digit to 'rev' by multiplying 'rev' by 10 and adding the digit.
#    c. Remove the last digit from the number using integer division (// 10).
# 4. Print the reversed number.

# Time Complexity (TC):
# O(n), where n is the number of digits in the input number.

num = int(input())
rev = 0

while num > 0:
    ans = num % 10
    rev = (rev * 10) + ans
    num = num // 10

print(rev)
