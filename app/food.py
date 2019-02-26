from util import CalculateDistance, IsPossibleMove

def calculateDirection(data):
    foods = data["board"]["food"]
    currPositions = data["you"]["body"]
    height = data["board"]["height"]
    width = data["board"]["width"]

    nearestFood = getClosestFood(foods, currPositions[0])

    return directionToFood(nearestFood, currPositions, height, width)

def directionToFood(food, bodyPositions, height, width):
    headPos = bodyPositions[0]

    dir = "left"

    movedTried = []

    if int(food["y"]) < int(headPos["y"]):
        if IsPossibleMove("up", bodyPositions, height, width):
            return "up"
    elif int(food["y"]) > int(headPos["y"]):
        if IsPossibleMove("down", bodyPositions,height, width):
            return "down"

    if int(food["x"]) < int(headPos["x"]):
        if IsPossibleMove("left", bodyPositions, height, width):
            return "left"
    elif int(food["x"]) > int(headPos["x"]):
        if IsPossibleMove("right", bodyPositions, height, width):
            return "right"

    while len(movedTried) is not 4:
        if "up" not in movedTried and IsPossibleMove("up", bodyPositions, height, width):
            movedTried.append("up")
            return "up"
        if "down" not in movedTried and IsPossibleMove("down", bodyPositions, height, width):
            movedTried.append("down")
            return "down"
        if "left" not in movedTried and IsPossibleMove("left", bodyPositions, height, width):
            movedTried.append("left")
            return "left"
        if "right" not in movedTried and IsPossibleMove("right", bodyPositions, height, width):
            movedTried.append("right")
            return "right"

    return dir



def getClosestFood(foods, headPos):

    closestDistance = CalculateDistance(foods[0], headPos)
    closestFood = foods[0]

    for food in foods:
        newDistance = CalculateDistance(food, headPos)
        if closestDistance > newDistance:
            closestDistance = newDistance
            closestFood = food

    print (headPos)
    return closestFood








