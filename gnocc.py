import argparse
import sys


substitutions = {
    "bacon": "Bacon, ham, salami, whatever cured meat that's still food you can find in your fridge. Or mushrooms, or any of the substitutions for mushrooms.",
    "mushroom": "Any other kind of mushroom you can find, or textured vegetable protein. Maybe sliced zucchini or eggplant. Conceivably you could also use tofu, beans or chickpeas, but you'll need to figure out how to cook those yourself, and they're probably an odd texture with gnocchi.",
    "onion": "Any onion, leeks, shallots, eschalots, spring onion or chives (add green stuff much closer to the end than the standard onion adding time). Or nothing.",
    "garlic": "Garlic powder, garlic granules, any onion type object, hing (tiny amounts! With the tomatoes! Be careful!). Or nothing."
    "gnocchi": "Any pasta, but try to keep to similar size/shape to the gnocchi.  Think bow ties or seashells, not so much spaghetti. Cook for half to three quarters as long as the package suggests and add after the tomato sauce is cooked down, with a bit of the pasta water, and finish in the sauce. Alternatively, chickpeas or large beans like gigantes or butter beans (fresh or dried but obviously you'll have to cook the dried ones and it'll take a lot longer).",
    "tomato": "Any kind of tomato-based pasta sauce, canned tomatoes of any kind (you'll need to cook them down longer), tomato paste/dried tomato paste and water if you're desperate, fresh tomatoes (grate them on a box grater and cook them down for a long, long time), or yr classic heinz tomato sauce (do not do this).",
    "air": "You can use any non-toxic gas, but stick to noble gases, or at least those that don't react explosively to heat when air is around, until you're more confident. You should be able to source some air in most circumstances, though.",
}

proteins = {
    "pre-chopped bacon": {
        "tags": ["fast", "cheap"],
        "type": "bacon",
    },
    "bacon": {
        "tags": ["cheap"],
        "type": "bacon",
    },
    "smoked panchetta": {
        "tags": ["fancy"],
        "type": "bacon",
    },
    "guanciale": {
        "tags": ["fancy"],
        "type": "bacon",  
    },
    "pre-chopped mushrooms": {
        "tags": ["fast", "cheap"],
        "type": "mushroom",
    },
    "white button mushrooms": {
        "tags": ["cheap"],
        "type": "mushroom",
    },
    "shiitake mushrooms": {
        "tags": ["fancy"],
        "type": "mushroom",
    },
    "porcini mushrooms": {
        "tags": ["fancy"],
        "type": "mushroom",
    },
    "dried shiitake mushrooms": {
        "tags": ["fancy", "dried"],
        "type": "mushroom",
    },
    "dried porcini mushrooms": {
        "tags": ["fancy", "dried"],
        "type": "mushroom",
    },
    "air": {
        "tags": ["breatharian"],
        "type": "air",
    },
}


class gnocchi(object):

    def __init__(self, args):
        for k, v in vars(args).items():
            setattr(self, f'{k}', v)
        print(dir(self))
        self.ingredient = {}
        self.ingredients()

    def ingredients(self):
        pass

    def get_protein(self):


    def methods(self):
        pass

    def printout(self):
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fast", help="Fast Mode. Do as little actual cooking as posisble.", action="store_true")
    parser.add_argument("--fancy", help="Fancy Mode. Do as much actual cooking as possible.", action="store_true")
    parser.add_argument("-c", "--cheap", help="We're not made of money, {$USER}.", action="store_true")
    parser.add_argument("-i", "--imperial", help="Imperial Mode, for imperialists.", action="store_true")
    parser.add_argument("-p", "--pantry", help="Pantry Mode. List possible substitutions if you don't have some ingredient.", action="store_true")
    parser.add_argument("-b", "--blog", help="Blog Mode. Adds long, discursive ramble about the time you went to Italy to the beginning of the recipe.", action="store_true")
    parser.add_argument("-n", "--no-dairy", help="Dairy Free Mode. No mammals allowed.", action="store_true")
    vegos = parser.add_mutually_exclusive_group()
    vegos.add_argument("-v", "--vegetability", action="count",
                        help="increase recipe vegetability. -v for vegetarian, -vv for vegan. OR:", default=0)
    vegos.add_argument("--vegetarian", action="store_true", help="Vegetarian Mode.")
    vegos.add_argument("--vegan", action="store_true", help="Vegan Mode.")

    args = parser.parse_args()
    # print(dir(args))
    # print(vars(args))
    # secret args
    parser.add_argument("--breatharian", action="store_true")
    parser.parse_args()

    if args.vegetability > 2:
        args.breatharian = True
    elif args.vegetability == 2:
        args.vegan = True
    elif args.vegetability == 1:
        args.vegetarian = True

    if args.imperial:
        sys.exit("No. There's barely and measurements in this recipe but also just l2metric, c'mon")
    g = gnocchi(args)

if __name__ == "__main__":
    main()