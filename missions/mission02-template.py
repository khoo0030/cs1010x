#
# CS1010X --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


###########
# Task 1a #
###########

def fractal(picture, n):
    if n == 1:
        return picture

    if n > 1:
        return beside(picture, fractal_split(picture, n))

def fractal_split(picture, n):
    if n > 1:       
        return fractal(stack(picture, picture), n-1)


# Test
# show(fractal(make_cross(rcross_bb), 3))
# show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here

###########
# Task 1b #
###########

def fractal_iter(picture, n):
    final_picture = picture;
    
    for i in range(1, n):
        final_picture = beside(picture, stack(final_picture, final_picture))
    
    return final_picture

# Test
# show(fractal_iter(make_cross(rcross_bb), 3))
# show(fractal_iter(make_cross(rcross_bb), 7))
# Write your additional test cases here


###########
# Task 1c #
###########

def dual_fractal(picture_1, picture_2, n):
    if n == 1:
        return picture_1

    if n > 1:
        return beside(picture_1, dual_fractal_split(picture_2, picture_1, n))
        

def dual_fractal_split(picture_1, picture_2, n):
    return dual_fractal(stack(picture_1, picture_1), stack(picture_2, picture_2), n-1)
       
        
def ping(n):
    if n == 0:
        return n
    else:
        print("ping")
        pong(n-1)

def pong(n):
    if n == 0:
        return n
    else:
        print("pong")
        ping(n-1)


# Test
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

###########
# Task 1d #
###########

def dual_fractal_iter(picture_1, picture_2, n):
    final_picture = 0

    for i in range(n):
        print(i, n-i)
        if i == 0:
            if (n-i)%2 == 0:
                last_column = stackn(2**(n-1), picture_2)
            if (n-i)%2 != 0:
                last_column = stackn(2**(n-1), picture_1)

            final_picture = last_column    

        if i > 0:
            if (n-i)%2 == 0:
                column = stackn(2**(n-i-1), picture_2)
            if (n-i)%2 != 0:
                column = stackn(2**(n-i-1), picture_1)
            
            final_picture = beside(column, final_picture)

    return final_picture
    

# Test
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

##########
# Task 2 #
##########

def mosaic(pic1, pic2, pic3, pic4):
    right = stack(pic1, pic2)
    left = stack(pic4, pic3)
    return beside(left, right)

def steps(right_top_pic, right_bottom_pic, left_bottom_pic, left_top_pic):
    top_layer = beside(stack(left_top_pic, blank_bb), blank_bb)
    second_layer = beside(stack(blank_bb, left_bottom_pic), blank_bb)
    third_layer = beside(blank_bb, stack(blank_bb, right_bottom_pic))
    fourth_layer = beside(blank_bb, stack(right_top_pic, blank_bb))

    #overlay(top_layer, overlay(second_layer, overlay(third_layer, fourth_layer)))

    #overlay(overlay(overlay(top_layer, second_layer), third_layer), fourth_layer)
    return overlay_frac(1/4, top_layer, overlay_frac(1/3, second_layer, overlay_frac(1/2, third_layer, fourth_layer)))

# Test
#show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))
