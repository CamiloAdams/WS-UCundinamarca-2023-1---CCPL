import sys

sys.stdin = open('./input.txt','r')

n = int(input())
e = int(input())

songs = 0


dic = {}

for i in range(1,n+1):
    dic[i] = 0 

for i in range(0, e):
    l = list(map(int, input().split()))
    l.pop(0)
    if 1 in l:
        for villager in l:
            dic[villager]+=1
        songs+=1
    else:
        for villager in l:
            dic[villager]=songs
    
all_songs = list()

for i in range(1,n+1):
    if dic[i] == songs:
        all_songs.append(i)


for i in sorted(all_songs):
    print(i)

