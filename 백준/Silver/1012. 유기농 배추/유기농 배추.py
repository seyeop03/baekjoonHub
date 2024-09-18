#전형적인 dfs 문제이다.

import sys
sys.setrecursionlimit(2500)
def find():
    ret = 0
    for y in range(n):
        for x in range(m):
            if arr[y][x] and not checked[y][x]:
                dfs(x,y)
                ret+=1
    return ret

def dfs(x,y):
    checked[y][x] = True
    
    for pos in range(4):
        nx = x + dx[pos]
        ny = y + dy[pos]
        if nx<0 or ny<0 or nx>=m or ny>=n:
            continue
        if arr[ny][nx] and not checked[ny][nx]:
            dfs(nx,ny)    

answers = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]

T = int(input()) # test case 수

for _ in range(T):
    m, n, k = map(int, input().split()) # 가로, 세로, 배추심어진갯수
    arr = [[0]*m for _ in range(n)]
    checked = [[False]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    answers.append(find())
for answer in answers:
    print(answer)