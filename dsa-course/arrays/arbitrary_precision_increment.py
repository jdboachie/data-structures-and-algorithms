A1 = [1, 4, 9]
A2 = [9, 9, 9]

def plus_one(A: list[int]) -> list[int]:
    A[-1] += 1
    
    for i in reversed(range(1, len(A))):
        if A[i] != 10: break
        A[i] = 0
        A[i-1] += 1
    
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


print(plus_one(A1))
print(plus_one(A2))