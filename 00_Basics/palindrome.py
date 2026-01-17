# Problem Statement:
# Given an integer number as input, check whether the number is a palindrome.
# A palindrome number remains the same when its digits are reversed.

# Algorithm:
# 1. Take an integer input from the user and store it in 'num'.
# 2. Store the original number in a temporary variable 'n'.
# 3. Initialize 'rev' to 0 to store the reversed number.
# 4. While 'n' is greater than 0:
#    a. Extract the last digit using modulus operator (% 10).
#    b. Append the digit to 'rev' by multiplying 'rev' by 10 and adding the digit.
#    c. Remove the last digit from 'n' using integer division (// 10).
# 5. Compare the reversed number with the original number.
# 6. If both are equal, print "Palindrome"; otherwise, print "Not a Palindrome".

# Time Complexity (TC):
# O(n), where n is the number of digits in the input number.

num = int(input())
n = num
rev = 0

while n > 0:
    ans = n % 10
    rev = (rev * 10) + ans
    n = n // 10

if rev == num:
    print("Palindrome")
else:
    print("Not a Palindrome")
