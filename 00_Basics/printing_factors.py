# Problem Statement:
# Given an integer number as input, find and print all the factors of the number.

# Algorithm:
# 1. Take an integer input from the user and store it in 'num'.
# 2. Initialize an empty list 'ans' to store the factors.
# 3. Iterate from 1 to 'num' (inclusive).
# 4. For each value 'i', check if 'num' is divisible by 'i'.
# 5. If divisible, add 'i' to the factors list.
# 6. Print the list of all factors.

# Time Complexity (TC):
# O(n), where n is the value of the input number.

num = int(input())
ans = []

for i in range(1, num + 1):
    if num % i == 0:
        ans.append(i)

print(ans)
