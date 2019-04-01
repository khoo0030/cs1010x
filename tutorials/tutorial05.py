#Q1-4:
tup = (7, (6, 5, 4), 3, (2, 1))
##print(tup[3][1])

tup = (7, (6,), (5, (4,)), (3, (2, (1,))))
##print(tup[3][1][1][0])

tup = ((7), (6, 5, 4), (3, 2), 1)
##print(tup[3])

tup = (7, ((6, 5), (4,), 3, 2), ((1,),))
print(tup[2][0][0])

#Q5:
def even_rank(tup):
    new_tupple = ()

    i = 1
    for item in tup:
        if (i%2 == 0):
            new_tupple = new_tupple + (item,)
        i += 1
        
    return new_tupple

##print(even_rank((3, 1, 4, 3, 2, 3, 19, 7, -90)))
##print(even_rank((2,)))
##print(even_rank(('a', 'x', 'b', 'y', 'c', 'x', 'd', 'p', 'q')))

#Q6:
def odd_even_sums(val):
    sum_of_odd_ranks = 0
    sum_of_even_ranks = 0
    
    i = 1
    for item in val:
        if (i%2 == 0):
            sum_of_even_ranks = sum_of_even_ranks + item
        else:
            sum_of_odd_ranks = sum_of_odd_ranks + item
        i += 1
        
    return (sum_of_odd_ranks, sum_of_even_ranks)

print(odd_even_sums((1, 3, 2, 4, 5)))
print(odd_even_sums((1, )))

#Q7:
# n=number of disk
# src=source pole
# dsc=destination pole
# aux=auxillary pole
def hanoi(n, src, dsc, aux):
    #Write your code here
    pass

print(hanoi(1, 1, 2, 3))
print(hanoi(1, 1, 3, 2))

