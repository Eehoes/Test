# 동전의 개수
cnt = 0

# 500, 100, 50, 10 동전이 존재.
coins = [500,100,50,10] 

# 거스름돈 1260 원
money = 1260

for coin in coins :
    cnt += money//coin # 거스름돈을 coins로 나눴을 때의 몫. 즉, 동전의 개수
    
    money %=coin

print(cnt)