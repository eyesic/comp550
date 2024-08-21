# Two Sum
def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i
        
        return []

# BST
def binary_search_trace(A, t):
    left, right = 0, len(A) - 1
    trace = []

    while left <= right:
        m = (left + right) // 2
        trace.append(m)
        
        if A[m] == t:
            return trace
        elif A[m] < t:
            left = m + 1
        else:
            right = m - 1

    return trace  # Return trace even if the target is not found

A = [1, 3, 4, 5, 8, 9]
t = 8

print(binary_search_trace(A, t))