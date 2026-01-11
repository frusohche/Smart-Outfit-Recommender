from data.preferences import preferences

def give_feedback(outfit, liked: bool):
    """
    Updates preference scores for each item in the outfit.
    liked=True -> increase score
    liked=False -> decrease score
    """
    for item in outfit:
        if item.id not in preferences:
            preferences[item.id] = 0

        if liked:
            preferences[item.id] += 1
        else:
            preferences[item.id] -= 1