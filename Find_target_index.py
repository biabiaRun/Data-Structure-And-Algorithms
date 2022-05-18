"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

"""
# wrong version 1
def find_int (self, nums: List[int], target: int):
    left = 0
    right = len(nums) - 1
    if nums[left] > nums[right]:
        return -1
    while (nums[left] <= nums[right]):  #这里错了，想想为什么
        pivot = left + (right - left) // 2
        guess = nums[pivot]
        
        if guess > target:
            right = pivot - 1
        if guess < target:
            left = pivot + 1
        else:
            return pivot # 这里也错了

# Wrong version 2
class Solution:
    def search (self, nums: List[int], target: int):
        left = 0
        right = len(nums) - 1
        
        while (left <= right):  # 思考：为什么此处是left <= right
            pivot = left + (right - left) // 2
            guess = nums[pivot]
        
            if guess > target:
                right = pivot - 1
            if guess < target:
                left = pivot + 1
            else:
                return pivot  # 这步错了是因为，除了上述2种情况，
                              # 并不是仅仅剩下pivot = target, 还有pivot != target的情况，及list中没有target
        return -1




# Correct version
class Solution:
    def search(self, nums: List[int], target: int) -> int: # 要弄懂这种定义是什么意思？
        left = 0
        right = len(nums) - 1
        
        while (left <= right):
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if nums[pivot] < target:
                left = pivot + 1
            else: right = pivot -1
            #return pivot
            
        return -1  # with case that target is NOT in the list
        
        
