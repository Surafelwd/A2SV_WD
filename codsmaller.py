n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
A, B, C = 0, 0, 0
ans = []
while B < m:
    if A < n and b[B] > a[A]:
        C += 1
        A += 1
    else:
        ans.append(C)
        B += 1
        if A == n:
            C = 0
            A = 0
print(" ".join(map(str, ans)))
