def explain_outfit(outfit, occasion):
    reasons = []

    for item in outfit:
        reasons.append(f"Includes {item.category} you like.")

        if item.formality < occasion.min_formality:
            reasons.append(f"{item.category} is slightly casual for {occasion.name}")
        elif item.formality > occasion.max_formality:
            reasons.append(f"{item.category} is slightly formal for {occasion.name}")

    return reasons