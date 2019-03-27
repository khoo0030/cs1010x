#
# CS1010X --- Programming Methodology
#
# Mission 5
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

##def connect_ends(curve1, curve2):
##    curve_1_start_point = connect_rigidly(curve1, curve2)(0)

##    curve_2_start_point = connect_rigidly(curve1, curve2)(0.50)
##    curve_2_end_point = connect_rigidly(curve1, curve2)(1)
##
##    def connected_curve(t):
##        if (t < 0.5):
##            return connect_rigidly(curve1, curve2)(t)
##        else:
##            translate_x = x_of(curve_1_end_point) - x_of(curve_2_start_point)
##            translate_y = y_of(curve_1_end_point) - y_of(curve_2_start_point)
##            return translate(translate_x, translate_y)(connect_rigidly(curve1, curve2))(t)
##        
##    return connected_curve

def connect_ends(curve1, curve2):
    curve_1_end_point = connect_rigidly(curve1, curve2)(0.499)
    curve_2_start_point = connect_rigidly(curve1, curve2)(0.50)

    
    def connected_curve(t):
        if (t < 0.5):
            return connect_rigidly(curve1, curve2)(t)
        else:
            translate_x = x_of(curve_1_end_point) - x_of(curve_2_start_point)
            translate_y = y_of(curve_1_end_point) - y_of(curve_2_start_point)
            return translate(translate_x, translate_y)(connect_rigidly(curve1, curve2))(t)
        
    return connected_curve

draw_connected_scaled(200, connect_ends(arc, unit_line))
draw_connected_scaled(200, connect_ends(translate(5,5)(arc), translate(1,1)(unit_line)))

##draw_connected_scaled(10, connect_ends(arc, unit_line))

##draw_connected_scaled(200, arc)
##draw_connected_scaled(200, unit_line)
##draw_connected_scaled(200, connect_rigidly(arc, unit_line))



##c = connect_rigidly(arc, unit_line)(0.25)
##print(x_of(c))
##print(y_of(c))


##########
# Task 2 #
##########

def show_points_gosper(level, num_points, initial_curve):
    "your solution here!"
    pass

##########
# Task 3 #
##########

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends("your solution here"))
    return inner_gosperize

# testing
# draw_connected(200, your_gosper_curve_with_angle(10, lambda lvl: pi/(2+lvl)))
# draw_connected(200, your_gosper_curve_with_angle(5, lambda lvl: (pi/(2+lvl))/(pow(1.3, lvl))))
