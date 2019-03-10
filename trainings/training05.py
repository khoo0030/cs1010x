def compose(f, g):
    return lambda x: f(g(x))

#Q1:
#foo = lambda x: x+10
#compose(foo, foo)(3) = foo(foo(x)) = (x+10) + 10

#Q2:
#foo = lambda x: x+1
#bar = compose(foo, foo) = foo(foo(x)) 
#compose(bar, bar)(10) = foo(foo(foo(foo(x)))) = ((((12 + 1) + 1) + 1) + 1)

#Q3:
#thrice = lambda f: compose(compose(f, f), f) = f(f(f(x)))
#thrice(lambda x: x+1)(6) = (((x+1) + 1) + 1)

def times3(x):
    return x * 3

def add1(x):
    return x + 1

#Q4:
#three_x_plus_1 = compose(add1, times3)
#three_x_plus_1(1) = add1(times3(x))

#Q5:
def make_adder(n):
    return lambda x: x+n

#add1 = make_adder(1)
#make_adder(5)(10)

#Q6:
def is_same(x,y):
    return x == y

def make_verifier(key):
    return lambda x: is_same(x, key)

#check_password = make_verifier(262010771)
#check_password(262010771)

#Q7:
def fold(op, f, n):
    if n == 0:
        return f(0)
    else:
        return op(f(n), fold(op, f, n-1))

minus = lambda x, y: x-y
identity = lambda x: x

#fold(minus, identity, 4)
#n=4, minus(f(4), fold(minus, identity, 3))
#n=3, minus(f(3), fold(minus, identity, 2))
#n=2, minus(f(2), fold(minus, identity, 1))
#n=1, minus(f(1), fold(minus, identity, 0))
#n=0, f(0)
#(4 - (3 - (2 - (1-0)))) = 2

#Q8:
def fold(op, f, n):
    if n == 0:
        return f(0)
    else:
        return op(fold(op, f, n-1), f(n))

minus = lambda x, y: x-y
identity = lambda x: x

#fold(minus, identity, 4)
#n=4, minus(fold(minus, identity, 3), f(4))
#n=3, minus(fold(minus, identity, 2), f(3))
#n=2, minus(fold(minus, identity, 1), f(2))
#n=1, minus(fold(minus, identity, 0), f(1))
#n=0, f(0)
#((((0-1) - 2) -3) -4) = -10

#Q9:
def fold2(op, term, a, next, b, base):
    print("fold 2, a: " + str(a))
    print("fold 2, b: " + str(b))
    print("fold 2, base: " + str(base))
    
    if a > b:
        print("a > b case - terminate")
        print("------------")
        return base
    else:
        print("a < b case")
        print("fold 2, term(a): " + str(term(a)))
        print("fold 2, next(a): " + str(next(a)))
        print("------------")
        return op (term(a), fold2(op, term, next(a), next, b, base))

#op is the operator
#term is a function
#next is a function to increment a
#a is the starting
#b is the end
#base is the base case value

def sum(term, a, next, b):
    return fold2(lambda x,y: x+y, term, a, next, b, 0)


def product(term, a, next, b):
    return fold2(lambda x,y: x*y, term, a, next, b, 1)

def geometric_series(a, r, n):
    op = lambda x,y: x+y
    term = lambda x: a * r ** (x-1)
    next = lambda x: x+1
    base = 0
    print("geometric_series, a: " + str(a))
    print("geometric_series, r: " + str(r))
    print("geometric_series, n: " + str(n))
    print("------------")
    return fold2(op, term, 1, next, n, base)

#Q10:
import random

##def generate_random_4d_number():
##    is_run = True
##    generated_number = 0
##    
##    while is_run == True:
##        generated_number = int(round(random.random() * 10000))
##        if generated_number > 1000:
##            break
##
##    return generated_number

def generate_random_4d_number():
    return random.randint(0, 9999)

#Q11:
#n = number of items
#m = item combination number
def num_combination(n, m):
    print("n value: " + str(n) + " ; m value: " + str(m))
    if m==0:
        print("m is zero")
        print("---------")
        return 1
    elif n < m:
        print("n is less than m")
        print("---------")
        return 0
    else:
        print("recursion")
        return num_combination(n-1, m-1) + num_combination(n-1, m)
            
def choose(n,k):
  if k==0:
     return 1
  elif n<k:
     return 0
  else:
     return choose(n-1, k-1) + choose(n-1, k)

def cc(amount, kinds_of_coins):
    if amount == 0:
        return 1

    elif (amount < 0) or (kinds_of_coins == 0):
        return 0

    else:
        return cc(amount, kinds_of_coins - 1) + cc(amount - first_denomination(kinds_of_coins), kinds_of_coins) 

def first_denomination(kinds_of_coins):
    if kinds_of_coins == 5:
        return 50
    
    elif kinds_of_coins == 4:
        return 20

    elif kinds_of_coins == 3:
        return 10

    elif kinds_of_coins == 2:
        return 5

    elif kinds_of_coins == 1:
        return 1

def count_change(amount):
    return cc(amount, 5)

#geometric_series(1, 2, 4)
#1 + (1 * 2 ^ 1) + (1 * 2 ^ 2) + (1 * 2 ^ 3) = 15
#1 + (1*2)       + (1*2*2)     + (1*2*2*2)

#geometric_series(1/2, 1/2, 3)
#1/2 + (1/2 * 1/2) + (1/2 * 1/2 * 1/2)
