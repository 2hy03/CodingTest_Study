S=int(input())

sum=0

for i in range(1,S+1):
    sum+=i

    if S<sum:
        print(i-1)
        break
    elif S==sum:
        print(i)
        break