s = input()
start=end=index = 0
start_flag = 0
end_flag = 0
quoted = 0
token_list =[]

while index < len(s):
    # blank
    if s[index] == " ":
        if quoted == 1:
            pass
        elif start_flag == 0:
            pass
        else:
            end = index
            token_list.append(s[start:end])
            start_flag = 0
            
    elif s[index] == '"':
        if quoted == 1:
            end = index
            token_list.append(s[start:end])
            start_flag = 0
            quoted = 0
        else:
            start = index + 1
            start_flag = 1
            quoted = 1
    elif index == len(s) -1:
        if start_flag ==1:
            end = index + 1
            token_list.append(s[start:end])
            start_flag = 0
        else:
            token_list.append(s[index:])

    elif start_flag == 1:
            pass
    else:
        start = index
        start_flag = 1
    index +=1

print(len(token_list))
for e in token_list:
    print(e)


