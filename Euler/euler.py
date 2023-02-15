def problemsixtysix():
    maxx = 900
    maxD = -1
    
    
    for D in range(29,1000):

        xrem = -1
        yrem = -1
        minimum = -1
        for x in range(maxx,100000):
            for y in range(1,100000):
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
        
                

problemsixtysix()