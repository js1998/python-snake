# Chase own tail when not looking for food
import util
import random


def find_tail(you, occupied, snake_heads, width, height):
    # Finds square closest to tail and moves in that direction
    head_pos = you[0]
    tail_pos = you[-1]
    optimal_move_score = {}
    possible_move_score = {}

    if head_pos['y'] < tail_pos['y'] and not util.check_lane(head_pos, occupied, "down", width, height):
        print('s trying down')
        if util.is_possible_move('down', you,snake_heads, occupied, width, height, spacing=2):
            score = util.score_move(head_pos, occupied, "down")
            optimal_move_score['down'] = score

    if head_pos['y'] > tail_pos['y'] and not util.check_lane(head_pos, occupied, "up", width, height):
        print('s trying up')
        if util.is_possible_move('up', you,snake_heads, occupied, width, height, spacing=2):
            score = util.score_move(head_pos, occupied, "up")
            optimal_move_score['up'] = score

    if head_pos['x'] < tail_pos['x'] and not util.check_lane(head_pos, occupied, "right", width, height):
        print('s trying right')
        if util.is_possible_move('right', you, snake_heads, occupied, width, height, spacing=2):
            score = util.score_move(head_pos, occupied, "right")
            optimal_move_score['right'] = score

    if head_pos['x'] > tail_pos['x'] and not util.check_lane(head_pos, occupied, "left", width, height):
        print('s trying left')
        if util.is_possible_move('left', you, snake_heads, occupied, width, height, spacing=2):
            score = util.score_move(head_pos, occupied, "left")
            optimal_move_score['left'] = score

    if optimal_move_score:
        best_moves = util.minimums(optimal_move_score)
        print("best moves are {} with scores {}".format(best_moves.keys(), best_moves.values()))
        move = random.choice(best_moves.keys())
        return move

    print('s I ended up in moveTried')
    if util.is_possible_move("up", you, snake_heads, occupied, height, width):
        score = util.score_move(head_pos, occupied, "up")
        possible_move_score["up"] = score

    if util.is_possible_move("down", you, snake_heads, occupied, height, width):
        score = util.score_move(head_pos, occupied, "down")
        possible_move_score["down"] = score

    if util.is_possible_move("left", you, snake_heads, occupied, height, width):
        score = util.score_move(head_pos, occupied, "left")
        possible_move_score["left"] = score

    if util.is_possible_move("right", you, snake_heads, occupied, height, width):
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
