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
    snake_heads = []
    snakes = data["board"]["snakes"]
    for snake in snakes:
        snake_heads.append(snake["body"][0])
        body_pos.extend(snake['body'])
        snake_heads.append(snake["body"][0])

    print("turn number {}".format(data["turn"]))

    #Dying so go get food
    if health < 50 or data['turn'] < 6:
        nearest_food = food.get_closest_food(foods, you[0])
        #TODO: pass all foods instead for fallback in case nearest food is unreachable
        print("headloc({} {}) + foodloc({} {})".format(body_pos[0]['x'], body_pos[0]['y'], nearest_food['x'], nearest_food['y']))
        return move.find_next_direction(body_pos, snake_heads ,you, height, width, nearest_food)

    # Chase tail to stall out
    else:
        return survive.find_tail(you=you,
                                 occupied=body_pos,
                                 snake_heads=snake_heads,
                                 width=width,
                                 height=height)
