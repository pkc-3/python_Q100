# 원의 넓이는 `반지름의 길이 x 반지름의 길이 x 3.14`로 구할 수 있습니다.
# 함수를 사용하여 원의 넓이를 구하는 코드를 작성해봅시다.

# **입력을 반지름의 길이로 정수 n이 주어지면 원의 넓이를 반환하는 함수**를 만들어 주세요.
# (입력을 해야하기 때문에 input을 반드시 사용해야합니다)

# r = int(input("반지름 입력 : ")) 방법1


# def area():
#     round = r * r * 3.14
#     print(round)


# area()

def solution(n):
    return n * n * 3.14


print(solution(int(input("반지름 입력 : "))))
