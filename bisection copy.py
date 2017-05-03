import math

a = int(input("Enter your A : "))
b = int(input("Enter your B : "))
t = float(input("Enter your Tolerance : "))
iteration = 0
c = 1

while c > t:

    x = (a+b)/2.000000

    #ENTER FUNCTION HERE####################

    c = x - 2**(-x)

    #ENTER FUNCTION HERE####################

    if c < a:
        x = a
    if c > b:
        x = b

    c = math.fabs(c)

if c < t:
    print "This is your solution", c



