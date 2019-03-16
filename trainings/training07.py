#Q4:
def average(values):
    # values is a tuple of int elemenents
    size = len(values)
    total = 0

    if size == 0:
        return 0
    else:
        for value in values:
            total += value

    return total/size

#print(average((1, 2, 3)))
#print(average((-3, 2, 8, -1)))

#Q5:
def max_and_min(values):
    # values is a tuple of int elemenents
    size = len(values)
    min = 0
    max = 0
    
    if size == 0:
        return None
    else:
        i = 0
        for value in values:
            if i == 0:
                min = value
                max = value
            else:
                if value < min:
                    min = value
                    
                if value > max:
                    max = value
                    
            i += 1

    return (max,min)

#print(max_and_min((1, 2, 3, 4, 5)))
#print(max_and_min((5, -2, -3, 4, -1)))
#print(max_and_min((2, 2)))

#Q6:
def calculate_mid_point(coord_1, coord_2):
    coord_1_x = coord_1[0]
    coord_1_y = coord_1[1]
    
    coord_2_x = coord_2[0]
    coord_2_y = coord_2[1]

    mid_point_x = (coord_1_x + coord_2_x) / 2
    mid_point_y = (coord_1_y + coord_2_y) / 2

    return (mid_point_x, mid_point_y)

#print(calculate_mid_point((1, 1), (3, 3)))
#print(calculate_mid_point((0, 1), (5, 6)))


#Q11:
# Do not edit student_records
student_records = (('A0077294U', 'Shaohong'), ('A0084135B', 'Yang Shun'), ('A0015384U', 'Soda'), ('A0088245A', 'Alex'), ('A0012345A', 'Ben'))

def get_student_name(matric_num, records):
    for record in records:
        if record[0] == matric_num:
            return record[1]
        else:
            continue
        
    return 'Not found'

#print(get_student_name('A0077294U', student_records))
#print(get_student_name('A0088245A', student_records))
#print(get_student_name('A0084135B', student_records))
#print(get_student_name('A0082442C', student_records))

#Q12:
def change_value_at_index(tpl, index, value):
    tpl_length = len(tpl)

    if index >= tpl_length or index < -tpl_length:
        return tpl
    else:
        before = tpl[:index]
        after = tpl[index+1:]
             
    return before + (value,) + after
    
#print(change_value_at_index((1, 2, 3), 1, -1))
#print(change_value_at_index((1, 2, 3), 10, -1))
#print(change_value_at_index((1, 2, 3), -3, 'huh'))
#print(change_value_at_index((1, 2, 3), 3, 'huh'))
#print(change_value_at_index((1, 2, 3, 4, 5), 4, 'huh'))
#print(change_value_at_index((1, 2, 3, 4, 5), -2, 'huh'))
