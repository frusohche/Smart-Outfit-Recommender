class ClothingItem:
    def _init_(self, id, category, color, style, season, formality):
        if formality < 1 or formality > 5:
            raise ValueError("Formality must be between 1 and 5.")
        self.id = id
        self.category = category    #top, bottom, soes, outerwear
        self.color = color          #black, white, blue, etc.
        self.style = style          #casual, formal, streetwear
        self.season = season        # summer, winter, spring, fall
        self.formality = formality  #1(very casual) -> 5 (very formal)