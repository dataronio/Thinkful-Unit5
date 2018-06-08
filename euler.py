# Euler 1 sum of multiples of 3 or 5 less than 1000
nums = [x for x in range(1000) if x%3==0 or x%5==0]
print(sum(nums))

# Euler2 sum of even fibonacci sequence terms less than 4million

ans = 0
f1 = 1
f2 = 2
while f1 < 4000000:
    if f1 % 2 == 0:
        ans += f1
    f1,f2 = f2, f1+f2

print(ans)

# euler 3 find largest prime factor of number
# repeat dividing by the smallest prime of number n will eventually get the largest prime factor
from math import sqrt

n = 600851475143
#n = 13195
while True:
    pr = 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % int(i) == 0:
            pr = int(i)
            print(pr)
            break
    if pr == 0:
        pr = n
    if pr < n:
        n = n // pr
        print(n)
    else:
        pr = n
        break

print("final prime is",pr)

# euler 4 largest palindrome made from the product of two 3-digit numbers

palindromes = [i * j for i in range(100,1000) for j in range(100,1000) if str(i * j) == str(i * j)[::-1] ]

print(max(palindromes))

# euler 5 What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# we will repeatedly compute the lcd of two numbers from 1 to 20. using fractions gcd function

import fractions
out = 1
for i in range(1, 21):
    out = (out*i // fractions.gcd(i, out) )

print("answer is ",out)

# euler 6 Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

numlist = [x for x in range(1,101)]
ssum = sum(numlist)**2
sumsq = sum([x*x for x in numlist])

print("diff of sum squares and square of sum is ", ssum-sumsq)

# euler 7 

def isprime(num):
    if num >= 2:
        for i in range(2, int(num ** 0.5)+1):
            if not ( num % i ):
                return False
    else:
        return False
    return True

#print(isprime(13),isprime(9),isprime(14),isprime(2),isprime(3))

count = 6
num = 13
while True:
    num += 2
    if isprime(num):
        count += 1
        if count == 10001:
            break

print("10001 prime is ", num)

# Euler 8 adjacent number product of large number

NUM = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
NUMADJ = 13

def adjproduct(num):
    prod = 1
    for item in num:
        prod *= int(item)
    return prod

adjprods = [adjproduct(NUM[i:i+NUMADJ]) for i in range(len(NUM)-NUMADJ+1)]

print("max 13 adj product is ",max(adjprods))

# Euler 9 get pythag3
answer = 0
for a in range(1,1001):
    for b in range(1,1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            answer = a*b*c

print("the triple is ", answer)


# euler 10 sum the primes below 2000000

count = 2
num = 3
primes = [2,3]
while num < 2000000:
    num += 2
    if isprime(num):
        #count += 1
        primes.append(num)

print("sum of primes below 2 million is ",sum(primes))
