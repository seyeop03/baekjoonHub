#빨간색 구슬이 먼저가고 차후 파란색 구슬이 따라올 경우와, 파란색 구슬이 먼저가고 차후 빨간색 구슬이 따라올 경우를 나누어 생각했다.
#위 경우만 생각하면 쌩구현 문제인듯
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = list(list(sys.stdin.readline().rstrip()) for _ in range(N))

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            red_pos = [i,j]
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            blue_pos = [i,j]
            arr[i][j] = '.'
        elif arr[i][j] == 'O':
            end_pos = [i,j]

q = deque()
q.append([red_pos, blue_pos, 0])

# 위,아래,좌,우
dx = [0,0,-1,1]
dy = [-1,1,0,0]


def dfs():
    while q:
        pos = q.popleft()
        r_y, r_x = pos[0][0], pos[0][1]
        b_y, b_x = pos[1][0], pos[1][1]

        if pos[2] >= 10:
            return -1
        
        for i in range(4): # 위,아래,좌,우
            r_ny, r_nx = r_y, r_x
            b_ny, b_nx = b_y, b_x

            if (i==0 and r_y<b_y) or (i==1 and r_y>b_y) or (i==2 and r_x<b_x) or (i==3 and r_x>b_x): # red가 먼저감
                chk = 0
                chk, r_ny, r_nx = red_first(i, r_ny, r_nx, chk)
                chk, b_ny, b_nx = blue_after(i, b_ny, b_nx, r_ny, r_nx, chk)
                
                if chk == 1:
                    return pos[2]+1
                elif chk == 0:
                    if r_x==r_nx and r_y==r_ny and b_x==b_nx and b_y==b_ny:
                        continue
                    else:
                        q.append([[r_ny, r_nx], [b_ny, b_nx], pos[2]+1])
                elif chk == -1:
                    continue
            else: # blue가 먼저감
                chk = 0
                chk, b_ny, b_nx = blue_first(i, b_ny, b_nx, chk)
                if chk != -1:
                    chk, r_ny, r_nx = red_after(i, r_ny, r_nx, b_ny, b_nx, chk)
                if chk == 1:
                    return pos[2]+1
                elif chk == 0:
                    if r_x==r_nx and r_y==r_ny and b_x==b_nx and b_y==b_ny:
                        continue
                    else:
                        q.append([[r_ny, r_nx], [b_ny, b_nx], pos[2]+1])
                elif chk == -1:
                    continue

    return -1
    

def red_first(i, r_ny, r_nx, chk):
    r_ny += dy[i]
    r_nx += dx[i]
    while arr[r_ny][r_nx] != '#':
        if arr[r_ny][r_nx] == 'O':
            chk = 1
            r_ny, r_nx = -1, -1
            break
        r_ny += dy[i]
        r_nx += dx[i]
    r_ny -= dy[i]
    r_nx -= dx[i]
    
    return chk, r_ny, r_nx

def blue_after(i, b_ny, b_nx, r_ny, r_nx, chk):
    b_ny += dy[i]
    b_nx += dx[i]
    while arr[b_ny][b_nx] != '#' and (b_ny!=r_ny or b_nx!=r_nx):
        if arr[b_ny][b_nx] == 'O':
            chk = -1
            b_ny, b_nx = -1, -1
        b_ny += dy[i]
        b_nx += dx[i]
    b_ny -= dy[i]
    b_nx -= dx[i]
    
    return chk, b_ny, b_nx

def blue_first(i, b_ny, b_nx, chk):
    b_ny += dy[i]
    b_nx += dx[i]
    while arr[b_ny][b_nx] != '#':
        if arr[b_ny][b_nx] == 'O':
            chk = -1
            b_ny, b_nx = -1, -1
        b_ny += dy[i]
        b_nx += dx[i]
    b_ny -= dy[i]
    b_nx -= dx[i]
    
    return chk, b_ny, b_nx

def red_after(i, r_ny, r_nx, b_ny, b_nx, chk):
    r_ny += dy[i]
    r_nx += dx[i]

    while arr[r_ny][r_nx] != '#' and (b_ny!=r_ny or b_nx!=r_nx):
        if arr[r_ny][r_nx] == 'O':
            chk = 1
            r_ny, r_nx = -1, -1
        r_ny += dy[i]
        r_nx += dx[i]

    r_ny -= dy[i]
    r_nx -= dx[i]

    return chk, r_ny, r_nx

result = dfs()

if result == -1:
    print(-1)
else:
    print(result)