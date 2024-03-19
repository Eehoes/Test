# 17시 28분 시작

# 얼음틀 크기 입력 N : 행 / M : 열
N,M = map(int, input().split())

# 얼음틀 기본 0으로 채워주기 ice[n][m]
ice_list = [[0 for i in range (M)] for i in range (N)]

print(ice_list)

# 얼음틀 내부 입력받기 0 or 1 으로 
for i in range(N) : 
    ice = list(map(int , input().split()))
    
    for j in range(M) :
        ice_list[i][j] = ice[j]
     

# DFS를 사용해서 해결해야 한다는 것까지 알겠음.
# So, DFS 함수 정의 완료
def DFS(graph,v,visited) :
    visited[v] = True
    
    for i in graph[v] :
        if not visited[i] :
            DFS(graph, i, visited)
    





