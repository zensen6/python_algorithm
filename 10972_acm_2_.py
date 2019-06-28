from sys import stdin, stdout

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]
    return

def next_permutation(n, A):
    i = n - 1
    while i > 0 and A[i-1] >= A[i]:
        i -= 1
    if i <= 0:
        return [-1]
    j = n - 1
    while j >= i and A[j] <= A[i-1]:
        j -= 1
    swap(A, i-1, j)
    A[i:] = reversed(A[i:])
    return A

n = int(stdin.readline())
s = stdin.readline()
a = [int(c) for c in s.split()]
np = next_permutation(n, a)
stdout.write(" ".join(map(str, np)) + "\n")