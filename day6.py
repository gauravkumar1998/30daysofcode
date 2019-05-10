'''Task 
Given a string, s, of length n that is indexed from 0 to n-1, print its
even-indexed and odd-indexed characters as 2 space-separated strings on a
single line.

Note: 0 is considered to be an even index.

-----'''

k=int(input())
for z in range(0,k):
    s=input()
    n=len(s)
    for i in range(0,n):
        if i%2==0:
            print(s[i],end="")
    print(" ",end="")
    for j in range(0,n):
        if j%2!=0:
            print(s[j],end="")
    print("")
