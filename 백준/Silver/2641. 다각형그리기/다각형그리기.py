N = int(input())
data = list(map(int, input().split()))

# 반대 방향(숫자를 바꾸면서, 순서도 바뀜)
reversemap = {1: 3, 3: 1, 2: 4, 4: 2}
data_R = [reversemap[x] for x in reversed(data)]

M = int(input())
result = []

for _ in range(M):
    c = list(map(int, input().split()))
    original_c = c[:]  # c의 원본을 복사

    for _ in range(N):
        if c == data or c == data_R:
            result.append(original_c)
            break
        c.append(c.pop(0))  # 리스트 회전

print(len(result))
for r in result:
    print(*r)
