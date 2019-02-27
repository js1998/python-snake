import json
import random
from util import CalculateDistance, optimal_move, possible_move


def directionToFood(food, you, occupied, height, width):
    headPos = you[0]

    dir = 'left'
    movedTried = []

    if int(food["y"]) < int(headPos["y"]):
        print('f trying up')
        if optimal_move("up", you, occupied, height, width):
            return "up"
    elif int(food["y"]) > int(headPos["y"]):
        print('f trying down')
        if optimal_move("down", you, occupied, height, width):
            return "down"

    if int(food["x"]) < int(headPos["x"]):
        print('f trying left')
        if optimal_move("left", you, occupied, height, width):
            return "left"
    elif int(food["x"]) > int(headPos["x"]):
        print('f trying right')
        if optimal_move("right", you, occupied, height, width):
            return "right"

    print('f I ended up in moveTried')
    if "up" not in movedTried and possible_move("up", you, occupied, height, width):
        movedTried.append("up")
        # return "up"
    if "down" not in movedTried and possible_move("down", you, occupied, height, width):
        movedTried.append("down")
        # return "down"
    if "left" not in movedTried and possible_move("left", you, occupied, height, width):
        movedTried.append("left")
        # return "left"
    if "right" not in movedTried and possible_move("right", you, occupied, height, width):
        movedTried.append("right")
        # return "right"
    if not movedTried:
        dir = 'left'
    else:
        dir = random.choice(movedTried)
    print(dir)
    return dir


def getClosestFood(foods, headPos):
    closest_distance = CalculateDistance(foods[0], headPos)
    closest_food = foods[0]

    for food in foods:
        new_distance = CalculateDistance(food, headPos)
        if closest_distance > new_distance:
            closest_distance = new_distance
            closest_food = food

    return closest_food
