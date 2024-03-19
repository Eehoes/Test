import time
start_time = time.time() # 측정 시간



# 시작 시간 1:43

# N : 처음 숫자  K : 나눌 수 있는 숫자
N,K = map(int, input().split())

# N -> 1이 될때까지 연산해야 함. 
# K : N%K == 0이 될때만 사용 가능

# 연산 횟수
cnt = 0 
# N이 1이 아니라면 계속해서 진행
while N!=1 :
    # N % K == 0 일때
    if((N%K)==0) :
        N = N/K
        cnt += 1
    else : 
        N -= 1
        cnt += 1
    
print(cnt)

# 다 푼 시간 1:52 

end_time = time.time()
print()
print("Time :", end_time-start_time)
