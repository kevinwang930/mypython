# 有这样一道智力题：“某商店规定：三个空汽水瓶可以换一瓶汽水。小张手上有十个空汽水瓶，她最多可以换多少瓶汽水喝？”答案是 5 瓶，方法如下：先用 9 个空瓶子换3瓶汽水，喝掉 3 瓶满的，喝完以后 4 个空瓶子，用 3 个再换一瓶，喝掉这瓶满的，这时候剩 2 个空瓶子。然后你让老板先借给你一瓶汽水，喝掉这瓶满的，喝完以后用 3 个空瓶子换一瓶满的还给老板。如果小张手上有 n 个空汽水瓶，最多可以换多少瓶汽水喝？

input_array=[]
while 1:
    x = int(input())
    if x ==0:
        break
    input_array.append(x)


def count_rec(bottle):
    if bottle < 2:
        return 0
    elif bottle == 2:
        return 1
    d_inc,b_rem = divmod(bottle,3)
    return d_inc + count_rec(d_inc+b_rem)

result = map(count_rec,input_array)
for x in result:
    print(x)

