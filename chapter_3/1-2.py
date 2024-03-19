import time
start_time = time.time() # 측정 시간

# 시작
N,M,K = list(map(int, input().split()))

# N만큼의 배열 입력
list_n = list(map(int, input().split()))

# list_n 정렬
list_n.sort()

# 최대, 두 번째 구하기
max = list_n[N-1]
sec = list_n[N-2]

# max의 개수
cnt = 0 
sum = 0 
for i in list_n :
    if(max==list_n) :
        cnt+= 1
    
for i in range(N) : 
    if(cnt>1 or K==M) :
        sum = max*M
    else :
        sum = ((max*K+sec)*(K-1)+(M%(K+1))*max)

print(sum)

end_time = time.time()
print()
print("Time :", end_time-start_time)
print()