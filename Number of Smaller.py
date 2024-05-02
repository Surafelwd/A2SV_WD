t = int(input())

for _ in range(t):
    
    n = int(input())

     a = list(map(int, input().split()))

    b = 0

    sum=0
    while b< n:
        d=[]
        if a[b]<0:
            while b<n and a[b] <0:
                d.append(a[b])
                b+=1
        else:
            while b<n and a[b]>0:
                d.append(a[b])
                b+=1
        sum+=max(d)
        d.clear()
    print(sum)

