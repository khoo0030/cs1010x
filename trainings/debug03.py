def factorial(n):
    i = 1
    result = 1
    while i <= n:
        result = result * i
        i += 1
    return result

def factorial2(n):
    result = 1
    for i in range(1, n+1):
        print("n: " + str(n) + " ;i: " + str(i))
        result = result * i
    return result

def factorial3(n):
    if n==1:
        return 1

    else:
        return n * factorial(n - 1)
