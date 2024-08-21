# Max Array
# ALG (A):
## Can return max(A) for simplicity
def Alg(A):
    m = A[1] # indexing + assignment = 2 operations
    for i in m:
        if A[i] > m: # index + comparison = 2 operations
            m = A[i] # 2 operations
        return m

# Correctness: m tracks max in A[1:i]
# Subarray form A[i] -> A[i]

# RT: O(n)
# number of "primitive operations"
# 1: asignment (m=0)
# 2: comparison (if x<y)
# 3: arithmetic (a=3+x)
# 4: indexing (x = A[3])
# 5: calls/returns (return A[i])


# Asymptotic Notation (n -> inf)
# ex: RT = f(n) = 3n^2 + 7n^2 + n + 11
# 1: Turn all coefficients into 1
# -> n^2 + n^3 + n + 1
# 2: Keep the largest term
# -> f(n) = O(n^3)
# Intuition: f(n) <= n^3
# O = <=  1: Technically, O(n) is a set
# Omega = >=
# Theta = =

# Sometimes people say "at least O(n^2)"
# -> "at least something(n^2)"

# If the problem sets asks for O(n^2) and your solution runs in O(n) time, probably
# A: your solution is incorrect or,
# B: it relies on something beyond the problems expectations