# Day 6: Code blocks, functions, while loops
##########################

# Karel

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()
  
square()

move()
move()
move()
turn_left()
move()
move()
move()
turn_around()

##################

# Hurdles

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
	move()
	turn_left()
	move()
	turn_right()
	move()
	turn_right()
	move()
	turn_left()

for i in range(1,7):  
    jump()
    

######################

# While loop

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -=1
    print(number_of_hurdles)

while at_goal() == False:
    jump()
    

while not at_goal():
    jump()

#######################

# Project: Escaping the maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()

wile front_is_clear():  # check for edge cases
	move()
turn_left()

while not at_goal():
    while not wall_on_right():
        turn_right()
        move()
    if front_is_clear():
        move()
    else:
        if right_is_clear():
            turn_right()
            move()
        elif wall_on_right:
            turn_left()
        else:
            turn_left()
            move()
                
               