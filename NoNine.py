T = int(input())

for x in range(T):
    inp = str(input())
    inp = inp.split(' ')
    F = int(inp[0])
    L = int(inp[1])
    c = 0
    lastdiv = -1
    firstnine = False
    for i in range(F, L+1):
        tmp = str(i)
        ninebool = False
        for j in tmp:
            if j == '9':
                ninebool = True
                break
        
        if firstnine:       
            if lastdiv + 9 == i:
                    lastdiv = lastdiv+9
                    ninebool = True
            elif not ninebool:
                c += 1

        if not ninebool and not firstnine:
            if i % 9 == 0:
                lastdiv = i
                firstnine = True
            else:
                c += 1
    print('Case #{}: {}'.format(x+1, c))