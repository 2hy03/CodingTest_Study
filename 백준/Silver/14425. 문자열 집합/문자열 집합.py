#14425.문자열 집합
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
s=set()
result=0
for _ in range(N):
    s.add(input())

for _ in range(M):
    txt=input()
    if txt in s:
        result+=1
        
print(result)