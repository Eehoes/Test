# 23시 10분 시작 

# 맵의 크기 입력 받음

N = int(input())

# 어디로 이동할지 입력 받음. 개수 제한 없으므로 바로 list로
# R : 오른쪽 +1 / L : 왼쪽 -1 // U : 위 +1 / D : 아래 -1
map = input().split()

x,y = 1 # 시작점 (1,1)

for i in map :
    if(map[i]=='R') :
        if(x+map[i] == len(map)) :
            print()