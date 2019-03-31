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

def connect_ends(curve1, curve2):
    def connected_curve(t):
        curve1_end_point = curve1(1)

        curve2_start_point = curve2(0)

        translate_x = x_of(curve1_end_point) - x_of(curve2_start_point)
        translate_y = y_of(curve1_end_point) - y_of(curve2_start_point)

        translated_curve2 = translate(translate_x, translate_y)(curve2)
        
        return connect_rigidly(curve1, translated_curve2)(t)
    return connected_curve

##draw_connected_scaled(200, connect_ends(arc, unit_line))
##draw_connected_scaled(200, connect_ends(translate(5,5)(arc), translate(1,1)(unit_line)))

##draw_connected_scaled(200, arc)
##draw_connected_scaled(200, unit_line)
##draw_connected_scaled(200, connect_rigidly(arc, unit_line))


##########
# Task 2 #
##########

def show_points_gosper(level, num_points, initial_curve):
    curve = repeated(gosperize, level)(initial_curve)
    
    squeezed_curve = squeeze_curve_to_rect(-0.5, -0.5, 1.5, 1.5)(curve)
    
    return draw_points(num_points, squeezed_curve)

##show_points_gosper(7, 1000, arc)
##show_points_gosper(5, 500, arc)

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
    
        left_curve = rotate(theta)(curve_fn)
        right_curve = rotate(-theta)(curve_fn)
        
        return put_in_standard_position(connect_ends(left_curve, right_curve))
    return inner_gosperize

# testing
draw_connected(200, your_gosper_curve_with_angle(10, lambda lvl: pi/(2+lvl)))
draw_connected(200, your_gosper_curve_with_angle(5, lambda lvl: (pi/(2+lvl))/(pow(1.3, lvl))))

##draw_connected_scaled(200, gosper_curve_with_angle (10 , lambda lvl : pi/(2+lvl)))
