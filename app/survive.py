# Chase own tail when not looking for food

import util
import random


def findTail(you, occupied, width, height):
    # Finds square closest to tail and moves in that direction
    head_pos = you[0]
    tail_pos = you[-1]

    move_score = {}

    if head_pos['y'] < tail_pos['y']:
        print('s trying down')
        if util.choose_move('down', you, occupied, width, height, spacing=2):
            return "down"

    if head_pos['y'] > tail_pos['y']:
        print('s trying up')
        if util.choose_move('up', you, occupied, width, height, spacing=2):
            return "up"

    if head_pos['x'] < tail_pos['x']:
        print('s trying right')
        if util.choose_move('right', you, occupied, width, height, spacing=2):
            return "right"

    if head_pos['x'] > tail_pos['x']:
        print('s trying left')
        if util.choose_move('left', you, occupied, width, height, spacing=2):
            return "left"

    print('f I ended up in moveTried')
    if util.choose_move("up", you, occupied, height, width):
        score = util.corner_check(head_pos, occupied, "up")
        move_score["up"] = score

    if util.choose_move("down", you, occupied, height, width):
        score = util.corner_check(head_pos, occupied, "down")
        move_score["down"] = score

    if util.choose_move("left", you, occupied, height, width):
        score = util.corner_check(head_pos, occupied, "left")
        move_score["left"] = score

    if util.choose_move("right", you, occupied, height, width):
        score = util.corner_check(head_pos, occupied, "right")
        move_score["right"] = score


    if not move_score:
        print("failure, no possible moves, trying to go towards tail")
        dir = 'left'
    else:
        best_moves = util.minimums(move_score)
        print("best moves are {}".format(best_moves))
        dir = random.choice(best_moves)
    print(dir)
    return dir