import json

def calculateDirection(data):
    foods = data["board"]["food"]
    currPositions = data["you"]["body"]
    height = data["board"]["height"]
    width = data["board"]["width"]

    nearestFood = getClosestFood(foods, currPositions[0])

    return directionToFood(foods[0], currPositions, height, width)

def directionToFood(food, bodyPositions, height, width):
    headPos = bodyPositions[0]

    dir = "left"

    movedTried = []

    if int(food["y"]) < int(headPos["y"]):
        if isPossibleMove("up", bodyPositions, height, width):
            return "up"
    elif int(food["y"]) > int(headPos["y"]):
        if isPossibleMove("down", bodyPositions,height, width):
            return "down"

    if int(food["x"]) < int(headPos["x"]):
        if isPossibleMove("left", bodyPositions, height, width):
            return "left"
    elif int(food["x"]) > int(headPos["x"]):
        if isPossibleMove("right", bodyPositions, height, width):
            return "right"

    while len(movedTried) is not 4:
        if "up" not in movedTried and isPossibleMove("up", bodyPositions, height, width):
            movedTried.append("up")
            return "up"
        if "down" not in movedTried and isPossibleMove("down", bodyPositions, height, width):
            movedTried.append("down")
            return "down"
        if "left" not in movedTried and isPossibleMove("left", bodyPositions, height, width):
            movedTried.append("left")
            return "left"
        if "right" not in movedTried and isPossibleMove("right", bodyPositions, height, width):
            movedTried.append("right")
            return "right"

    return dir

def isPossibleMove(direction, bodyPositions, height, width):
    headPos = bodyPositions[0]

    i = 1
    while i < len(bodyPositions):

        headPos_x = headPos["x"]
        headPos_y = headPos["y"]

        bodyPos_x = bodyPositions[i]["x"]
        bodyPos_y = bodyPositions[i]["y"]

        if direction == "up":
            if (headPos_y - bodyPos_y == 1 and headPos_x == bodyPos_x) or headPos_y == 0:
                return False
        if direction == "down":
            if (bodyPos_y - headPos_y == 1 and headPos_x == bodyPos_x) or headPos_y == height - 1:
                return False
        if direction == "right":
            if (bodyPos_x - headPos_x == 1 and headPos_y == bodyPos_y) or headPos_x == width - 1:
                return False
        if direction == "left":
            if (headPos_x - bodyPos_x == 1 and headPos_y == bodyPos_y) or headPos["x"] == 0:
                return False

        i = i + 1

    return True

def getClosestFood(foods, headPos):

    closestDistance = calculateDistance(foods[0], headPos)
    closestFood = foods[0]

    for food in foods:
        newDistance = calculateDistance(food, headPos)
        if closestDistance > newDistance:
            closestDistance = newDistance
            closestFood = food

    print(closestFood)
    print(closestDistance)
    print(headPos)
    return closestFood

def calculateDistance(food, headPos):

    distance = 0;

    food_x = food["x"];
    food_y = food["y"];

    headPos_x = headPos["x"];
    headPos_y = headPos["y"];

    if headPos_x < food_x:
        distance = distance + food_x - headPos_x
    else:
        distance = distance + headPos_x - food_x

    if headPos_y < food_y:
        distance = distance + food_y - headPos_y
    else:
        distance = distance + headPos_y - food_y

    return distance








