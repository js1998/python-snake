
def CalculateDistance(dest, headPos):

    dest_x = dest["x"]
    dest_y = dest["y"]

    headPos_x = headPos["x"]
    headPos_y = headPos["y"]

    return abs(dest_x - headPos_x) + abs(dest_y - headPos_y)


def corner_check(head, occupied, direction):
    count = 0

    if direction == 'left':
        if any(loc["y"] == (head["y"] - 1) and loc["x"] == (head["x"] - 1) for loc in occupied):
            count += 1
        if any(loc["y"] == (head["y"] + 1) and loc["x"] == (head["x"] - 1) for loc in occupied):
            count += 1

    elif direction == 'right':
        if any(loc["y"] == (head["y"] - 1) and loc["x"] == (head["x"] + 1) for loc in occupied):
            count += 1
        if any(loc["y"] == (head["y"] + 1) and loc["x"] == (head["x"] + 1) for loc in occupied):
            count += 1

    elif direction == 'up':
        if any(loc["y"] == (head["y"] - 1) and loc["x"] == (head["x"] - 1) for loc in occupied):
            count += 1
        if any(loc["y"] == (head["y"] - 1) and loc["x"] == (head["x"] + 1) for loc in occupied):
            count += 1

    elif direction == 'right':
        if any(loc["y"] == (head["y"] + 1) and loc["x"] == (head["x"] - 1) for loc in occupied):
            count += 1
        if any(loc["y"] == (head["y"] + 1) and loc["x"] == (head["x"] + 1) for loc in occupied):
            count += 1
    return count
    

def optimal_move(direction, you, occupied, height, width):
    headPos = you[0]

    i = 1
    while i < len(occupied):

        headPos_x = headPos["x"]
        headPos_y = headPos["y"]

        taken_x = occupied[i]["x"]
        taken_y = occupied[i]["y"]

        dist_y = taken_y - headPos_y
        dist_x = taken_x - headPos_x

        if direction == "up":
            if (abs(dist_y) <= 2 and taken_y < headPos_y and headPos_x == taken_x) or headPos_y == 0:
                return False
        if direction == "down":
            if (abs(dist_y) <= 2 and taken_y > headPos_y and headPos_x == taken_x) or headPos_y == height - 1:
                return False
        if direction == "right":
            if (abs(dist_x) <= 2 and taken_x > headPos_x and headPos_y == taken_y) or headPos_x == width - 1:
                return False
        if direction == "left":
            if (abs(dist_x) <= 2 and taken_x < headPos_x and headPos_y == taken_y) or headPos_x == 0:
                return False

        i = i + 1

    return True


def possible_move(direction, you, occupied, height, width):
    head_pos = you[0]

    i = 1
    while i < len(occupied):

        head_pos_x = head_pos["x"]
        head_pos_y = head_pos["y"]

        taken_x = occupied[i]["x"]
        taken_y = occupied[i]["y"]

        dist_y = taken_y - head_pos_y
        dist_x = taken_x - head_pos_x

        if direction == "up":
            if (abs(dist_y)==1 and taken_y < head_pos_y and head_pos_x == taken_x) or head_pos_y == 0:
                return False
        if direction == "down":
            if (abs(dist_y)==1 and taken_y > head_pos_y and head_pos_x == taken_x) or head_pos_y == height - 1:
                return False
        if direction == "right":
            if (abs(dist_x)==1 and taken_x > head_pos_x and head_pos_y == taken_y) or head_pos_x == width - 1:
                return False
        if direction == "left":
            if (abs(dist_x)==1 and taken_x < head_pos_x and head_pos_y == taken_y) or head_pos["x"] == 0:
                return False

        i = i + 1

    return True
