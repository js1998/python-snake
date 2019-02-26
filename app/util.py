def CalculateDistance(dest, headPos):

    dest_x = dest["x"]
    dest_y = dest["y"]

    headPos_x = headPos["x"]
    headPos_y = headPos["y"]

    return abs(dest_x - headPos_x) + abs(dest_y - headPos_y)

def IsPossibleMove(direction, bodyPositions, height, width):
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