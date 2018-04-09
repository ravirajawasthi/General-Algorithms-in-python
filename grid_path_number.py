print("You Start form (0,0), Enter you destination in the form 'x y': ")
end = list(map(int, input().split()))
end_r, end_c = end[0], end[1]
print("Enter number of blocked paths : ")
blocked = []
for i in range(int(input())):
    end = input().split()
    blocked.append((int(end[0]), int(end[1])))
calculated = {}


def isValid(row, col):
    if row > end_r or col > end_c or (row, col) in blocked:
        return False
    return True


def isEnd(row, col):
    if row == end_r and col == end_c:
        return True
    return False


def solveGrid(row, col):
    if not isValid(row, col):
        return 0
    if isEnd(row, col):
        return 1
    if (row, col) in calculated.keys():
        return calculated[(row, col)]
    else:
        calculated[(row, col)] = solveGrid(row + 1, col) + solveGrid(row, col+1)
    return calculated[(row, col)]


print(solveGrid(0, 0))