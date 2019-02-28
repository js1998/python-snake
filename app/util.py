
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

    elif direction == 'down':
        if any(loc["y"] == (head["y"] + 1) and loc["x"] == (head["x"] - 1) for loc in occupied):
            count += 1
        if any(loc["y"] == (head["y"] + 1) and loc["x"] == (head["x"] + 1) for loc in occupied):
            count += 1
    return count


def minimums(some_dict):
    # Returns a list of all keys with the minimum value within a dictionary

    positions = []
    min_value = float("inf")
    for k, v in some_dict.items():
        if v == min_value:
            positions.append(k)
        if v < min_value:
            min_value = v
            del positions[:]
            positions.append(k)

    return positions


def choose_move(direction, you, occupied, height, width, spacing=1):
    head_pos = you[0]
    i = 1
    while i < len(occupied):

        headPos_x = head_pos["x"]
        headPos_y = head_pos["y"]

        taken_x = occupied[i]["x"]
        taken_y = occupied[i]["y"]

        dist_y = taken_y - headPos_y
        dist_x = taken_x - headPos_x

        if direction == "up":
            if (abs(dist_y) <= spacing and taken_y < headPos_y and headPos_x == taken_x) or headPos_y == 0:
                return False
        if direction == "down":
            if (abs(dist_y) <= spacing and taken_y > headPos_y and headPos_x == taken_x) or headPos_y == height - 1:
                return False
        if direction == "right":
            if (abs(dist_x) <= spacing and taken_x > headPos_x and headPos_y == taken_y) or headPos_x == width - 1:
                return False
        if direction == "left":
            if (abs(dist_x) <= spacing and taken_x < headPos_x and headPos_y == taken_y) or headPos_x == 0:
                return False

        i = i + 1

    return True



