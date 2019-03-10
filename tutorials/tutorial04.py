#Q1:
def calc_integral(f, a, b, n):
    h = (b - a)/n

    def term(f, coefficent, a, h, k):
        print("k value: " + str(k))
        return coefficient * (f(a + (k*h)))

    result = 0

    for i in range(0, n+1):
        if i == 0 or i == n:
            coefficient = 1
            print("i first or last: " + str(i) + "; coefficient: " + str(coefficient) + "; k value: " + str(i))
            result += term(f, coefficient, a, h, i)
            
        if i != 0 and i != n:
            if i % 2 == 0:
                coefficient = 2
                print("i even: " + str(i) + "; coefficient: " + str(coefficient) + "; k value: " + str(i))
                result += term(f, coefficient, a, h, i)
                
            else:
                coefficient = 4
                print("i odd: " + str(i) + "; coefficient: " + str(coefficient) + "; k value: " + str(i))
                result += term(f, coefficient, a, h, i)
                
    return (h/3) * result

#calc_integral(lambda x: x*x*x, 0, 1, 100)


#Q2:
def fold(op, f, n):
    if n == 0:
        return f(0)
    return op(f(n), fold(op, f, n-1))

def g(k):
    op = lambda x,y: x*y
    f = lambda x: x - ((x+1)**2)

    return fold(op, f, k)
    
#print(g(0))
#print(g(3))
#print(g(8))


#Q3:
def accumulate(combiner, base, term, a, next, b):
    if a > b:
        print("a > b case - terminate")
        print("------------")
        return base
    else:
        print("a < b case")
        print("fold 2, term(a): " + str(term(a)))
        print("fold 2, next(a): " + str(next(a)))
        print("------------")
        return combiner (term(a), accumulate(combiner, term, next(a), next, b, base))
    return

accumulate(lambda x, y: x*y, 1, lambda x: x**2 + 1, 0, lambda x: x+2, 5)
accumulate(lambda x, y: x+y, 1, lambda x: x**2 + 1, 0, lambda x: x+2, 5)
accumulate(lambda x, y: x+y, 1, lambda x: x**2 + 1, 1, lambda x: x+2, 5)
