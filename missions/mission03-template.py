#
# CS1010X --- Programming Methodology
#
# Mission 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###########
# Task 1a #
###########
from math import *

def compose(f, g):
    return lambda x:f(g(x))

def thrice(f):
    return compose(f, compose(f, f))

def repeated(f, n):
    if n == 0:
        return identity
    else:
        return compose(f, repeated(f, n - 1))

# Your answer here:
# n = 6

###########
# Task 1b #
###########

identity = lambda x: x
add1 = lambda x: x + 1
sq = lambda x: x**2

# (i) print(thrice(thrice)(add1)(6))
# Explanation:
# 27 + 6 = 33
# - compose => f . f
# - thrice => f . f . f
# - thrice(thrice) => thrice(f . f . f) => f . 27 times


# (ii) print(thrice(thrice)(identity)(compose))
# Explanation:
# - returns function equivalent to compose


# (iii) print(thrice(thrice)(sq)(1))
# Explanation:
# (1**2)**27 = 1

# (iv) print(thrice(thrice)(sq)(2))
# Explanation:
# (2**2)**27 = 18014398509481984


###########
# Task 2a #
###########

##def combine(f, op ,n):
##    result = f(0)
##    for i in range(n):
##        result = op(result, f(i))
##        print("i: " + str(i) + "; result: " + str(result))
##    return result

def smiley_sum(t):
    def f(x):
        if x == 1:
            return 1
        else:
            return 2*(x**2)

    def op(x, y):
        return x + y

    n  = t+1

    # Do not modify this return statement
    return combine(f, op, n)

##S(1) = 1 => f(1)
##S(2) = 4 + 1 + 4 = 9 => 2*f(2) + f(1)
##S(3) = 9 + 4 + 1 + 4 + 9 = 27 => 2*f(3) + f(2)
##S(4) = 16 + 9 + 4 + 1 + 4 + 9 + 16 = 59 => 2*f(4) + f(3)
##S(5) = 25 + 16 + 9 + 4 + 1 + 4 + 9 + 16 + 25 = 109 => 2*f(5) + f(4)

#print(smiley_sum(1))
#print(smiley_sum(2))
#print(smiley_sum(5))

###########
# Task 2b #
###########

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def combine(f, op ,n):
    result = f(0)
    for i in range(n):
        result = op(result, f(i))
        print("i: " + str(i) + "; result: " + str(result))
    return result

def new_fib(n):
    def f(x):
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            return f(x)

    def op(x, y):
        return x + y

    return combine(f, op, n+1)

# Your answer here:

#fib
#f(0) = 0
#f(1) = 1
#f(2) = f(1) + f(0) = 1+0 = 1
#f(3) = f(2) + f(1) = 1+1 = 2
#f(4) = f(3) + f(2) = 2+1 = 3

#print(new_fib(1))
#print(new_fib(2))
#print(new_fib(3))
#print(new_fib(10))
