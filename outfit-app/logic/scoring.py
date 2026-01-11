def formality_score(item1, item2):
    difference = abs(item1.formaility - item2.formality)

    if difference == 0:
        return 10
    elif difference == 1:
        return 5
    elif difference == 2:
        return 0
    else:
        return -5