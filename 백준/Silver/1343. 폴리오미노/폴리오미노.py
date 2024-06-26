# 1343. 폴리오미노

input=input()
input=input.replace('XXXX','AAAA')
input=input.replace('XX','BB')

if 'X' in input:
    print(-1)
else:
    print(input)