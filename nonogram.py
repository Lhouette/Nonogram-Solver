import time

def getAll(length, data, l):
    result = []
    if len(data) == 0:
        l += [-1]*length
        if length == -1:
            return [l[:-1]]
        return [l]
    for i in range(length-sum(data)-len(data)+2):
        result += getAll(length-i-1-data[0], data[1:], l+[-1]*i+[1]*data[0]+[-1])
    return result

def getOverlap(L):
    result = [0]*len(L[0])
    for i in range(len(L[0])):
        for j in range(len(L)):
            result[i] += L[j][i]
    for i in range(len(result)):
        if abs(result[i]) == len(L):
            result[i] = L[0][i]
        else:
            result[i] = 0
    return result

def update(L, data):
    result = []
    r = True
    for i in range(len(L)):
        for j in range(len(data)):
            if data[j] != 0 and data[j] != L[i][j]:
                r = False
        if r == True:
            result += [L[i]]
        else:
            r = True
    return result

def printGrid(grid, w, h):
    for i in range(h):
        for j in range(w):
            if grid[i*w+j] == 0:
                print('  ',end='')
            elif grid[i*w+j] == 1:
                print('██',end='')
            else:
                print('░░',end='')
        print()
    print('=='*50)

def getGrid(grid, b, n, w, h): #b = true --> Columns b = False --> Rows
    result = []
    if b:
        return grid[n*w:(n+1)*w]
    else:
        for i in range(h):
            result += [grid[w*i+n]]
        return result

bar = 0

print('='*30)
height = int(input('height : '))
t = time.time()
width = int(input('width : '))
grid = [0]*width*height
Columns = []
Rows = []
print('='*30)
for i in range(height):
    print('Row\t','[' ,i+1,']',end='',sep='')
    Columns += [getAll(width,list(map(int,input('\t:').split())),[])]
print('='*30)
for i in range(width):
    print('Column\t', '[' ,i+1,']',end='',sep='')
    Rows += [getAll(height,list(map(int,input('\t:').split())),[])]
print('='*50)
while True:
    data = []
    for i in range(height):
        Columns[i] = update(Columns[i],getGrid(grid, True, i, width, height))
        grid[width*i:width*(1+i)] = getOverlap(Columns[i])
    printGrid(grid, width, height)
    for i in range(width):
        Rows[i]=update(Rows[i],getGrid(grid, False, i, width, height))
        data = getOverlap(Rows[i])
        for j in range(height):
            grid[j*width+i] = data[j]
    printGrid(grid, width, height)
    if grid.count(0) == 0:
        break
print('\n'+'='*50)
print('계산이 완료되었습니다. 경과된 시간 :', time.time()-t, 's')
printGrid(grid, width, height)
input('Enter를 눌러 종료합니다.')

