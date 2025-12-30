import random

def recommend_outfit(closet, occasion):
    if occasion == "casual":
        top = random.choice(closet["tops"])
        bottom = random.choice(closet["bottoms"])
        shoes = random.choice(closet["shoes"])
        return {
            "top": top,
            "bottom": bottom,
            "shoes": shoes
        }
    else:
        return None