import time
start_time = time.time() # 측정 시간

n,m,k = map(int,input().split())

data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

cnt = int(m / (k+1) * k)
cnt += m % (k+1)

result = 0
result += (cnt)* first
result += (m-cnt)*second

print(result)

end_time = time.time()
print()
print("Time :", end_time-start_time)