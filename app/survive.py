# Chase own tail when not looking for food

import util
import random


def findTail(you, occupied, width, height):
    # Finds square closest to tail and moves in that direction
    headPos = you[0]
    tailPos = you[-1]

    movedTried = []

    if headPos['y'] < tailPos['y']:
        print('s trying down')
        if util.optimal_move('down', you, occupied, width, height):
            return "down"

    if headPos['y'] > tailPos['y']:
        print('s trying up')
        if util.optimal_move('up', you, occupied, width, height):
            return "up"

    if headPos['x'] < tailPos['x']:
        print('s trying right')
        if util.optimal_move('right', you, occupied, width, height):
            return "right"

    if headPos['x'] > tailPos['x']:
        print('s trying left')
        if util.optimal_move('left', you, occupied, width, height):
            return "left"

    print('s I ended up in moveTried')
    if "up" not in movedTried and util.possible_move("up", you, occupied, height, width):
        movedTried.append("up")
        # return "up"
    if "down" not in movedTried and util.possible_move("down", you, occupied, height, width):
        movedTried.append("down")
        # return "down"
    if "left" not in movedTried and util.possible_move("left", you, occupied, height, width):
        movedTried.append("left")
        # return "left"
    if "right" not in movedTried and util.possible_move("right", you, occupied, height, width):
        movedTried.append("right")
        # return "right"
    if not movedTried:
        print('failure, no possible moves')
        dir = "left"
    else:
        dir = random.choice(movedTried)
    print(dir)
    return dir