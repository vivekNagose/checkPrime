def prime(n):
    for i in range(2, n+1):
        if (n%i) == 0:
            break
    if i==n:
        print('prime')
    else:
        print('not prime')

n=int(input())
prime(n)

#Input 3 Output prime
#Input 6 Output not prime