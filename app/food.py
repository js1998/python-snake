import json

def calculateDirection(data):
    foods = data["board"]["food"]
    currPositions = data["you"]["body"]

    #TODO: nearestFood = getNearestFood(foods)

    return directionToFood(foods[0], currPositions)

def directionToFood(food, bodyPositions):
    headPos = bodyPositions[0]

    dir = "left"

    if int(food["y"]) < int(headPos["y"]):
        if isPossibleMove("up", bodyPositions):
            print("up")
            return "up"
    else:
        if isPossibleMove("down", bodyPositions):
            print("down")
            return "down"

    if int(food["x"]) < int(headPos["x"]):
        if isPossibleMove("left", bodyPositions):
            print("left")
            return "left"
    else:
        if isPossibleMove("right", bodyPositions):
            print("right")
            return "right"

    return dir

def isPossibleMove(direction, bodyPositions):
    headPos = bodyPositions[0]

    i = 1
    #TODO: check for walls
    while i < len(bodyPositions):

        if direction == "up":
            if headPos["y"] - bodyPositions[i]["y"] == 1:
                return False
        if direction == "down":
            if bodyPositions[i]["y"] - headPos["y"] == 1:
                return False
        if direction == "right":
            if bodyPositions[i]["x"] - headPos["x"] == 1:
                return False
        if direction == "left":
            if headPos["x"] - bodyPositions[i]["x"] == 1:
                return False

        i = i + 1

    return True






