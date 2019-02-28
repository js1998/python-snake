
def calculate_direction(dest, headPos):

    dest_x = dest["x"]
    dest_y = dest["y"]

    headpos_x = headPos["x"]
    headpos_y = headPos["y"]

    return abs(dest_x - headpos_x) + abs(dest_y - headpos_y)


def corner_check(head, occupied, direction):
    """ Gives a score for a given direction based on on how many corners are occupied around that direction

    :param head: x and y coordinate of head
    :type head: dict

    :param occupied: dicts containing all spacies occupied by bodies
    :type occupied: list

    :param direction: up, down, left, or right
    :type direction: str

    :return: int of how many corners occupied
    """
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
    """ Returns a list of all keys with the minimum value within a dictionary

    :param some_dict: dictionary with values as ints
    :return: list with all keys that had the minimum value
    """

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


def is_possible_move(direction, you, occupied, height, width, spacing=1):
    """

    :param direction: up down left or right
    :type direction: str

    :param you: all blocks our body is occupying
    :type you: list

    :param occupied: all blocks all snakes are occupying
    :type occupied: list

    :param height: height of the board
    :type height: int

    :param width: width of the board
    :type width: int

    :param spacing: how many spaces directly in front of you to look ahead
    :type spacing: int
    :return: boolean

    """
    head_pos = you[0]
    i = 1
    while i < len(occupied):

        headpos_x = head_pos["x"]
        headpos_y = head_pos["y"]

        taken_x = occupied[i]["x"]
        taken_y = occupied[i]["y"]

        dist_y = taken_y - headpos_y
        dist_x = taken_x - headpos_x

        if direction == "up":
            if (abs(dist_y) <= spacing and taken_y < headpos_y and headpos_x == taken_x) or headpos_y == 0:
                return False
        if direction == "down":
            if (abs(dist_y) <= spacing and taken_y > headpos_y and headpos_x == taken_x) or headpos_y == height - 1:
                return False
        if direction == "right":
            if (abs(dist_x) <= spacing and taken_x > headpos_x and headpos_y == taken_y) or headpos_x == width - 1:
                return False
        if direction == "left":
            if (abs(dist_x) <= spacing and taken_x < headpos_x and headpos_y == taken_y) or headpos_x == 0:
                return False

        i = i + 1

    return True

