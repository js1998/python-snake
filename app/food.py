import json
import random
from util import CalculateDistance, optimal_move, possible_move, detect_box


def directionToFood(food, you, occupied, height, width):
    headPos = you[0]

    dir = 'left'
    movedTried = []

    if int(food["y"]) < int(headPos["y"]):
        print('f trying up')
        if optimal_move("up", you, occupied, height, width) and not detect_box("up", you):
            return "up"
    elif int(food["y"]) > int(headPos["y"]):
        print('f trying down')
        if optimal_move("down", you, occupied, height, width) and not detect_box("down", you):
            return "down"

    if int(food["x"]) < int(headPos["x"]):
        print('f trying left')
        if optimal_move("left", you, occupied, height, width) and not detect_box("left", you):
            return "left"
    elif int(food["x"]) > int(headPos["x"]):
        print('f trying right')
        if optimal_move("right", you, occupied, height, width) and not detect_box("right", you):
            return "right"

    print('f I ended up in moveTried')

    while ("up" not in movedTried and "down" not in movedTried and "left" not in movedTried and "right" not in movedTried):
        if "up" not in movedTried and possible_move("up", you, occupied, height, width) and not detect_box("up", you):
            movedTried.append("up")
        if "down" not in movedTried and possible_move("down", you, occupied, height, width) and not detect_box("down", you):
            movedTried.append("down")
        if "left" not in movedTried and possible_move("left", you, occupied, height, width) and not detect_box("left", you):
            movedTried.append("left")
        if "right" not in movedTried and possible_move("right", you, occupied, height, width) and not detect_box("right", you):
            movedTried.append("right")

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
