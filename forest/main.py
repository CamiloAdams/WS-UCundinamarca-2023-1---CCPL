import sys

sys.stdin = open('./input.txt','r')
#
# i = int(input())
#
# days =  list(map(int, input().split()))
#
# counter = 0
#
# for day in days:
#     if day < 0:
#         counter+= 1
#
# print(counter)

p, t = map(int, input().split())


# print(p, t)

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

