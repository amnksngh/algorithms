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

# print(insertion_sort([5,1,5,2,5,1,4,5]))