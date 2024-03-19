# 책 풀이
input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,-2),(-2,1)]

result = 0
for step in steps :
    next_row = row + step[0]
    next_column = column + step[1]
    
    print("step[0] : ", step[0])
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8 :
        result += 1
        
print(result)

# 나는 그냥 97~ 104 로 시작을 하기 위해 굳이 숫자를 빼지 않았지만, 책에서는 가로도 1로 시작하게 하려고 ord('a') 를 빼줬다는 것에서 차이가 잇음
# steps = [(1,2),(3,4),(5,6)] 이런 형식으로 되어 있지만 결국
# steps = [1,2,3,4,5,6] 과 동일하다는 것을 알 수 있음. -> 틀린 상식
