'''Task 
Given a base-10 integer, n, convert it to binary (base-2). Then find and print
the base-10 integer denoting the maximum number of consecutive 1's in n's
binary representation.

-----'''

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    c,max=0,0
    n = int(input())
    b=str(bin(n).replace("0b",""))
    for i in b:
        if i=="1":
            c+=1
            if c>=max:
                max=c
        elif i=="0":
            c=0
    print(max)
