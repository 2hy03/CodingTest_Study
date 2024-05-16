
#import sys
#sys.stdin = open("input.txt", "r")
from collections import Counter

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    t=input()
	
    n_list=list(map(int, input().split()))
    count=Counter(n_list)
    print('#'+str(test_case),count.most_common()[0][0])

    
    # ///////////////////////////////////////////////////////////////////////////////////
