def Sequence(l):
    n = len(l)
    pos1abs = 0
    pos2abs = 0
    indicator = True
    for i in range(n - 1, 2, -1): #chains length
        for j in range(0, n + 1 - i): #chains first element
            flag = True
            pos1 = l[j]
            pos2 = l[j + i - 1]
            for k in range(j, j + i - 1): #specific chains elements
                if l[k] >= l[k + 1]:
                    flag = False
            if flag and pos1abs == 0:
                pos1abs = pos1
                pos2abs = pos2
            elif flag and pos1abs != 0:
                if pos2abs < pos1 or pos1abs > pos2:
                    return True
                else:
                    indicator = False
        if not indicator:
            return False

    return False


if __name__ == '__main__':
    list = [2, 15, 17, 12, 13, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 10, 3, 2]
    n = len(list)
    print(Sequence(list))