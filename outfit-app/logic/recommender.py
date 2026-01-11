from scoring import formality_score
from data.preferences import preference_score
from logic.occasion_scoring import occasion_score
from logic.explanation import explain_outfit


def recommend_outfits(outfits, occasion):
    scored_outfits = []

    for outfit in outfits:
        top, bottom, shoe = outfit
        score = 0
        
        #Compatability scoring
        score += formality_score(top, bottom)
        score += formality_score(bottom, shoe)
        score += formality_score(top, shoe)

        #Personal preference scoring
        for item in outfit:
            score += preference_score(item.id)


        #Occasion awarness
        score += occasion_score(outfit, occasion)

        
        scored_outfits.append((score, outfit))

    scored_outfits.sort(reverse=True, key=lambda x: x[0])
    top_outfits = scored_outfits[:3]

    explanations = [explain_outfit(o, occasion) for _, o in top_outfits]
    return top_outfits, explanations

