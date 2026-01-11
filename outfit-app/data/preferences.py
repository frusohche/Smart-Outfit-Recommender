preferences = {}

def update_preference(item_id, liked):
    if item_id not in preferences:
        preferences[item_id] = 0

    if liked:
        preferences[item_id] += 1
    else:
        preferences[item_id] -= 1


def preference_score(item_id):
    return preferences.get(item_id, 0)