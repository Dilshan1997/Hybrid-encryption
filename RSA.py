import random
import sys

def keyGenaration(size=8):
    #1) genarate 2 large prime p,q(same bit)
    p*genaratePrime(size)
    q*genaratePrime(size)

    if not(isPrime(p) and isprime(q)):
        raise ValueError('Both number must be prime')
    elif p==q:
        raise ValueError('p and q cannot be equal')
    #2)compute n=pq and phi=(p-1)(q-1) phi=eular function
    n=p*q
    phi=(p-1)*(q-1)

    #3) select random integer "e" (1<e<phi) such that gcd(e,phi)=1
    e=random.randrange(1,phi)
    g=gcd(e,phi)
    while g!=1:
        e=random.randrange(1,phi)
        g=gcd(e,phi)

#4)Use extended eculid's algorithm to computer another unique integer "d" (1<d<phi) such that e.del(mod phi)
    d=multiplicativeInverse(e,phi)

#5) return public and private keys
#public key is (e,n) and private key is (d,n)
    return ((n,e),(d,n))

#Encryption

def encrypt(pk,plaintext):
    #1)obtain(n,e)
    n,e=pk
#2)message space[0,n-1]
#3)compute c=m^e(mod n)
    c=[(ord(char)**e)%n for char in plaintext]
    print(c)
#4) send "c" to other party
    return c

#decryption

def decrypt(pk,ciphertext):
    d,n=pk
    #5)m=c^d(mod n)
    m=[(chr(char**d )%n) for char in ciphertext]
    return m

def gcd(a,b):
    #eculids algorithm
    while b !=0:
        temp=a%b
        a=b
        b=temp
    return a

def multiplicativeInverse(a,b):
    #eculids extended algorithm
    x=0
    y=1
    lx=1
    ly=0
    oa=a
    ob=b

    while b!=0:
        q=a//b
        (a,b)=(b,a%b)
        (x,lx)=((lx-(q*x)),x)
        (y,ly)=((ly-(q*y)),y)

        if lx<0:
            lx+=ob
        if ly<0:
            ly+=oa
            return lx

#genarate prime number

def genaratePrime(keysize):
    while True:
        num=random.randrange(2**(keysize-1),2**(keysize))
        if isPrime(num):
            return num

def isPrime(num):
        if(num<2):
            return false #0,1 and negative numbers are not prime
        lowPrimes=[2,3,5,7,11,13,17,19,23,27,29,31,33,37,41,43,47,53,57,59,61,67,71,73,77,79,83,89,97,101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
                    601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                    701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
                   ]
        if num in lowPrimes:
            return True
        for prime in lowPrimes:
            if(num%prime==0):
                return False

            return millerRabin(num)

def millerRabin(n,k=7):
    if n<6:
        return [False,False,True,True,False,True][n]
    elif n & 1==0:
        return False
    else:
        s,d=0,n-1
        while d & 1==0:
            s,d=s+1,d>>1
            for a in random.sample(range(2,min(n-2,sys.maximize)),min(n-1,k)):
                x=pow(a,d,n)
                if x!=1 and x+1!=n:
                    for r in range(1,s):
                        x=pow(x,2,n)
                        if x==1:
                            return False
                        elif x==n-1:
                            a=0
                            break
                            if a:
                                return False
                return True





