import time
start_time = time.time() # 측정 시간

# 시작 시간 24:25

#card[N행][M열]
N,M = map(int, input().split())

# 카드를 만듦 card[N][M]
card=[[0 for i in range(M)] for i in range(N)]

list_min=[]
max = 0

# 카드 입력을 받음 여기까진 문제X
for i in range(N) :
    num = list(map(int, input().split()))
    
    for j in range(M) :
        card[i][j] = num[j]   
               
    card[i].sort() # 정렬 시킴
    list_min.append(card[i][0])

    
list_min.sort()
max = list_min[N-1]

print(max) 

end_time = time.time()
print()
print("Time :", end_time-start_time)

# 다 푼 시간 24:53