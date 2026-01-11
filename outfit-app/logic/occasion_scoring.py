def occasion_score(outfit, occasion):
    socre = 0

    for item in outfit:
        if item.formality < occasion.min_formality:
            score -= 5
        elif item.formality > occasion.max_formality:
            score -= 5
        else:
            score += 3

    return score