import math
from util import is_possible_move

def find_next_direction(occupied, body_pos, snake_heads, width, height, dest):

    closed_list = []
    open_list = []

    head_pos = body_pos[0]

    start_node = create_node(None, head_pos, dest)

    open_list.append(start_node)

    while len(open_list) != 0:

        curr_node = find_lowest_f(open_list)

        open_list.remove(curr_node)
        closed_list.append(curr_node)

        if point_in_list(closed_list, dest)[0]:
            print("destination to path found")
            break

        # check 4 direction to children
        up_point = {"x": head_pos["x"], "y": head_pos["y"] - 1}
        if is_possible_move("up", body_pos, snake_heads, occupied, height, width) and not point_in_list(closed_list, up_point)[0]:
            open_list = find_path(open_list, curr_node, up_point, dest)

        down_point = {"x": head_pos["x"], "y": head_pos["y"] + 1}
        if is_possible_move("down", body_pos, snake_heads, occupied, height, width) and not point_in_list(closed_list, down_point)[0]:
            open_list = find_path(open_list, curr_node, down_point, dest)

        right_point = {"x": head_pos["x"] + 1, "y": head_pos["y"]}
        if is_possible_move("right", body_pos, snake_heads, occupied, height, width) and not point_in_list(closed_list, right_point)[0]:
            open_list = find_path(open_list, curr_node, right_point, dest)

        left_point = {"x": head_pos["x"] - 1, "y": head_pos["y"]}
        if is_possible_move("left", body_pos, snake_heads, occupied, height, width) and not point_in_list(closed_list, left_point)[0]:
            open_list = find_path(open_list, curr_node, left_point, dest)

    if open_list is [] and not point_in_list(closed_list, dest):
        #at this point, we're trapped and have died
        return "left"

    #iterate over closed_list then return direction to go
    return direction_to_go(closed_list, head_pos)


def direction_to_go(node_list, head_pos):
    for node in node_list:
        parent_node_pos = node["parent"]
        if parent_node_pos is not None:
            parent_node_pos = parent_node_pos["position"]
            if parent_node_pos["x"] == head_pos["x"] and parent_node_pos["y"] == head_pos["y"]:
                if node["position"]["x"] == head_pos["x"]:
                    if node["position"]["y"] > head_pos["y"]:
                        print("going down")
                        return "down"
                    else:
                        print("going up")
                        return "up"
                else:
                    if node["position"]["x"] < head_pos["x"]:
                        print("going left")
                        return "left"
                    else:
                        print("going right")
                        return "right"

    #shouldn't get here but...
    print(node_list)
    print("ERROR: head_pos not in closed_list")
    return "left"


def find_path(open_list, curr_node, point_to_check, dest):
    new_node = create_node(curr_node, point_to_check, dest)
    node_in_list = point_in_list(open_list, point_to_check)
    if node_in_list[0]:
        node = node_in_list[1]
        open_list.remove(node)
        if node["g_score"] > new_node["g_score"]:
            node["parent"] = curr_node
            node["g_score"] = new_node["g_score"]
            node["f_score"] = new_node["g_score"] + new_node["h_score"]

        open_list.append(node)
    else:
        open_list.append(new_node)

    return open_list


def create_node(parent_node, curr_pos, dest):

    h_score = calculate_h_score(curr_pos, dest)
    if parent_node is None:
        g_score = 0
    else:
        g_score = parent_node["g_score"] + 1
    f_score = h_score + g_score

    return {"parent": parent_node,
            "position": curr_pos,
            "h_score": h_score,
            "g_score": g_score,
            "f_score": f_score}



def point_in_list(list, point):

    for node in list:
        if node["position"]["x"] == point["x"] and node["position"]["y"] == point["y"]:
            return True, node

    return False, None


def find_lowest_f(open_list):
    min_score = open_list[0]["f_score"]
    min_node = open_list[0]

    for node in open_list:
        if node["f_score"] < min_score:
            min_score = node["f_score"]
            min_node = node

    return min_node


def calculate_h_score(start, dest):
    return math.pow(start["x"] - dest["x"], 2) + math.pow(start["y"] - dest["y"], 2)


