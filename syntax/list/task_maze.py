# 定义一个二维数组 N*M ，如 5 × 5 数组下所示：


# int maze[5][5] = {
# 0, 1, 0, 0, 0,
# 0, 1, 1, 1, 0,
# 0, 0, 0, 0, 0,
# 0, 1, 1, 1, 0,
# 0, 0, 0, 1, 0,
# };


# 它表示一个迷宫，其中的1表示墙壁，0表示可以走的路，只能横着走或竖着走，不能斜着走，要求编程序找出从左上角到右下角的路线。入口点为[0,0],既第一格是可以走的路。


# 本题含有多组数据。

def passThrough(maze,r,c,steps):

    def getNextSteps():
        nextSteps = []
        if c_r > 0 and [c_r-1,c_c] not in steps and maze[c_r-1][c_c] != 1:
            nextSteps.append([c_r-1,c_c])
        if c_r < r and [c_r+1,c_c] not in steps and maze[c_r+1][c_c] != 1:
            nextSteps.append([c_r+1,c_c])
        if c_c >0 and [c_r,c_c-1] not in steps and maze[c_r][c_c-1] != 1:
            nextSteps.append([c_r,c_c-1])
        if c_c <c and [c_r,c_c+1] not in steps and maze[c_r][c_c+1] != 1:
            nextSteps.append([c_r,c_c+1])
        return nextSteps

    c_r,c_c = steps[-1]
    if c_c == c and c_r == r:
        return steps
    next_steps =getNextSteps()
    if len(next_steps) == 0:
        return False
    for step in next_steps:
        newSteps = steps[:]
        newSteps.append(step)
        s = passThrough(maze,r,c,newSteps)
        if s:
            return s
    return False

    



while True:
    try:
        r,c = [int(i) for i in input().split()]
        maze = [[] for _ in range(r)]
        for i in range(r):
            maze[i] =[int(j) for j in input().split()]
        steps = [[0,0]]
        s=passThrough(maze,r-1,c-1,steps)
        if s:
            for step in s:
                print(f'({step[0]},{step[1]})')
    except:
        break