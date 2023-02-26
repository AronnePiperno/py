import math


def problemsixtysix():
    maxx = 2
    maxD = -1

    for D in range(3, 4):

        xrem = -1
        yrem = -1
        minimum = -1
        for x in range(maxx, 100000):
            for y in range(1, x):
                tmp = x ** 2 - D * (y ** 2)
                if tmp == 1:
                    minimum = tmp
                    xrem = x
                    yrem = y

            if minimum != -1:
                if maxx < xrem and xrem > 0:
                    maxx = xrem
                    maxy = yrem
                    maxD = D
                    print(f'{maxx}^2-{maxD}*{yrem}={minimum}')
                    break
            print(f'current D {D} maxxx {maxx}')

    print(f'{maxx} {maxD} {maxy} {minimum}')


def ndigitreciprocals():
    n = 10 ** 7
    ret = 0
    for k in range(1, n + 1):
        value = 1 / k
        print(value)
        try:
            v = int(value[n])
            print(v, k)
        except:
            v = 0
        ret += v

    print(ret)


def SquaretheSmallest():
    thedict = {}
    L = [k for k in range(2, 10 ** 4)]
    print(L)


def Codedtrianglenumbers():
    f = open('/home/ale/Backup/py/Euler/p042_words.txt', 'r')
    words = f.read()
    f.close
    words = words.replace('"', '')
    L = words.split(',')

    generalcounter = 0

    trianglenumbers = [n * (n + 1) / 2 for n in range(1000)]

    for word in L:
        forsum = 0
        for letter in word:
            forsum += ord(letter) - ord('A') + 1
        if forsum in trianglenumbers:
            generalcounter += 1
        print(forsum)

    print(generalcounter)


def compute_hcf(x, y):
    # choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf


def distinctpowers():
    S = set()

    for a in range(2, 101):
        for b in range(2, 101):
            S.add(a ** b)
    print(len(S))


def OrderedFractions():
    S = []
    i = 0
    for n in range(1, 9):
        for d in range(n, 9):
            if compute_hcf(n, d) == 1 and n < d:
                S.append(f'{n}/{d}')
            i += 1
            print(f'computing {i} {n}')
    print(S)


def Powerdigitsum():
    v = str(2 ** 1000)
    print(v)
    print('---------')
    summatory = 0
    for digit in v:
        print()
        summatory += int(digit)
    print(summatory)


def Pentagonnumbers():
    pentagon = [int(n * (3 * n - 1) / 2) for n in range(1, 5000)]
    pentagonDict = {}
    for i in pentagon:
        pentagonDict[i] = 0
    print('dict')
    minimum = math.inf
    i = 0
    for j in range(0, len(pentagon)):
        for k in range(j, len(pentagon)):
            if pentagon[j] + pentagon[k] in pentagonDict and abs(pentagon[k] - pentagon[j]) in pentagonDict:
                if abs(pentagon[k] - pentagon[j]) < minimum:
                    minimum = abs(pentagon[k] - pentagon[j])
                    print(f'partial {abs(pentagon[k] - pentagon[j])}')
            i += 1
            print(i, j)

    print(minimum)


def Triangularpentagonalhexagonal():
    z = 100000
    triangle = [int(n * (n + 1) / 2) for n in range(1, z)]
    pentagonal = [int(n * (3 * n - 1) / 2) for n in range(1, z)]
    hexagonal = [int(n * (2 * n - 1)) for n in range(1, z)]

    pentagonalDict = {}
    hexagonalDict = {}

    for i in pentagonal:
        pentagonalDict[i] = 0

    for i in hexagonal:
        hexagonalDict[i] = 0
    L = []
    for n in triangle:
        if n in pentagonalDict and n in hexagonalDict:
            L.append(n)
    print(L)


def calculateCent(cent):
    if cent == 1000:
        return 11
    if cent % 100 == 0:
        return calculateunit(int(str(cent)[0])) + 7
    summy = 0
    match int(str(cent)[0]):
        case 1:
            summy += 3 + 10 + calcualteDec(int(str(cent)[1:]))
        case 2:
            summy += 3 + 10 + calcualteDec(int(str(cent)[1:]))
        case 3:
            summy += 5 + 10 + calcualteDec(int(str(cent)[1:]))
        case 4:
            summy += 4 + 10 + calcualteDec(int(str(cent)[1:]))
        case 5:
            summy += 4 + 10 + calcualteDec(int(str(cent)[1:]))
        case 6:
            summy += 3 + 10 + calcualteDec(int(str(cent)[1:]))
        case 7:
            summy += 5 + 10 + calcualteDec(int(str(cent)[1:]))
        case 8:
            summy += 5 + 10 + calcualteDec(int(str(cent)[1:]))
        case 9:
            summy += 4 + 10 + calcualteDec(int(str(cent)[1:]))

    return summy


def calcualteDec(dec, summy=0):
    if len(str(dec)) < 2:
        return calculateunit(dec)

    if dec > 10 and dec < 20:
        match dec:
            case 11:
                return 6
            case 12:
                return 6
            case 13:
                return 8
            case 14:
                return 8
            case 15:
                return 7
            case 16:
                return 7
            case 17:
                return 9
            case 18:
                return 8
            case 19:
                return 8

    match int(str(dec)[0]):
        case 0:
            summy += 0
        case 1:
            summy += 3
        case 2:
            summy += 6
        case 3:
            summy += 6
        case 4:
            summy += 5
        case 5:
            summy += 5
        case 6:
            summy += 5
        case 7:
            summy += 7
        case 8:
            summy += 6
        case 9:
            summy += 6
    return calculateunit(int(str(dec)[1]), summy)


def calculateunit(unit, summy=0):
    match unit:
        case 0:
            summy += 0
        case 1:
            summy += 3
        case 2:
            summy += 3
        case 3:
            summy += 5
        case 4:
            summy += 4
        case 5:
            summy += 4
        case 6:
            summy += 3
        case 7:
            summy += 5
        case 8:
            summy += 5
        case 9:
            summy += 4

    return summy


def Numberlettercounts():
    summy = 0
    for number in range(1, 1001):
        if number >= 100:
            summy += calculateCent(number)
        elif number >= 10 and number < 100:
            summy += calcualteDec(number)
        else:
            summy += calculateunit(number)

    print(summy)


def ConcealedSquare():
    n = 1010064540
    for i in range(n, n * 10, 10):
        n = i ** 2
        stri = str(n)
        j = 1
        for k in range(0, 20, 2):
            if int(stri[k]) == j:
                if j == 9:
                    j = 0
                elif j == 0:
                    print(f'found {i}')
                    return i
                else:
                    j += 1
            else:
                break
        print(i)


def LargeSum():
    f = open('/home/def/Backup/py/Euler/numbers.txt', 'r')
    L = f.read()
    f.close()

    L = L.split('\n')

    summy = 0
    for n in L:
        try:
            summy += int(n)
        except:
            pass
    print(str(summy)[:10])


def NamesScores():
    f = open('/home/def/Backup/py/Euler/p022_names.txt', 'r')
    names = f.read()
    f.close()

    names = names.replace('"', '')
    names = names.split(',')
    names.sort()
    print(names)
    summy = 0
    i = 0
    for name in range(0, len(names)):
        tmp = 0
        for let in names[name]:
            tmp += ord(let) - ord('A') + 1
        summy += tmp * (name + 1)
        # i+= 1
        # print(i)
    print(summy)


def prime_eratosthenes(n):
    prime_list = set()
    isprime = []
    for i in range(2, n + 1):
        if i not in prime_list:
            isprime.append(i)
            for j in range(i * i, n + 1, i):
                prime_list.add(j)
    return isprime


def Reversibleprimesquares():
    prime = prime_eratosthenes(50000000)
    squareprime = set()
    for num in prime:
        squareprime.add(num ** 2)
    print('Done')
    summy = 0
    j = 0
    for n in squareprime:
        if str(n) != str(n)[-1::-1]:
            if int(str(n)[-1::-1]) in squareprime:
                summy += n
                j += 1
                print(int(str(n)[-1::-1]), n)
                if j == 50:
                    print(f'50 {summy}')
                    return

    print(j, summy)


def powerful_digit_counts():
    counter = 0
    i = 0
    for n in range(1, 1000):
        for exp in range(1, 1000):
            str_num = str(n**exp)
            if len(str_num) == exp:
                counter += 1
            i += 1
            print(i)

    print(counter)


powerful_digit_counts()
