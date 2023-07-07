"""
Pair the longest task with the shortest one
(Elements in the array, A, represent durations for each task.)
"""
A = [6, 3, 2, 7, 5, 5]

A = sorted(A)

for i in range(len(A)//2):
    print(A[i], A[~i])
