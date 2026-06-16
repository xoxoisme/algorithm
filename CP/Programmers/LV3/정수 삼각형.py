
def solution(triangle):
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]

# 모든 값을 비교해야하기에 bottom-up 방식
# ---
# 트라이앵글을 table로 활용(table 말고 그냥 triangle 자체로 해도 될 거 같아서 바꿈)

# 3행부터 계산해야하기에 range(len(triangle)-2, -1, -1) 반복 - i
#     해당 3행 쭉 돌 때까지 반복 - j
#         table[i][j] += (table[i+1][j], table[i+1][j+1]) 중에서 더 큰 값
    
# table[0][0]이 최대값