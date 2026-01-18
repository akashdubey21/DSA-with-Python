# Problem Statement:
# Given a list of integers, sort the list using the Bubble Sort algorithm.
# One function sorts the list in ascending order and another sorts it in descending order.

# Algorithm:
# Ascending Order (bubble_sort):
# 1. Find the length of the list.
# 2. Traverse the list from the end towards the beginning.
# 3. Compare adjacent elements.
# 4. Swap them if they are in the wrong order.
# 5. After each pass, the largest element moves to its correct position.
#
# Descending Order (bubble_sort1):
# 1. Find the length of the list.
# 2. Traverse the list from the end towards the beginning.
# 3. Compare adjacent elements.
# 4. Swap them if they are in the wrong order for descending order.
# 5. After each pass, the smallest element moves to its correct position.

# Time Complexity (TC):
# Best Case: O(n²)
# Space Complexity: O(1) 

nums = [1, 2, 4, 3, 6, 8, 5, 7, 9, 10]

def bubble_sort(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        for j in range(0, i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def bubble_sort1(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        for j in range(0, i - 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


print(bubble_sort(nums))
print(bubble_sort1(nums))
