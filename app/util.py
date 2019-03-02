def calculate_direction(dest, headPos):
    dest_x = dest["x"]
    dest_y = dest["y"]

    headpos_x = headPos["x"]
    headpos_y = headPos["y"]

    return abs(dest_x - headpos_x) + abs(dest_y - headpos_y)


def score_move(head, occupied, direction, width=0, height=0):
    """ Gives a score for a given direction based on on how many corners are occupied around that direction

    :param head: x and y coordinate of head
    :type head: dict

    :param occupied: dicts containing all spacies occupied by bodies
    :type occupied: list

    :param direction: up, down, left, or right
    :type direction: str

    :return: int of how many corners occupied
    """

    def is_snake(start, finish, facing):
        count = 0
        if facing == 'left':
            if any((loc["x"] == start["x"] - 2 and loc["y"] == start["y"]) or  # two spaces ahead
                   (loc["y"] == (start["y"] - 1) and loc["x"] == (start["x"] - 1)) or  # close top right
                   (loc["y"] == (start["y"] - 1) and loc["x"] == (start["x"] - 2)) or  # far top right
                   (loc["y"] == (start["y"] + 1) and loc["x"] == (start["x"] - 1)) or  # close top left
                   (loc["y"] == (start["y"] + 1) and loc["x"] == (start["x"] - 2))  # far top left
                   for loc in finish):
                count += 1

        elif facing == 'right':
            if any((loc["x"] == start["x"] + 2 and loc["y"] == start["y"]) or  # two spaces ahead
                   (loc["y"] == (start["y"] + 1) and loc["x"] == (start["x"] + 1)) or  # close top right
                   (loc["y"] == (start["y"] + 1) and loc["x"] == (start["x"] + 2)) or  # far top right
                   (loc["y"] == (start["y"] - 1) and loc["x"] == (start["x"] + 1)) or  # close top left
                   (loc["y"] == (start["y"] - 1) and loc["x"] == (start["x"] + 2))  # far top left
                   for loc in finish):
                count += 1

        elif facing == 'down':
            if any((loc["y"] == start["y"] + 2 and loc["x"] == start["x"]) or  # two spaces ahead
                   (loc["x"] == (start["x"] + 1) and loc["y"] == (start["y"] + 1)) or  # close top right
                   (loc["x"] == (start["x"] + 1) and loc["y"] == (start["y"] + 2)) or  # far top right
                   (loc["x"] == (start["x"] - 1) and loc["y"] == (start["y"] + 1)) or  # close top left
                   (loc["x"] == (start["x"] - 1) and loc["y"] == (start["y"] + 2))  # far top left
                   for loc in finish):
                count += 1

        elif facing == 'up':
            if any((loc["y"] == start["y"] - 2 and loc["x"] == start["x"]) or  # two spaces ahead
                   (loc["x"] == (start["x"] - 1) and loc["y"] == (start["y"] - 1)) or  # close top right
                   (loc["x"] == (start["x"] - 1) and loc["y"] == (start["y"] - 2)) or  # far top right
                   (loc["x"] == (start["x"] + 1) and loc["y"] == (start["y"] - 1)) or  # close top left
                   (loc["x"] == (start["x"] + 1) and loc["y"] == (start["y"] - 2))  # far top left
                   for loc in finish):
                count += 1
        return count

    def is_out(start, facing, x_boundary, y_boundary):
        if facing == 'left':
            if (start["x"] - 2) <= -1:
                return 1
            elif (start["x"] - 1) <= -1:
                return 2

        elif facing == "right":
            if (start["x"] + 2) >= y_boundary:
                return 1
            if (start["x"] + 1) >= y_boundary:
                return 2

        elif facing == 'up':
            if (start["y"] - 2) <= -1:
                return 1
            elif (start["y"] - 1) <= -1:
                return 2

        elif facing == 'down':
            if (start["y"] + 1) >= x_boundary:
                return 1
            if (start["y"] + 1) >= x_boundary:
                return 2
        return 0

    snake_score = is_snake(start=head,
                           finish=occupied,
                           facing=direction)

    out_score = is_out(start=head,
                       facing=direction,
                       x_boundary=width,
                       y_boundary=height)

    return snake_score + out_score


def minimums(some_dict):
    """ Returns a list of all keys with the minimum value within a dictionary

    :param some_dict: dictionary with values as ints
    :return: list with all keys that had the minimum value
    """

    positions = {}
    min_value = float("inf")
    for k, v in some_dict.items():
        if v == min_value:
            positions[k] = v
        if v < min_value:
            min_value = v
            positions.clear()
            positions[k] = v

    return positions


def is_possible_move(direction, you, snake_heads, occupied, height, width, spacing=1):
    """

    :param direction: up down left or right
    :type direction: str

    :param you: all blocks our body is occupying
    :type you: list of dict

    :param occupied: all blocks all snakes are occupying
    :type occupied: list of dict

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
            if (abs(dist_y) <= spacing and taken_y < headpos_y and headpos_x == taken_x) or headpos_y == 0:# or possible_head_collision("up", head_pos, snake_heads):
                return False
        if direction == "down":
            if (abs(dist_y) <= spacing and taken_y > headpos_y and headpos_x == taken_x) or headpos_y == height - 1:# or possible_head_collision("down", head_pos, snake_heads):
                return False
        if direction == "right":
            if (abs(dist_x) <= spacing and taken_x > headpos_x and headpos_y == taken_y) or headpos_x == width - 1:# or possible_head_collision("right", head_pos, snake_heads):
                return False
        if direction == "left":
            if (abs(dist_x) <= spacing and taken_x < headpos_x and headpos_y == taken_y) or headpos_x == 0:# or possible_head_collision("left", head_pos, snake_heads):
                return False

        i = i + 1

    return True


def possible_head_collision(direction, our_head, snake_heads):
    if direction == "up":
        for head in snake_heads:
            if (our_head["y"] - 2 == head["y"] and our_head["x"] == head["x"]) or (our_head["y"] - 1 == head["y"] and (our_head["x"] == head["x"] - 1 or our_head["x"] == head["x"] - 1)):
                return True

    if direction == "down":
        for head in snake_heads:
            if (our_head["y"] + 2 == head["y"] and our_head["x"] == head["x"]) or (our_head["y"] - 1 == head["y"] and (our_head["x"] == head["x"] + 1 or our_head["x"] == head["x"] - 1)):
                return True

    if direction == "left":
        for head in snake_heads:
            if (our_head["x"] - 2 == head["x"] and our_head["y"] == head["y"]) or (our_head["x"] + 1 == head["x"] and (our_head["y"] == head["y"] - 1 or our_head["y"] == head["y"] - 1)):
                return True

    if direction == "right":
        for head in snake_heads:
            if (our_head["x"] + 2 == head["x"] and our_head["y"] == head["y"]) or (our_head["x"] - 1 == head["x"] and (our_head["y"] == head["y"] + 1 or our_head["y"] == head["y"] - 1)):
                return True

    return False

def detect_box(direction, body_parts):
    head_pos = body_parts[0]

    #TODO: check for walls, other directions, and threshhold for box

    if direction == "up":
        y_val = head_pos["y"] - 1

        total_count = 1
        for part in body_parts:
            if part["y"] == y_val:
                total_count = total_count + 1

        if total_count >= 2:
            return True

    if direction == "down":
        y_val = head_pos["y"] + 1

        total_count = 1
        for part in body_parts:
            if part["y"] == y_val:
                total_count = total_count + 1

        if total_count >= 2:
            return True

    if direction == "right":
        x_val = head_pos["x"] + 1

        total_count = 1
        for part in body_parts:
            if part["x"] == x_val:
                total_count = total_count + 1

        if total_count >= 2:
            return True

    if direction == "left":
        x_val = head_pos["x"] - 1

        total_count = 1
        for part in body_parts:
            if part["x"] == x_val:
                total_count = total_count + 1

        if total_count >= 2:
            return True

    return False


# def trap_detection(direction, bodyPositions, visited, height, width, dest_x, dest_y):
#     x = bodyPositions["x"]
#     y = bodyPositions["y"]
#
#     if x == dest_x and y == dest_y:
#         return True
#     if x >= width or y > height:
#         return False
#     if x < 0 or y < 0:
#         return False
#     if visited[x][y]:
#         return False
#     # if curr_x and curr_y not body Position, return false
#     visited[x][y] = True
#     if (trap_detection(x + 1, y, visited, n, m, mat, dest_x, dest_y)):
#         return True
#     if (trap_detection(x - 1, y, visited, n, m, mat, dest_x, dest_y)):
#         return True
#     if (trap_detection(x, y + 1, visited, n, m, mat, dest_x, dest_y)):
#         return True
#     if (trap_detection(x, y - 1, visited, n, m, mat, dest_x, dest_y)):
#         return True
#     return False

def check_lane(head, occupied, direction, width, height):
    # lane_def = []
    # i = 0
    #
    # if direction == 'left':
    #     while head["x"] != -1:
    #         lane_def.append({"y": head["y"] + 1, "x": head["x"] - i})
    #         lane_def.append({"y": head["y"] - 1, "x": head["x"] - i})
    #         i -= 1
    #
    # elif direction == 'right':
    #     while head["x"] != width:
    #         lane_def.append({"y": head["y"] + 1, "x": head["x"] + i})
    #         lane_def.append({"y": head["y"] - 1, "x": head["x"] + i})
    #         i += 1
    #
    # elif direction == 'up':
    #     while head["y"] != -1:
    #         lane_def.append({"y": head["y"] - i, "x": head["x"] + 1})
    #         lane_def.append({"y": head["y"] - i, "x": head["x"] - 1})
    #         i -= 1
    #
    # elif direction == 'down':
    #     while head["y"] != height:
    #         lane_def.append({"y": head["y"] + i, "x": head["x"] + 1})
    #         lane_def.append({"y": head["y"] + i, "x": head["x"] - 1})
    #         i += 1
    #
    # if all(lane_def) in occupied:
    return False

    # return True

