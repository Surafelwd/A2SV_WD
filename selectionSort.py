class Solution: 
    def selectionSort(self,arr, n):
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr
