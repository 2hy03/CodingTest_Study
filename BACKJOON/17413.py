#17413.단어뒤집기_구현

stack=[]
result=[]
string=input()
for i in range(len(string)):
    if string[i] == '<' and stack:  #stack에 요소가 있고, 열림괄호일때,
        stack.reverse()
        result.append(''.join(stack))
        stack=[string[i]]
    elif string[i] == '>':
        stack.append('>')
        result.append(''.join(stack))
        stack=[]
    elif string[i] == ' ' and '<' not in stack:   #괄호밖에서 여백
        stack.reverse()
        result.append(''.join(stack))
        result.append(' ')
        stack=[]
    else: 
        stack.append(string[i])
if stack:
    stack.reverse()
    result.append(''.join(stack))
print(''.join(result))