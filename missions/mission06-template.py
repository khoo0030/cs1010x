#
# CS1010X --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from diagnostic import *
from hi_graph_connect_ends import *

# Mission 6 requires certain functions from Mission 5 to work.
# Do copy any relevant functions that you require in the space below:







# Do not copy any other functions beyond this line #
##########
# Task 1 #
##########

# Example from the mission description on the usage of time function:
# profile_fn(lambda: gosper_curve(1000)(0.1), 500)

# Choose a significant level for testing for all three sets of functions.

# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below

##print(profile_fn ( lambda : gosper_curve(10)(0.1), 50))

# Time measurements
#  <...your time measurements here...>
#  <...do for at least 5 times and take the average...>

##run 1: 2.1375000000000144
##run 2: 2.5328000000000017
##run 3: 2.049299999999976
##run 4: 2.0444000000000018
##run 5: 2.0496999999999876
##
##average: 2.16273999999999

# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below

##print(profile_fn(lambda: gosper_curve_with_angle(10 , lambda lvl : pi/4), 50))
    
#  <...your time measurements here...>
#  <...do for at least 5 times and take the average...>

##
##run 1: 1.5890999999999544
##run 2: 2.3456000000000032
##run 3: 2.5227999999999917
##run 4: 1.2124000000000024
##run 5: 3.1303999999999776
##
##average: 2.16005999999998

#
# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
    
        left_curve = rotate(theta)(curve_fn)
        right_curve = rotate(-theta)(curve_fn)
        
        return put_in_standard_position(connect_ends(left_curve, right_curve))
    return inner_gosperize

##print(profile_fn(lambda: your_gosper_curve_with_angle(10, lambda lvl : pi/4), 50))

#  <...your time measurements here...>
#  <...do for at least 5 times and take the average...>

##run 1: 45.49709999999996
##run 2: 44.56750000000004
##run 3: 45.23900000000003
##run 4: 68.3316
##run 5: 59.0446
##
##average: 52.535960000000006

# Conclusion:
#  <...your conclusion here...>

##gosper_curve and gosper_curve_with_angle are customised functions with average
##run time of 2.16
##
##your_gosper_curve_with_angle is a customizable function with average run time
##of 52.53
##
##customised functions run faster than customizable function

##########
# Task 2 #
##########

#  1) your explanation here
##yes. both rotate(angle) and joe_rotate(angle) output will be the same

#  2) your explanation here
##rotate computes the point once
##joe_rotate computes the point twice


##########
# Task 3 #
##########

def joe_rotate ( angle ):
    def transform ( curve ):
        def rotated_curve (t):
            x, y = x_of ( curve (t)), y_of ( curve (t))
            cos_a , sin_a = cos ( angle ), sin ( angle )
            return make_point ( cos_a *x - sin_a *y, sin_a *x + cos_a *y)
        return rotated_curve
    return transform


##print(x_of(gosper_curve(3)(0.5)))
##draw_connected_scaled(200, gosper_curve(5))

##original_rotate = rotate
##replace_fn (rotate , joe_rotate )

trace(x_of)
x_of(gosper_curve(1)(0.5))


#
# Fill in this table:
#
#                    level      rotate       joe_rotate
#                      1         3             3
#                      2         5             7
#                      3         7             15
#                      4         9             31
#                      5         11            63
#
#  Evidence of exponential growth in joe_rotate.
