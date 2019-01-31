#
# CS1010X --- Programming Methodology
#
# Mission 1 - Side Quest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

##########
# Task 1 #
##########

def egyptian(picture, n):
    b = make_horizontal(quarter_turn_left(picture), n)
    a = quarter_turn_left(make_middle_section(picture, n))
    
    c = stack_frac((n-1)/n, a, b)
    d = stack_frac(1/n, b, c)
    return quarter_turn_right(d)

def make_middle_section(picture, n):
    bottom = make_horizontal(picture, n-2)
    top = make_horizontal(picture, n-2)
    return stack_frac(1/n, top, stack_frac((n-1)/n, picture, bottom))

def make_horizontal(picture, n):
    return quarter_turn_left(stackn(n, quarter_turn_right(picture)))



# Test
#show(egyptian(make_cross(rcross_bb), 5))
