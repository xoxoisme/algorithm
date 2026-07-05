# Algorithm

PS

## 컨벤션

```text
백준: [번호]-[문제 이름].py
프로그래머스: [문제 이름].py
```

---

## 언어

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![C](https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=white)](https://en.cppreference.com/w/c)
[![Java](https://img.shields.io/badge/Java-007396?style=flat-square&logo=openjdk&logoColor=white)](https://www.java.com/)

## 이용 사이트

[백준](https://www.acmicpc.net/)
<br>
[프로그래머스](https://programmers.co.kr/)

## 슈도 코드

```python

from collections import deque

def solution(n, edge):
    
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    distances = [-1] * (n+1)
    distances[1] = 0
    
    queue = deque([1])
    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if distances[next] == -1:
                distances[next] = distances[cur] + 1
                queue.append(next)
                
    max_dist = max(distances)
    return distances.count(max_dist)

# 최단 거리
# 모든 노드 가중치가 같음(bfs 가능)
# ---

# 그래프 생성
# dsts 배열 -1로 생성
# dsts 시작(1)은 0

# 큐(1) 생성
# 빌 때까지 반복
#     - popleft()
#     그래프에서 다음꺼 하나씩 꺼내서 반복
#         다음 꺼가 -1이라 방문 안했다면
#             - dsts[다음]에다가 dsts[현재]+1
#             - 큐에 넣기
        
# dsts에서 최대값 찾기
# dsts에서 최대값 카운트
```

- 코드를 작성하기 전, 항상 자연어로 코드 형태로 작성한다.
- 다만, 짧은 코드는 제외한다.

---

#### 깃 꼬여서 rebase 도중 2000년으로 잘못 설정, 수정은 했으나 아직 잔디 갱신이 안됨!