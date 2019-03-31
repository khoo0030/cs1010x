## Q3:
def map(fn, seq):
    if seq == ():
        return ()
    else:
        return (fn(seq[0]), ) + map(fn, seq[1:])

x = (1, 2, -3, 4, 5, -6, 7)

square = lambda x: x * x
double = lambda x: x * 2
abs = lambda x: x if x > 0 else -x

##mystery_op = lambda x: double(square(x))
##print(map(mystery_op, x))

##mystery_op = lambda x: square(double(abs(x)))
##print(map(mystery_op, x))

##mystery_op = lambda x: double(square(abs(x)))
##print(map(mystery_op, x))

##mystery_op = lambda x: square(abs(double(x)))
##print(map(mystery_op, x))

##mystery_op = lambda x: double(abs(square(x)))
##print(map(mystery_op, x))

## none of the above returns (1, 8, 18, 32, 50, 72, 98)


# Q4:
## doing it iteratively
def square_odd_terms_iterative(tpl):
    result = ()
    for item in tpl:
        if (item%2 != 0):
            item = item ** 2
        result = result + (item,)
    return result

## doing it recursively use map()
def square_odd_terms(tpl):
    def square_odd_number(number):
        if (number%2 != 0):
            return number ** 2
        return number
    return map(square_odd_number, tpl)

##print(square_odd_terms((1, 2, 3, 4, 5)))
##print(square_odd_terms((2, 4, 6, 8, 10)))


# Q5:
def accumulate(fn, initial, seq):
    if seq == ():
        return initial
    else:
        return fn(seq[0],  accumulate(fn, initial, seq[1:]))

##print(accumulate(lambda x,y:(x, y), (), (1, 2, 3)))


# Q6:
def filter(pred, seq):
    if seq == ():
        return ()
    elif pred(seq[0]):
        return (seq[0],) + filter(pred, seq[1:])
    else:
        return filter(pred, seq[1:])

is_odd = lambda x : x%2 != 0
##print(filter(is_odd, (1, 2, 3, 4, 5)))

x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
##print(filter(isPrime, x))


# Q7:
minus = lambda x,y: x - y 
is_odd = lambda x: x%2 == 1 
square = lambda x: x**2

##print(accumulate(minus, 0,  map(square, filter(is_odd, tuple(range(6))))))

#Q7 explaination:
#tuple(range(6) = (0,1,2,3,4,5)
#filter(is_odd, tuple(range(6))) = (1,3,5)
#map(square, filter(is_odd, tuple(range(6)))) = (1,9,25)

#accumulate(minus, 0,  map(square, filter(is_odd, tuple(range(6)))))
# -> step: (1 - (9 - 25))
# -> final step: (1 - (-17))


# Q8:
def reverse(seq):
    if seq == ():
        return ()
    else:
        return reverse(seq[1:]) + (seq[0],)

def scale_seq(seq, factor):
    if seq == ():
        return ()
    else:
        return (seq[0] * factor,) + scale_seq(seq[1:], factor)

def wrong_copy_tree(tree):
    return tree

def is_leaf(item):
    return type(item) != tuple 

# doing it iteratively + recursively
def copy_tree(tree):
    new_tree = ()
    
    for i in tree:
        # recursively copy i *if it is a tuple*
        if isinstance(i, tuple):
          new_i = (copy_tree(i),)
        else:
          new_i = (i,)
        new_tree = new_tree + new_i
        
    return new_tree

##original = (1, 2, 3, 4)
##print((original is copy_tree(original)))
##print(copy_tree(original))

##original = (1, 2, (3, 4))
##print((original is copy_tree(original)))
##print(copy_tree(original))


# Q9:
def count_leaves(tree):
    if tree == ():
        return 0
    elif is_leaf(tree):
        return 1
    else:
        return count_leaves(tree[0]) + count_leaves(tree[1:])

x = ((1, 2), ((3, 4), (5, (6, 7), (8, 9))), (10, (11, 12)), (13, (14,), (16,), 17, 18, (19, 20)))

##print(count_leaves(x))


# Q10:
def to_str(tup):
    string = ''
    for item in tup:
        string = string + str(item)
    return string    
        
print(to_str(('c', 's', 1, 0, 1, 0, 's')))
print(to_str(('a', 'b', 'c')))
print(to_str((1, 2, 3)))
print(to_str((12, 345, 6)))

