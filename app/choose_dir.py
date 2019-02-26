import food
import survive

def calculateDirection(data):
    foods = data["board"]["food"]
    curr_pos = data["you"]["body"]
    height = data["board"]["height"]
    width = data["board"]["width"]
    health = data["you"]['health']

    print('turn number {}'.format(data['turn']))

    # Dying so go get food
    if health < 50 or data['turn'] < 6:
        nearest_food = food.getClosestFood(foods, curr_pos[0])
        print("headloc({} {}) + foodloc({} {})".format(curr_pos[0]['x'], curr_pos[0]['y'], nearest_food['x'], nearest_food['y']))
        return food.directionToFood(nearest_food, curr_pos, height, width)

    # Chase tail to stall out
    else:
        return survive.findTail(curr_pos, width, height)
