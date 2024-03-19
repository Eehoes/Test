# 21시 15분 시작

input_data = input()

# 숫자로 바꿔주기 x : 가로 y : 세로
x = ord(input_data[0])
y = int(input_data[1])

# a1 -> a : 가로 , 1 : 세로
# x : 가로, y : 세로

# 가능한 수, 정답
cnt = 0

move_x =[2,2,-2,-2,1,1,-1,-1]
move_y =[(1),(-1),(1),(-1),(2),(-2),(2),(-2)]


for i in range(8) :
    if(x+move_x[i]>=97 and x+move_x[i]<= 104 and y+move_y[i]>=1 and y+move_y[i]<=8) :
        cnt += 1
        

print(cnt)

# 21시 56분 끝
# x,y = [] 형식이 되는 줄 알았는데 아니었다. 하나씩 해야 한다는 걸 알게됨
# 잊지 말자 ord('a') -> 영어의 아스키코드로 변경이 가능하다는 것.
# 반대로 chr(97) -> 입력된 아스키코드에 맞는 영어가 출력이 된다. 