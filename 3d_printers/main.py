# import sys
#
# sys.stdin = open('./input.txt','r')

n = int(input())

p = 1
d = 0

if n == 1:
    print(1)
    exit()

while p*2 < n:
    p*=2
    d+=1

d+=2
print(d)
