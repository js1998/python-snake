import food
import survive
import move


def calculate_direction(data):
    foods = data["board"]["food"]

    height = data["board"]["height"]
    width = data["board"]["width"]
    health = data["you"]['health']

    you = data["you"]["body"]

    body_pos = []
    snakes = data["board"]["snakes"]
    for snake in snakes:
        body_pos.extend(snake['body'])
    tail = you[-1]
    if tail in body_pos:
        body_pos.remove(tail)

    print("turn number {}".format(data["turn"]))

    #Dying so go get food

    if health < 75 or len(you) < 7:
        nearest_food = move.get_closest_food(foods, you[0])
        #TODO: pass all foods instead for fallback in case nearest food is unreachable
        print("headloc({} {}) + foodloc({} {})".format(body_pos[0]['x'], body_pos[0]['y'], nearest_food['x'], nearest_food['y']))
        my_move = move.find_next_direction(body_pos, you, height, width, nearest_food)
        if my_move:
            return my_move
        else:
            print("surviving")
            return survive.find_tail(you, body_pos, width, height)

    # Chase tail to stall out
    else:
        return survive.find_tail(you, body_pos, width, height)
