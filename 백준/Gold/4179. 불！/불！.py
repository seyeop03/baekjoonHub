import sys
from collections import deque

def fire_bfs():

    while q1:
        y, x = q1.popleft()
        
        for pos in range(4):
            nx = x + dx[pos]
            ny = y + dy[pos]
            
            if nx < 0 or ny < 0 or nx >= cols or ny >= rows:
                continue
            if fire_visited[ny][nx] == 0:
                continue
            if fire_visited[ny][nx] == 1:
                fire_visited[ny][nx] = fire_visited[y][x] + 1
                q1.append((ny, nx))
        

def jihoon_bfs():
    
    while q2:
        y, x = q2.popleft()
        
        for pos in range(4):
            nx = x + dx[pos]
            ny = y + dy[pos]
            
            if nx < 0 or ny < 0 or nx >= cols or ny >= rows:
                print(jihoon_visited[y][x])
                return
            if jihoon_visited[ny][nx] == 0:
                continue
            
            if jihoon_visited[ny][nx] == 1:
                if jihoon_visited[y][x] + 1 < fire_visited[ny][nx] or (fire_visited[ny][nx]==1):
                    jihoon_visited[ny][nx] = jihoon_visited[y][x] + 1
                    q2.append((ny, nx))
                else:
                    jihoon_visited[ny][nx] = 0
    print("IMPOSSIBLE")

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

rows, cols = map(int, input().split())
arr = []
fire_visited = [[0]*cols for _ in range(rows)]
jihoon_visited = [[0]*cols for _ in range(rows)]
q1 = deque()
q2 = deque()

for row in range(rows):
    tmp = list(sys.stdin.readline().rstrip())
    for col, c in enumerate(tmp):
        if c == 'J':
            q2.append((row, col))
            jihoon_visited[row][col] = 1
            fire_visited[row][col] = 1
        elif c == 'F':
            q1.append((row, col))
            fire_visited[row][col] = 1
        elif c == '.':
            fire_visited[row][col] = 1
            jihoon_visited[row][col] = 1
          
fire_bfs()
jihoon_bfs()