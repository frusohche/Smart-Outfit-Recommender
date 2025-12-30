from closet import closet
from recommender import recommend_outfit

def main():
    print("Welcome to the Outfit App")

    occasion = input("Where are you going? ").lower()

    outfit = recommend_outfit(closet, occasion)

    if outfit is None:
        print("Sorry, I don't know that occasion yet.")
    else:
        print("\nYour outfit:")
        for item, clothing in outfit.items():
            print(item.capitalize() + ": " + clothing)
main()
