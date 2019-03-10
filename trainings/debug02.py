##def p1(x, y):
##    return p2(x, y) + p3(x, y)
##
##def p2(z, w):
##    return z * w
##
##def p3(a, b):
##    return p2(a) + p2(b)

def area(x, y):
    return 1/2 * x * y

def remainder(larger, smaller):
    #k = larger / smaller
    #return larger - k * smaller
    return larger % smaller

def sums(n):
    i = 0
    result = 0
    
    while i <= n:
        result = result + i
        i = i + 1
        
    return result

def average(x1, x2):
    return (x1 + x2) / 2
