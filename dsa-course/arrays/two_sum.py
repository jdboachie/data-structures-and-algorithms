def two_sum_brute_force(A: list[int], target: int) -> bool:
    """
    Uses Brute Force

    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Args:
        A (list[int]): input list
        target (int): target sum

    Returns:
        bool: True if a suitable pair is found else False
    """
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
    return False


def two_sum_hash_table(A: list[int], target: int) -> bool:
    """
    Uses an auxilliary hash table
    Time Complexity: O(n)
    Space Complexity: O(n)

    Args:
        A (list[int]): input list
        target (int): target sum

    Returns:
        bool: True if a suitable pair is found else False
    """
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True
        else:
            ht[target - A[i]] = A[i]
    return False


def two_sum_two_pointers(A: list[int], target: int) -> bool:
    """
    Uses two pointers
    This algorithm assumes that A is sorted.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        A (list[int]): input list
        target (int): target sum

    Returns:
        bool: True if a suitable pair is found else False
    """
    # # In case A is not sorted, I use the sorted() python function.
    # # That bumps up the time complexity to O(nlogn)
    # A = sorted(A)

    i = 0
    j = len(A) - 1

    while i < j:
        if (A[i] + A[j]) == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1

    return False


A = [-2, 1, 2, 4, 7, 11]
target = 13
print(two_sum_brute_force(A, target))
print(two_sum_hash_table(A, target))
print(two_sum_two_pointers(A, target))
