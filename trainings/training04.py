def sum_odd_n(n):
    sum = 0
    
    for i in range(1, n+1, 1):
        sum = sum + 2*i - 1
            
    return sum


def sum_odd_e(n):
    sum = 0
    
    i = 1
    while i <= n:
        sum = sum + 2*i - 1
        i += 1
            
    return sum

def sum_odd_r(n):
    if n == 1:
        return 1

    if n > 1:
        return (2*n - 1) + sum_odd_r(n-1)

def sum_n_squares(n):
    result = 0
    for counter in range(1, n+1, 1):
        result = result + counter*counter

    return result

def sum_n_squares(n):
    counter, result = 1, 0
    while counter <= n:
        result = result + counter*counter
        counter += 1
        
    return result


def sum_n_squares(n):
    if n == 1:
        return 1

    return n ** 2 + sum_n_squares(n - 1)



def defeat_balrog(protagonist):    
    def spawn_balrog():
        """Spawns and returns a stubborn balrog"""
        pass
    def balrog_attack(balrog, person):
        """Returns an attack move from the balrog's repertoire"""
        pass
    cave_balrog = spawn_balrog()
    is_balrog_defeated = False
    yell(protagonist, 'You cannot pass!')
    while not is_balrog_defeated:
        current_attack = balrog_attack(cave_balrog, protagonist)
        if current_attack != None:
            take_defensive_action(protagonist, current_attack)
        yell(protagonist, 'YOU SHALL NOT PASS!')
        take_offensive_action(protagonist, cave_balrog)
        is_balrog_defeated = True
    return True

def take_defensive_action(attacked_entity, attack_move):
    """
    attacked_entity anticipates attack_move and defends himself.
    """
    pass

def yell(protagonist, message):
    """
    print some message on screen
    """
    pass

def take_offensive_action(protagonist, current_attack):
    """
    attacks protagonist
    """
    pass

#
# Your stubs will go here
#
defeat_balrog('gandalf')


def foo(x, y):
    while y > x:
        y = y // 2
        x = x + 1


