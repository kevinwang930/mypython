
def getTokenStart():
    global index
    while True:
        if index == c_length:
            return -1
        
        if c_str[index] == " ":
            index+=1
        else:
            return index
        
def getTokenEnd():
    global index
    while True:
        if index == c_length:
            return index 
        if c_str[index] == ' ':
            index+=1
            return index -1
        else:
            index+=1
            
    

def getToken():
    
    start = getTokenStart()
    if start == -1:
        return -1
    token=''

    if c_str[start] == '"':
        start +=1
        end = c_str.find('"',start)
    else:
        end = getTokenEnd()
                            
        
    token = c_str[start:end]
    token_list.append(token)
def parse():
    while True:
        rv = getToken()
        if rv == -1:
            break
while True:
    try:
        token_list = []
        c_str = input()
        index = 0
        c_length = len(c_str)
        parse()
        print(len(token_list))
        for e in token_list:
            print(e)
    except:
        break