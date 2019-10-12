import turtle
#using Sieve of Eratosthenes find the prime numbers up until a number n
def primes(n):
    primeList = []
    for i in range (2,n):
        primeList.append(i)
    for i in primeList:
        for j in range (2,n):
            if j%i==0 and j!=i and j in primeList:
                primeList.remove(j)
    return primeList

#Question 3: Creating a visualization of the prime numbers
def primespic(n):
    g = primes(n)
    window = turtle.Screen()
    window.bgcolor("light blue")
    window.title("prime visualization")
    miriam = turtle.Turtle()
    for i in g:
        f = i
        miriam.forward(f)
        miriam.left(90)
    window.exitonclick()

primespic(17)
