def generate_outfits(tops, bottoms, shoes):
    outfits = []

    for top in tops:
        for bottom in bottoms:
            for shoe in shoes:
                #Basic constraint
                if abs(top.formality - shoe.formality) > 2:
                    continue

                outfits.append((top, bottom, shoe))
    
    return outfits