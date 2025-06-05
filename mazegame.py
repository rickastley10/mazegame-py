import time
print('welcome to the MAZE')
input('press [enter] to start')
x = 0
y = 0
level = 0
def basicroom():
    print('___w___')
    print('|      |')
    print('a      d')
    print('|      |')
    print('|__s___|)')

def movement():
    global move  # Make move accessible to coords()
    move = input('\n [w, a, s, d] \n')

def coords():
    global x, y  # Need to declare these as global to modify them
    if move == 'w':
        x += 1  # Need += instead of +
    elif move == 'a':
        y -= 1  # Need -= instead of -
    elif move == 's':
        x -= 1  # Need -= instead of -
    elif move == 'd':
        y += 1  # Changed to y += 1 since d should move right (increase y)

def debug_coordinates():
    print(x, y)

def levelfinish():
    global level
    if x == 1 and y == -3 and level == 0:

        print('********')
        print('********')
        print('LEVEL 0 ')
        print('COMPLETE')
        print('********')
        level  = 1
    if x == -9 and y == 5 and level == 1:
        
        print('********')
        print('LEVEL 1 ')
        print('COMPLETE')
        print('********')
        print('********')
        level = 2
    if x == -5 and y == -4 and level == 2:

        print('********')
        print('FINAL   ')
        print('LEVEL   ')
        print('COMPLETE')
        print('********')
        print('well done')

while 1 == 1:
    debug_coordinates()
    basicroom()
    movement()
    coords()
    levelfinish()