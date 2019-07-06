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

##print(odd_even_sums((1, 3, 2, 4, 5)))
##print(odd_even_sums((1, )))

#Q7:
# n=number of disk
# src=source pole
# dsc=destination pole
# aux=auxillary pole
def hanoi2(n, src, dsc, aux):
    num_moves = 2**n - 1

    moves = ()

    if n%2 == 0:
        aux, dsc = dsc, aux

    for i in range(1, num_moves+1):
        if i%3 == 1:
            moves = moves + ((src, dsc),)
        if i%3 == 2:
            if i%2 == 0:
                moves = moves + ((src, aux),)
            else:
                moves = moves + ((aux, src),)
        if i%3 == 0:
            if (i/3)%2 != 0:
                moves = moves + ((dsc, aux),)
            else:
                moves = moves + ((aux, dsc),)

    return moves

def hanoi(n, src, dsc, aux):
    moves = []
    
    def move_tower(size, src, aux, dest, moves):
        if size == 1:
            print("move top disk from ", src, " to ", dest)
            return moves.append((src, dest))
        else:
            move_tower(size-1, src, dest, aux, moves)
            move_tower(1, src, aux, dest, moves)
            move_tower(size-1, aux, src, dest, moves)

        return moves    

    return tuple(move_tower(n, src, aux, dsc, moves))
    
##print(hanoi(1, 1, 2, 3))
##print(hanoi(1, 1, 3, 2))
##print(hanoi(3, 1, 3, 2))

def print_move(src, dest):
    print("move top disk from ", src, " to ", dest)

def move_tower(size, src, dest, aux):
    if size == 0:
        return True
    else:
        move_tower(size-1, src, aux, dest)
        print_move(src, dest)
        move_tower(size-1, aux, dest, src)
    
##move_tower(3, "src", "dest", "aux")

def move_tower2(size, src, aux, dest):
    if size == 1:
        print("move top disk from ", src, " to ", dest)
    else:
        move_tower2(size-1, src, dest, aux)
        move_tower2(1, src, aux, dest)
        move_tower2(size-1, aux, src, dest)

##move_tower2(3, "src", "dest", "aux")

def move_tower_iter(size, src, aux, dest):
    num_moves = 2**size - 1

    moves = ()

    if size%2 == 0:
        #size is even
        print("size is even")
        aux, dest = dest, aux
    else:
        print("size is odd")

    for i in range(1, num_moves+1):
        if i%3 == 1: # 1, 4, 7,...i+3
            print("move top disk from ", src, " to ", dest)
            moves = moves + ((src, dest),)
        if i%3 == 2: # 2, 5, 8,...i+3
            if i%2 == 0:
                print("move top disk from ", src, " to ", aux)
                moves = moves + ((src, aux),)
            else:
                print("move top disk from ", aux, " to ", src)
                moves = moves + ((aux, src),)
        if i%3 == 0: # 3, 6, 9,...i+3
            if (i/3)%2 != 0:
                print("move top disk from ", dest, " to ", aux)
                moves = moves + ((dest, aux),)
            else:
                print("move top disk from ", aux, " to ", dest)
                moves = moves + ((aux, dest),)

    return moves                
        
##move_tower_iter(3, "src", "aux", "dest")

