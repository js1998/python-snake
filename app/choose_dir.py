import food
import survive

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

    # Dying so go get food
    if foods and (health < 50 or data['turn'] < 4):
        nearest_food = food.getClosestFood(foods, you[0])
        print("headloc({} {}) + foodloc({} {})".format(body_pos[0]['x'], body_pos[0]['y'], nearest_food['x'], nearest_food['y']))
        return food.directionToFood(food=nearest_food,
                                    you=you,
                                    occupied=body_pos,
                                    height=height,
                                    width=width)

    # Chase tail to stall out
    else:
        return survive.findTail(you, body_pos, width, height)
