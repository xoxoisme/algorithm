# Algorithm

PS

## 컨벤션

```text
파일명: [번호]-[문제 이름].py
```

---

## 언어

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![C](https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=white)](https://en.cppreference.com/w/c)
[![Java](https://img.shields.io/badge/Java-007396?style=flat-square&logo=openjdk&logoColor=white)](https://www.java.com/)

## 이용 사이트

[백준](https://www.acmicpc.net/)
[프로그래머스](https://programmers.co.kr/)

## 학습 정리

[PS 정리 노션](https://cypress-orangutan-125.notion.site/PS-36d89525f86280c78fd0cf19626d70c8?source=copy_link)

## 슈도 코드

```python

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
```

- 코드를 작성하기 전, 항상 자연어로 코드 형태로 작성한다.
- 다만, 짧은 코드는 제외한다.