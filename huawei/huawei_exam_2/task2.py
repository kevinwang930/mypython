# 报文相应时间

import sys



n = int(sys.stdin.readline().strip())
l =[]
for _ in range(n):
    t,mrc = [int(i) for i in sys.stdin.readline().strip().split()]
    if mrc < 128:
        rt = mrc
    else:
        bin_mrc = bin(mrc)[2:]
        rt = (int(bin_mrc[4:8],2)|0x10) << (int(bin_mrc[1:4],2)+3)

    l.append([t,rt])
# print(l)
start_time = l[0][0]
response_time = l[0][1]
responed = 0
for i in range(1,n):
    if l[i][0] >= response_time + start_time:
        print(response_time+start_time)
        responed = 1
        break
    elif (l[i][0]+ l[i][1]) < start_time+response_time:
             start_time = l[i][0]
             response_time = l[i][1]
if responed == 0:
    print(response_time+start_time)
