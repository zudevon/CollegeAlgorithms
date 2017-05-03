def fibonacci_list(x):
    total = 1
    prevNum = 0
    #fibs = []
    print prevNum, total
    while x > total:
        prevNum += total
        actualNum = total + prevNum
        total = actualNum
        if total > x:
            print prevNum
        else:
            print prevNum, actualNum


n = input("Enter a number : ")

print fibonacci_list(n)

#0, 1, 1, 2 , 3, 5, 8, 13, 21, 34