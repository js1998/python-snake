import food
import survive
import move

def calculateDirection(data):
    foods = data["board"]["food"]

    height = data["board"]["height"]
    width = data["board"]["width"]
    health = data["you"]['health']

    you = data["you"]["body"]

    body_pos = []
    snakes = data["board"]["snakes"]
    for snake in snakes:
        body_pos.extend(snake['body'])

    print("turn number {}".format(data["turn"]))

    #Dying so go get food
    if health < 50 or data['turn'] < 6:
        nearest_food = food.getClosestFood(foods, you[0])
        #TODO: pass all foods instead for fallback in case nearest food is unreachable
        print("headloc({} {}) + foodloc({} {})".format(body_pos[0]['x'], body_pos[0]['y'], nearest_food['x'], nearest_food['y']))
        return move.find_next_direction(body_pos, you, height, width, nearest_food)

    # Chase tail to stall out
    else:
        return survive.findTail(you, body_pos, width, height)
