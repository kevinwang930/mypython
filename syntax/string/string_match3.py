def cal(s):
    for length in range(len(s),-1,-1): #长度递减
        for index in range(0,len(s)-length+1):
            sub_string = s[index:length+index]
            if sub_string == sub_string[::-1]:
                return len(sub_string)
while True:
    try:
        a = input()
        if a:
            print(cal(a)) 
    except:
        break