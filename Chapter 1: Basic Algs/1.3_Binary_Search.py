# Binary Search
# (A, t) is sorted

# GOAL: Return k s.t. A[k] = t (or nothing)

# A = [1, 3, 4, 7, 8, 12, 15], t = 8

# Brute force: O(n)
# RT: 0(1) per iteration
# each iteration shrinks by 1/2 thus RT = O(logn) iterations
def bruteForceBST(self, nums: list[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        # Finding the mid using floor division
        mid = low + ((high - low) // 2)

        # Target value is present at the middle of the array
        if nums[mid] == target:
            return mid

        # Target value is present in the low subarray
        elif target < nums[mid]:
            high = mid - 1

        # Target value is present in the high subarray
        elif target > nums[mid]:
            low = mid + 1

        # Target value is not present in the array
        return -1