def countingSort(arr):
    count = [0] * 100  
    for num in arr:
        count[num] += 1
    return count

n = int(input())
arr = list(map(int, input().split()))
result = countingSort(arr)
print(" ".join(map(str, result)))
