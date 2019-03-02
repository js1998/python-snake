import json
import random
import util



def direction_to_food(food, you, occupied, height, width):
    head_pos = you[0]
    optimal_move_score = {}
    possible_move_score = {}

    if int(food["y"]) < int(head_pos["y"]) and not util.is_trap(head_pos, occupied, "up", width, height):
        print('f trying up')

        if util.is_possible_move("up", you, occupied, height, width, spacing=2):
            score = util.score_move(head_pos, occupied, "up")
            optimal_move_score['up'] = score

    elif int(food["y"]) > int(head_pos["y"]) and not util.is_trap(head_pos, occupied, "down", width, height):
        print('f trying down')
        if util.is_possible_move("down", you, occupied, height, width, spacing=2):
            score = util.score_move(head_pos, occupied, "down")
            optimal_move_score['down'] = score

    if int(food["x"]) < int(head_pos["x"]) and not util.is_trap(head_pos, occupied, "left", width, height):
        print('f trying left')

        if util.is_possible_move("left", you, occupied, height, width, spacing=2):
            score = util.score_move(head_pos, occupied, "left")
            optimal_move_score['left'] = score

    elif int(food["x"]) > int(head_pos["x"]) and not util.is_trap(head_pos, occupied, "up", width, height):
        print('f trying right')
        if util.is_possible_move("right", you, occupied, height, width, spacing=2):
            score = util.score_move(head_pos, occupied, "right")
            optimal_move_score['right'] = score

    if optimal_move_score:
        best_moves = util.minimums(optimal_move_score)
        print("best moves are {} with scores {}".format(best_moves.keys(), best_moves.values()))
        move = random.choice(best_moves.keys())
        return move

    print('f I ended up in moveTried')
    if util.is_possible_move("up", you, occupied, height, width):
        score = util.score_move(head_pos, occupied, "up")
        possible_move_score["up"] = score

    if util.is_possible_move("down", you, occupied, height, width):
        score = util.score_move(head_pos, occupied, "down")
        possible_move_score["down"] = score

    if util.is_possible_move("left", you, occupied, height, width):
        score = util.score_move(head_pos, occupied, "left")
        possible_move_score["left"] = score

    if util.is_possible_move("right", you, occupied, height, width):
        score = util.score_move(head_pos, occupied, "right")
        possible_move_score["right"] = score

    if not possible_move_score:
        print("failure, no possible moves, trying to go towards tail")
        move = 'left'

    else:
        best_moves = util.minimums(possible_move_score)
        print("best moves are {} with scores {}".format(best_moves.keys(), best_moves.values()))
        move = random.choice(best_moves.keys())
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
