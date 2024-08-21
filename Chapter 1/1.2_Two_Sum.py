# Input: Array A of n distinct integers sorted in increasing order and integer t
# A = [1,3,4,5,7,10,11], t= 10
# -> Alg should return 2, 5, there are cases where can return nothing
# Goal: Return (i, j) s.t. i<j and A[i] + A[j] = t

# Brute Force

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (i != j and nums[i] + nums[j] == target):
                    return [i, j]
        return []

# Two Pointer

def twosSumPointer(A, t):
    left, right = 0, len(A) - 1
    
    while left < right:
        current_sum = A[left] + A[right]
        
        if current_sum == t:
            return (A[left], A[right])
        elif current_sum < t:
            left += 1  # Move the left pointer to the right
        else:
            right -= 1  # Move the right pointer to the left
    
    return None  # If no pair is found