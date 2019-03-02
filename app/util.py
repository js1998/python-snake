
def CalculateDistance(dest, headPos):

    dest_x = dest["x"]
    dest_y = dest["y"]

    headPos_x = headPos["x"]
    headPos_y = headPos["y"]

    return abs(dest_x - headPos_x) + abs(dest_y - headPos_y)


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
