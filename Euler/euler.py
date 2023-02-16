import math


def problemsixtysix():
    maxx = 2
    maxD = -1
    
    
    for D in range(3,4):

        xrem = -1
        yrem = -1
        minimum = -1
        for x in range(maxx,100000):
            for y in range(1,x):
                tmp = x**2-D*(y**2)
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
    n = 10**7
    ret = 0
    for k in range(1,n+1):
        value = 1/k
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
    L = [k for k in range(2,10**4)]
    print(L)

def Codedtrianglenumbers():
    f = open('/home/ale/Backup/py/Euler/p042_words.txt', 'r')
    words = f.read()
    f.close
    words = words.replace('"', '')
    L = words.split(',')

    generalcounter = 0

    trianglenumbers = [n*(n+1)/2 for n in range(1000)]

    for word in L:
        forsum = 0
        for letter in word:
            forsum += ord(letter)- ord('A')+1
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
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf
def distinctpowers():
    S = set()

    for a in range(2,101):
        for b in range(2,101):
            S.add(a**b)
    print(len(S))

def OrderedFractions():
    S = set()
    i = 0
    for n in range(1,1000000):
        for d in range(n,1000000):
            if compute_hcf(n,d) == 1 and n < d:
                S.add(n/d)
                print(S)
            i+=1
            #print(f'computing {i}')
    print(S)

def Powerdigitsum():
    v = str(2**1000)
    print(v)
    print('---------')
    summatory = 0
    for digit in v:
        print()
        summatory += int(digit)
    print(summatory)
    
def Pentagonnumbers():
    pentagon = [int(n*(3*n-1)/2) for n in range(1,5000)]
    pentagonDict = {}
    for i in pentagon:
        pentagonDict[i] = 0
    print('dict')
    minimum = math.inf
    i = 0
    for j in range(0,len(pentagon)):
        for k in range(j, len(pentagon)):
            if pentagon[j]+pentagon[k] in pentagonDict and abs(pentagon[k]-pentagon[j]) in pentagonDict:
                if abs(pentagon[k]-pentagon[j]) < minimum:
                    minimum = abs(pentagon[k]-pentagon[j])
                    print(f'partial {abs(pentagon[k]-pentagon[j])}')
            i+=1
            print(i, j)

    print(minimum)
def Triangularpentagonalhexagonal():
    z = 100000
    triangle = [int(n*(n+1)/2) for n in range(1,z)]
    pentagonal = [int(n*(3*n-1)/2) for n in range(1,z)]
    hexagonal = [int(n*(2*n-1)) for n in range(1,z)]


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
def calcualteDec(dec, summy = 0):
        
        match int(str(dec)[0]):
                
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
        return summy + calculateunit(int(str(dec)[1]))
def calculateunit(unit, summy = 0):

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
    for number in range(1,12):
        strnumber = str(number)
        if number > 100:
            pass
        elif number > 10:
            summy += calcualteDec(number)
        else:
            summy += calculateunit(number)
            
    print(summy)



Numberlettercounts()


