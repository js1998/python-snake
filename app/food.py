import json


def calculateDirection(data):
    foods = data["board"]["food"]
    bodyPos = data["you"]["body"]
    height = data["board"]["height"]
    width = data["board"]["width"]

    # nearestFood = getClosestFood(foods, bodyPos[0])
    print('turn number {}'.format(data['turn']))
    print("head loc({} {}) and food loc({} {})".format(bodyPos[0]['x'], bodyPos[0]['y'], foods[0]['x'], foods[0]['y']))
    # print(directionToFood(foods[0], bodyPos, height, width))
    return directionToFood(foods[0], bodyPos, height, width)


def directionToFood(food, bodyPositions, height, width):
    headPos = bodyPositions[0]

    dir = "left"

    movedTried = []

    if int(food["y"]) < int(headPos["y"]):
        print('trying up')
        if optimal_move("up", bodyPositions, height, width):
            return "up"
    elif int(food["y"]) > int(headPos["y"]):
        print('trying down')
        if optimal_move("down", bodyPositions, height, width):
            return "down"

    if int(food["x"]) < int(headPos["x"]):
        print('trying left')
        if optimal_move("left", bodyPositions, height, width):
            return "left"
    elif int(food["x"]) > int(headPos["x"]):
        print('trying right')
        if optimal_move("right", bodyPositions, height, width):
            return "right"

    print('I ended up in moveTried')
    while len(movedTried) is not 4:
        if "up" not in movedTried and possible_move("up", bodyPositions, height, width):
            movedTried.append("up")
            return "up"
        if "down" not in movedTried and possible_move("down", bodyPositions, height, width):
            movedTried.append("down")
            return "down"
        if "left" not in movedTried and possible_move("left", bodyPositions, height, width):
            movedTried.append("left")
            return "left"
        if "right" not in movedTried and possible_move("right", bodyPositions, height, width):
            movedTried.append("right")
            return "right"

    return dir


def optimal_move(direction, bodyPositions, height, width):
    headPos = bodyPositions[0]

    i = 1
    while i < len(bodyPositions):

        headPos_x = headPos["x"]
        headPos_y = headPos["y"]

        bodyPos_x = bodyPositions[i]["x"]
        bodyPos_y = bodyPositions[i]["y"]

        dist_y = bodyPos_y - headPos_y
        dist_x = bodyPos_x - headPos_x

        if direction == "up":
            if (abs(dist_y) <= 2 and bodyPos_y < headPos_y and headPos_x == bodyPos_x) or headPos_y == 0:
                return False
        if direction == "down":
            if (abs(dist_y) <= 2 and bodyPos_y > headPos_y and headPos_x == bodyPos_x) or headPos_y == height - 1:
                return False
        if direction == "right":
            if (abs(dist_x) <= 2 and bodyPos_x > headPos_x and headPos_y == bodyPos_y) or headPos_x == width - 1:
                return False
        if direction == "left":
            if (abs(dist_x) <= 2 and bodyPos_x < headPos_x and headPos_y == bodyPos_y) or headPos_x == 0:
                return False

        i = i + 1

    return True


def possible_move(direction, bodyPositions, height, width):
    headPos = bodyPositions[0]

    i = 1
    while i < len(bodyPositions):

        headPos_x = headPos["x"]
        headPos_y = headPos["y"]

        bodyPos_x = bodyPositions[i]["x"]
        bodyPos_y = bodyPositions[i]["y"]

        dist_y = bodyPos_y - headPos_y
        dist_x = bodyPos_x - headPos_x

        if direction == "up":
            if (abs(dist_y) <= 1 and bodyPos_y < headPos_y and headPos_x == bodyPos_x) or headPos_y == 0:
                return False
        if direction == "down":
            if (abs(dist_y) <= 1 and bodyPos_y > headPos_y and headPos_x == bodyPos_x) or headPos_y == height - 1:
                return False
        if direction == "right":
            if (abs(dist_x) <= 1 and bodyPos_x > headPos_x and headPos_y == bodyPos_y) or headPos_x == width - 1:
                return False
        if direction == "left":
            if (abs(dist_x) <= 1 and bodyPos_x < headPos_x and headPos_y == bodyPos_y) or headPos_x == 0:
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
