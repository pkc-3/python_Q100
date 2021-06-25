# 행렬 2개가 주어졌을 때 곱할 수 있는 행렬인지 확인하고 곱할 수 있다면 그 결과를, 곱할 수 없다면 -1을 출력하는 프로그램을 만들어주세요.

# * 라이브러리는 사용을 금지합니다.

# 입력
# a = ([1, 2],  b = ([1, 0],
#      [2, 4])       [0, 3])
#
# 행렬의 곱
# a의 1행과 b의 1열을 곱한다 (1*1+2*0)= 1  => a의 1행과 b의 2열을 곱한다 (1*0+2*3)= 6 =>[1,6]
# a의 2행과 b의 1열을 곱한다 (2*1+4*0)= 2  => a의 2행과 b의 2열을 곱한다.(2*0+4*3)=12 =>[2,12]
#
# 출력
# ([1,6], [2,12])
def sol(a, b):
    c = []
    if len(a) == len(b[0]):
        for i in range(len(a)):
            c.append([0]*len(b[0]))

        for i in range(len(c)):
            for j in range(len(c[i])):
                for k in range(len(a[i])):
                    c[i][j] += a[i][k] * b[k][j]
        return c
    else:
        return -1


a = ([1, 2], [2, 4])
b = ([1, 0], [0, 3])

print(sol(a, b))
