N = int(input())
dasom = int(input())
li = [int(input()) for _ in range(N - 1)]
cnt = 0

if (N == 1):
  pass
else:
  while dasom <= max(li):
    dasom += 1
    cnt += 1
    li[li.index(max(li))] -= 1

print(cnt)