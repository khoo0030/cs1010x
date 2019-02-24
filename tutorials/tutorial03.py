from math import *

def f(n):
    if n < 3:
        return n

    if n >= 3:
        return f(n-1) + (2 * f(n-2)) + (3 * f(n-3))

def g(n):
    if n < 3:
        return n

    if n >= 3:
        results = []

        for i in range(0, n+1):
            if (i==0):
                results.insert(i, 0)
                
            if (i==1):
                results.insert(i, 1)
    
            if (i==2):
                results.insert(i, 2)

            if (i>=3):
                value = results[i-1] + 2 * results[i-2] + 3 * results[i-3]
                results.insert(i, value)

    size = len(results)
    return results[size-1]

def h(n):
    if n < 3:
        return n

    if n >= 3:
        previous_three_iteration_value = 0
        previous_two_iteration_value = 1
        previous_one_iteration_value = 2

        for i in range(3, n+1):
            if (i>=3):
                current_iteration_value = previous_one_iteration_value + (2 * previous_two_iteration_value) + (3 * previous_three_iteration_value)

                previous_one_iteration_value, previous_two_iteration_value, previous_three_iteration_value = current_iteration_value, previous_one_iteration_value, previous_two_iteration_value
                
    return current_iteration_value

def is_fib(number):
    if number < 0:
        return False

    if number == 0:
        return True

    if number == 1:
        return True

    if number > 1:
        is_run = True
        is_fibonacci_number = False

        fibonacci_numbers = [0, 1, 1]

        i = 2
        while is_run == True:
            fibonacci_number = fibonacci_numbers[i-1] + fibonacci_numbers[i-2]

            if (number == fibonacci_number):
                is_fibonacci_number = True
                break
            else:
                if (number > fibonacci_numbers[i-1] and number < fibonacci_number):
                    is_fibonacci_number = False
                    break

                fibonacci_numbers.insert(i, fibonacci_number)

            i += 1

        return is_fibonacci_number

def is_fib2(number):
    if number < 0:
        return False

    if number == 0:
        return True

    if number == 1:
        return True

    if number > 1:
        is_run = True
        is_fibonacci_number = False

        previous_two_iteration_fib_number = 1
        previous_one_iteration_fib_number = 1

        i = 2
        while is_run == True:
            current_iteration_fib_number = previous_one_iteration_fib_number + previous_two_iteration_fib_number

            if (number == current_iteration_fib_number):
                is_fibonacci_number = True
                break
            else:
                if (number > previous_one_iteration_fib_number and number < current_iteration_fib_number):
                    is_fibonacci_number = False
                    break

                previous_one_iteration_fib_number, previous_two_iteration_fib_number = current_iteration_fib_number, previous_one_iteration_fib_number
                
            i += 1

        return is_fibonacci_number

def make_fare(stage1, stage2, start_fare, increment, block1, block2):
    def taxi_fare(distance, stage1, stage2, start_fare, increment, block1, block2):  # distance in metres
        if distance <= stage1:
            return start_fare
        elif distance <= stage2:
            return start_fare + (increment * ceil((distance - stage1) / block1))
        else:
            return taxi_fare(stage2) + (increment* ceil((distance - stage2) / block2))
    
    return lambda distance: taxi_fare(distance, stage1, stage2, start_fare, increment, block1, block2)

#comfort_fare = make_fare(1000, 10000, 3.0, 0.22, 400, 350) 
#comfort_fare(3500)
