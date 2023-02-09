import time

def recFib(n):
    if n == 0 or n == 1:
        return 1
    else:
        fib = recFib(n-2) + recFib(n-1)
        return fib

def dpFib(n):
    dp =[1,1]

    for i in range(2,n+1):
        dp.append(dp[i-1] + dp[i-2])

    return dp[n]

n = 100000
#sr = time.time()
#for i in range(n):
#    print(recFib(i))
#fr = time.time()


sdp = time.time()
#for i in range(n):
    #print(dpFib(i))
dp =[1,1]

for i in range(2,n+1):
    dp.append(dp[i-1] + dp[i-2])
    print(dp[i])
fdp = time.time()

print(f'Time recursion \nTime Dynamic Programming {fdp-sdp}secs')