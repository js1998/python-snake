import json
import random
from util import CalculateDistance, IsPossibleMove



def directionToFood(food, bodyPositions, height, width):
    headPos = bodyPositions[0]

    dir = 'left'
    movedTried = []

    if int(food["y"]) < int(headPos["y"]):
        print('f trying up')
        if optimal_move("up", bodyPositions, height, width):
            return "up"
    elif int(food["y"]) > int(headPos["y"]):
        print('f trying down')
        if optimal_move("down", bodyPositions, height, width):
            return "down"

    if int(food["x"]) < int(headPos["x"]):
        print('f trying left')
        if optimal_move("left", bodyPositions, height, width):
            return "left"
    elif int(food["x"]) > int(headPos["x"]):
        print('f trying right')
        if optimal_move("right", bodyPositions, height, width):
            return "right"

    print('f I ended up in moveTried')
    if "up" not in movedTried and possible_move("up", bodyPositions, height, width):
        movedTried.append("up")
        # return "up"
    if "down" not in movedTried and possible_move("down", bodyPositions, height, width):
        movedTried.append("down")
        # return "down"
    if "left" not in movedTried and possible_move("left", bodyPositions, height, width):
        movedTried.append("left")
        # return "left"
    if "right" not in movedTried and possible_move("right", bodyPositions, height, width):
        movedTried.append("right")
        # return "right"
    if not movedTried:
        dir = 'left'
    else:
        dir = random.choice(movedTried)
    print(dir)
    return dir




def getClosestFood(foods, headPos):
    closestDistance = calculateDistance(foods[0], headPos)
    closestFood = foods[0]

    for food in foods:
        newDistance = CalculateDistance(food, headPos)
        if closestDistance > newDistance:
            closestDistance = newDistance
            closestFood = food

