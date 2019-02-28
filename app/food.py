import json
import random
import util


def direction_to_food(food, you, occupied, height, width):
    head_pos = you[0]
    move_score = {}

    if int(food["y"]) < int(head_pos["y"]):
        print('f trying up')
        if util.is_possible_move("up", you, occupied, height, width, spacing=2):
            return "up"

    elif int(food["y"]) > int(head_pos["y"]):
        print('f trying down')
        if util.is_possible_move("down", you, occupied, height, width, spacing=2):
            return "down"

    if int(food["x"]) < int(head_pos["x"]):
        print('f trying left')
        if util.is_possible_move("left", you, occupied, height, width, spacing=2):
            return "left"

    elif int(food["x"]) > int(head_pos["x"]):
        print('f trying right')
        if util.is_possible_move("right", you, occupied, height, width, spacing=2):
            return "right"

    print('f I ended up in moveTried')
    if util.is_possible_move("up", you, occupied, height, width):
        score = util.corner_check(head_pos, occupied, "up")
        move_score["up"] = score
        # return "up"
    if util.is_possible_move("down", you, occupied, height, width):
        score = util.corner_check(head_pos, occupied, "down")
        move_score["down"] = score
        # return "down"
    if util.is_possible_move("left", you, occupied, height, width):
        score = util.corner_check(head_pos, occupied, "left")
        move_score["left"] = score
        # return "left"
    if util.is_possible_move("right", you, occupied, height, width):
        score = util.corner_check(head_pos, occupied, "right")
        move_score["right"] = score
        # return "right"
    if not move_score:
        print("failure, no possible moves, trying to go towards tail")
        move = 'left'
    else:
        best_moves = util.minimums(move_score)
        print("best moves are {}".format(best_moves))
        move = random.choice(best_moves)
    print(move)
    return move


def get_closest_food(foods, headPos):
    closest_distance = util.calculate_direction(foods[0], headPos)
    closest_food = foods[0]

    for food in foods:
        new_distance = util.calculate_direction(food, headPos)
        if closest_distance > new_distance:
            closest_distance = new_distance
            closest_food = food

    return closest_food
