from math import *

def magnitude (x1 , y1 , x2 , y2 ):
    def square_of_difference(num1, num2):
        return (num1 - num2) ** 2

    def sum(num1, num2):
        return num1 + num2

    def squareroot(num):
        return num ** 0.5

    length = squareroot(sum(square_of_difference(x1, x2), square_of_difference(y1, y2)))

    return length

def area (base_length, height):
    return 0.5 * base_length * height

def area2(length_a, length_b, rad_ab):
    """
    Write your answer within these triple quotes
    Answer:
    Both cannot be a direct substitute for each other.
    area(a1, a2) takes in 2 arguments while area2(a1,a2,a3) takes in 3 arguments
    """
    return 0.5 * length_a * length_b * sin(rad_ab)

def area3 (x1 , y1 , x2 , y2 , x3 , y3 ):
    length_a = magnitude(x1, y1, x2, y2)
    length_b = magnitude(x1, y1, x3, y3)
    length_c = magnitude(x2, y2, x3, y3)

    print("length_a value: " + str(length_a))
    print("length_b value: " + str(length_b))
    print("length_c value: " + str(length_c))

    #s = 0.5 * (length_a + length_b + length_c)
    #area = (s * (s - length_a) * (s - length_b) * (s - length_c)) ** 0.5

    return herons_formula(length_a, length_b, length_c)

# Don't need to modify the following function
def herons_formula(a, b, c):
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))

def sqrt(num):
    return num ** 0.5

#round(area3(0, 0, 1, 1, 2, 0))
#round(area3(1, 1, 0, 0, 2, 0))






def foo1():
    i = 0
    result = 0
    
    while i < 10:
        result += i
        i += 1
        
    return result #i start at 0 => 1+2+3+4+5+6+7+8+9 => 45

def foo2():
    i = 0
    result = 0
    
    while i < 10:
        if i == 3:
            break
    
        result += i
        i += 1
        
    return result #i start at 0 => 0+1+2 => 3

def bar1():
    result = 0
    
    for i in range (10):
        result += i
        
    return result #i start at 0 => 0+1+2+3+4+5+6+7+8+9 => 45

def bar2():
    result = 0
    
    for i in range (10):
        if i % 3 == 1:
            continue
        
        result += i
        
    return result #i start at 0 => 0+2+3+5+6+8+9 => 33


def factorial(n):
    product = 1

    for i in range(1, n+1):
        product = product * i
                    
    return product

def sum_even_factorials(n):
    sum = 0

    for i in range(n+1):
        if i%2 != 0:
            continue

        sum += factorial(i)

    return sum

def f(g):
    return g(2)

def square(x):
    return x ** 2

