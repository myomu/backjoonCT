# 서로 다른 부분 문자열의 개수

str_list = []
STRING = input()
length = len(STRING)
for i in range(1, length+1):
    for j in range(length): # length-i 로 계산하는 방법도 있다.
        if j+i <= length: # 이부분..5로 해서 처음에 틀림. 
            str_slice = STRING[j:j+i]
            str_list.append(str_slice)

str_list = set(str_list)
print(len(str_list))