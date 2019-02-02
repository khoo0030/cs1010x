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
    top = make_row(picture, n);
    bottom = make_row(picture, n);
    middle = make_middle(picture, n);

    stack_middle_on_bottom = stack_frac((n-2)/(n-1), middle, bottom)

    stack_top_on_middle_and_bottom = stack_frac(1/n, top, stack_middle_on_bottom)
    
    return stack_top_on_middle_and_bottom;

def make_row(picture, n):
    return quarter_turn_left(stackn(n, quarter_turn_right(picture)))

def make_middle(picture, n):
    right = quarter_turn_right(make_middle_sides(picture, n))
    left = quarter_turn_right(make_middle_sides(picture, n))
    center = quarter_turn_right(picture)

    stack_center_on_right = stack_frac((n-2)/(n-1), center, right)

    stack_left_on_center_and_right = stack_frac(1/n, left, stack_center_on_right)
        
    return quarter_turn_left(stack_left_on_center_and_right)

def make_middle_sides(picture, n):
    return stackn(n-2, picture)





# Test
#show(egyptian(make_cross(rcross_bb), 5))
