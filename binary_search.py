"""
Check if nums[mid] is equal to the target. If so, we’ve already found a match—in the very first step—and the search terminates.
If nums[mid] > target, you only need to search the left half of the array. Even when you search through the left subarray you can use the same binary search algorithm.
If nums[mid] < target, you can ignore all the elements up to the middle element and only consider the right half of the array.
"""

def binary_search(nums, target, low, high):
    if low > high: # base case: target not found
        return False
    else: 
        mid = (low + high)//2
        if nums[mid] == target:
            return True # Target found
        elif nums[mid] < target:
            return binary_search(nums, target, mid +1, high)
        else: 
            return binary_search(nums, target, low, mid-1)

    
"""
nums = [2,5,7,11,14,21,27,30,36]
target = 27

print(binary_search(nums,target,0,len(nums)-1))
# Output: True

target = 38
print(binary_search(nums,target,0,len(nums)-1))
# Output: False
"""