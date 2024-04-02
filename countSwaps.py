#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    count=0
    sorted= False
    while not sorted:
        sorted=True
        for i in range(n-1):
            if a[i]>a[i+1]:
                a[i], a[i+1]=a[i+1],a[i]
                count+=1
                sorted=False
        
    return count
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    swaps = countSwaps(a)
    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
    
