# 10시 24분 시작

# 맵 크기 입력
n,m = map(int,input().split())

# 플레이어 위치, 바라보고 있는 방향 입력
x,y,a = map(int,input().split())

# 맵 바다 or 육지 입력
list_map = [[0 for i in range(n)] for i in range(m)]

for i in range(m) :
    num = list(map(int, input().split()))
    
    for j in range(n) :
        list_map[i][j] = num[j]


# 바라보는 방향마다 갈 수 있는 곳이 다름.
list_north = [(1,1),(-1,1)]
list_south = [(1,-1),(-1,-1)]
list_west = [(-1,1),(-1,1)]
list_east = [(1,1),(1,-1)]

list_a = [list_north, list_east, list_south, list_west]
