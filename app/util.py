def CalculateDistance(food, headPos):

    distance = 0

    food_x = food["x"]
    food_y = food["y"]

    headPos_x = headPos["x"]
    headPos_y = headPos["y"]

    if headPos_x < food_x:
        distance = distance + food_x - headPos_x
    else:
        distance = distance + headPos_x - food_x

    if headPos_y < food_y:
        distance = distance + food_y - headPos_y
    else:
        distance = distance + headPos_y - food_y

    return distance