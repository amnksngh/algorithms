def insertion_sort(A, reverse = False):
    """Assumes A is a list of integers, by default reverse = False
       Returns the sorted A in non-decreasing order if reverse = False, 
       and in non-increasing order if reverse = True.
       ****************************************
       The complexity of the algorithm is O(n^2)."""
    if reverse == False:
        for j in range(1, len(A)):
            key = A[j]
            i = j - 1
            while i >= 0 and A[i] > key:
                A[i+1] = A[i]
                i = i-1
            A[i+1] = key
        return A
    else:
        for j in range(1, len(A)):
            key = A[j]
            i = j - 1
            while i >= 0 and A[i] < key:
                A[i+1] = A[i]
                i = i - 1
            A[i+1] = key
        return A

# print(insertion_sort([5,1,5,2,5,1,4,5], True))

# Merge-sort

def merge(A, p, q, r):
    """Assumes A to be an array of numbers, p, q, and r are indices of the array A such that that
       p <= q < r. The process also assumes that the subarrays A[p, q] and A[q+1, r] are sorted."""
    n1 = q-p+1
    n2 = r-q
    L, R = [], []
    for i in range(n1):
        L.append(A[p+i])
    for j in range(n2):
        R.append(A[q+j+1])
    L.append(1000)
    R.append(1000)
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A

print(merge([5,6,8,12,15,16,2,5,8,6,7], 0, 5, 10))