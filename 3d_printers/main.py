import sys

sys.stdin = open('./input.txt','r')

n = int(input())

printers = 1
days = 0

if n == 1:
    print(1)
    exit()

while printers*2 < n:
    printers*=2
    days+=1

days+=2
print(days)
