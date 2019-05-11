'''Task 
Given an array, a, of n integers, print a's elements in reverse order as a
single line of space-separated numbers.

-----'''

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    for i in range(n-1,-1,-1):
        print(arr[i],end="")
        print(" ",end="")
