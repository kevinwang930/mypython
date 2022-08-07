# 输入一个表达式（用字符串表示），求这个表达式的值。
# 保证字符串中的有效字符包括[‘0’-‘9’],‘+’,‘-’, ‘*’,‘/’ ,‘(’， ‘)’,‘[’, ‘]’,‘{’ ,‘}’。且表达式一定合法。 



# 3+2*{1+2*[-4/(8-6)+7]}

def parse(v_str):
    str1 =  parse_brace(v_str)
    return parse_bracket(str1)

def parse_brace(v_str):
    brace_begin = v_str.find('{')
    if brace_begin == -1:
        return v_str
    else:
        brace_end = v_str.find('}',brace_begin)
    return parse_bracket(v_str[0:brace_begin]) + str(eval(parse_bracket(v_str[brace_begin+1:brace_end]))) +parse_brace(v_str[brace_end+1:])

def parse_bracket(v_str):
    bracket_begin = v_str.find('[')
    if bracket_begin == -1:
        return v_str
    else:
        bracket_end = v_str.find(']',bracket_begin)
        return v_str[0:bracket_begin] +str(eval(v_str[bracket_begin+1:bracket_end]))+str(parse_bracket(v_str[bracket_end+1:]))


try:
    input_str = input()
    parse_result = parse(input_str)
    print(eval(parse_result))
except Exception as e:
    print(e)


express = input()
express = express.replace("[", "(")
express = express.replace("{", "(")
express =express.replace("]", ")")
express =express.replace("}", ")")
print(eval(express))
