# def solution(n, k):
#     answer = []
    
#     def dfs(n, visited, result):
#         if len(result) == n:
#             answer.append(result[:])
#             return
        
#         for i in range(1, n + 1):
#             if not visited[i]:
#                 visited[i] = True
#                 result.append(i)
#                 dfs(n, visited, result)
#                 result.pop()
#                 visited[i] = False
    
#     visited = [False] * (n + 1)
#     dfs(n, visited, [])

#     return sorted(answer)[k - 1]

# 순열을 모두 생성하고 정렬한 후, k번째 순열을 반환하므로 시간 복잡도는 𝑂(𝑛!)
# 순열을 모두 생성하지 않고, k번째 순열만 직접적으로 계산

# 규칙 찾기
# [1, 2, 3, 4]에서 k = 12
# 4! = 4 * 3 * 2 * 1 = 24
# [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], 
#  [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], 
#  [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], 
#  [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
# 4! -> 24 // 4 = 6번마다 앞자리가 바뀜
# 3! -> 6 // 3 = 2번마다 2번째 자리가 바뀜
# 2! -> 2 // 2 = 1번마다 3번째 자리가 바뀜
# 1! -> 1 // 1 = 마지막 숫자

import math

def solution(n, k):
    answer = []
    
    source = [i + 1 for i in range(n)] # [1, 2, 3, 4]         [1, 3, 4]            [1, 3]
    
    for i in range(n, 0, -1): # 4, 3, 2, 1
        every = math.factorial(i) // i # 4!(24) // 4 = 6      3!(6) // 3 = 2       2!(2) // 2 = 1
        idx = (k - 1) // every         # (12 - 1) // 6 = 1    (8 - 1) // 2 = 3     (2 - 1) // 1 = 1
        answer.append(source.pop(idx)) # [2]                  [2, 4]               [2, 4, 3]
        k -= idx * every               # 12 - (1 * 4) = 8     8 - (3 * 2) = 2      2 - (1 * 1) = 1
        
    return answer