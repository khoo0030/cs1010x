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
        return combiner (term(a), accumulate(combiner, base, term, next(a), next, b))
    
#print(accumulate(lambda x, y: x*y, 1, lambda x: x**2 + 1, 0, lambda x: x+2, 5))
#print(accumulate(lambda x, y: x+y, 1, lambda x: x**2 + 1, 0, lambda x: x+2, 5))
#print(accumulate(lambda x, y: x+y, 1, lambda x: x**2 + 1, 1, lambda x: x+2, 5))


#Q4:
def sum(term, a, next, b):
    combiner = lambda x,y: x+y
    base = 0
    return accumulate(combiner, base, term, a, next, b)

#print(sum(lambda x: x*2, 1, lambda x: x+1, 5))
#print(sum(lambda x: x*2, 0, lambda x: x+2, 10))
#print(sum(lambda x: x**2, 1, lambda x: x+1, 5))


#Q5:
def accumulate_iter(combiner, null_value, term, a, next, b):
    results = []
    
    while a <= b:
        results.append(term(a))
        a = next(a)
        
    results.append(null_value)
    
    print(results)

    # now we can combine from behind!
    while len(results) > 1:
        results[-2] = combiner(results[-2], results[-1])
        results.pop()
        print(results)
        
    return results[0]

#print(accumulate_iter(lambda x,y: x*y, 1, lambda x: x*x, 1, lambda x: x+1, 5))        
#print(accumulate_iter(lambda x,y: x+y, 1, lambda x: x*x, 1, lambda x: x+1, 5))
#print(accumulate_iter(lambda x,y: x+y, 0, lambda x: x*x, 1, lambda x: x+1, 5))


#python array:
#https://www.w3schools.com/python/python_arrays.asp
#results[-1] === last array element
#results[-2] === 2nd last array element ...and so on

#results.append(value) -> add value to array last element
#results.pop(position) -> remove element in array position (default last element)


#Q6:
def make_point(x, y):
    return (x,y)

def x_point(p):
    return p[0]
    
def y_point(p):
    return p[1]

#For running public test case, do not delete
#p1 = make_point(2, 3)

#Q7:
def make_segment(p1, p2):
    return (p1, p2)
    
def start_segment(s):
    return s[0]

def end_segment(s):
    return s[1]
    
#do not uncomment! this is for reference only.
p1 = make_point(2, 3)
p2 = make_point(5, 7)

#print(x_point(start_segment(make_segment(p1, p2))))
#print(y_point(start_segment(make_segment(p1, p2))))
#print(x_point(end_segment(make_segment(p1, p2))))
#print(y_point(end_segment(make_segment(p1, p2))))


#Q8:
def midpoint_segment(segment):
    start_point = start_segment(segment)
    end_point = end_segment(segment)

    start_point_x_coordinate = x_point(start_point)
    start_point_y_coordinate = y_point(start_point)

    end_point_x_coordinate = x_point(end_point)
    end_point_y_coordinate = y_point(end_point)

    mid_point_x_coordinate = (start_point_x_coordinate + end_point_x_coordinate) / 2
    mid_point_y_coordinate = (start_point_y_coordinate + end_point_y_coordinate) / 2
    
    return make_point(mid_point_x_coordinate, mid_point_y_coordinate)
    
#for running public test case, do not delete!
p1 = make_point(2, 3)
p2 = make_point(5, 7)
s = make_segment(p1, p2)

#print(x_point(midpoint_segment(s)))
#print(y_point(midpoint_segment(s)))
