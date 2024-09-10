# Selection Sort (A) which is not sorted
#Similar to brute force for 2sum

# GOAL: Sort A s.t. A[1] < A[2] < ... < A[n]
# A = [7, 2, 1, 4, 3]
# RT: O(logn)

def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)