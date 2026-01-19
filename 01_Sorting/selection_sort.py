# Problem Statement:
# Given a list of integers, sort the list using the Selection Sort algorithm.
# One function sorts the list in ascending order and another sorts it in descending order.

# Algorithm:
# Ascending Order (selection_sort):
# 1. Find the length of the list.
# 2. Iterate through the list from index 0 to n-1.
# 3. Assume the current index as the minimum element.
# 4. Compare it with the remaining elements to find the actual minimum.
# 5. Swap the minimum element with the element at the current index.
# 6. Repeat until the list is sorted in ascending order.
#
#
# Descending Order (selection_sort1):
# 1. Find the length of the list.
# 2. Iterate through the list from index 0 to n-1.
# 3. Assume the current index as the maximum element.
# 4. Compare it with the remaining elements to find the actual maximum.
# 5. Swap the maximum element with the element at the current index.
# 6. Repeat until the list is sorted in descending order.

# Time Complexity (TC):
# Best Case: O(n²)
# Space Complexity: O(1) 

nums = [1, 2, 4, 3, 6, 8, 5, 7, 9, 10]

def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


def selection_sort1(nums):
    n = len(nums)
    for i in range(0, n):
        max_index = i
        for j in range(i + 1, n):
            if nums[j] > nums[max_index]:
                max_index = j
        nums[i], nums[max_index] = nums[max_index], nums[i]
    return nums


print(selection_sort(nums))
print(selection_sort1(nums))
