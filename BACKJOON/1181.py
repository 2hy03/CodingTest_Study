#1181.단어정렬
N=int(input())
word_list=[]
for _ in range(N):
    word_list.append(input())
    
word_list=list(set(word_list))

#길이에 따라, 사전순
word_list.sort(key=lambda x : (len(x),x))
for word in word_list:
    print(word)