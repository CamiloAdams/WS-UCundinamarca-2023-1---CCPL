import sys

sys.stdin = open('./input.txt','r')

p, t = map(int, input().split())

dic = {}

for i in range(1,p+1):
    dic[i] = list()

while(True):
    try:
        a, b = map(int, input().split())
    except EOFError:
        break

    dic[a].append(b)

op = set()
for i in range(1,p+1):
    op.add(tuple(sorted(dic[i])))   
    
print(len(op))

