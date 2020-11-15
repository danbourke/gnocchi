import argparse
import sys
import random
import step


substitutions = {
    "bacon": "Bacon, ham, salami, whatever cured meat that's still food you can find in your fridge. Or mushrooms, or any of the substitutions for mushrooms.",
    "mushroom": "Any other kind of mushroom you can find, or textured vegetable protein. Maybe sliced zucchini or eggplant. Conceivably you could also use tofu, beans or chickpeas, but you'll need to figure out how to cook those yourself, and they're probably an odd texture with gnocchi.",
    "haloumi": "I'd guess paneer, spanakopita, etc? Perhaps fetta?",
    "onion": "Any onion, leeks, shallots, eschalots, spring onion or chives (add green stuff much closer to the end than the standard onion adding time). Or nothing.",
    "garlic": "Garlic powder, garlic granules, any onion type object, hing (tiny amounts! With the tomatoes! Be careful!). Or nothing.",
    "gnocchi": "Any pasta, but try to keep to similar size/shape to the gnocchi.  Think bow ties or seashells, not so much spaghetti. Cook for half to three quarters as long as the package suggests and add after the tomato sauce is cooked down, with a bit of the pasta water, and finish in the sauce. Alternatively, chickpeas or large beans like gigantes or butter beans (fresh or dried but obviously you'll have to cook the dried ones and it'll take a lot longer).",
    "tomato": "Any kind of tomato-based pasta sauce, canned tomatoes of any kind (you'll need to cook them down longer), tomato paste/dried tomato paste and water if you're desperate, fresh tomatoes (grate them on a box grater and cook them down for a long, long time), or yr classic heinz tomato sauce (do not do this).",
    "air": "You can use any non-toxic gas, but stick to noble gases, or at least those that don't react explosively to heat when air is around, until you're more confident. You should be able to source some air in most circumstances, though.",
}


class ingredient(object):
    def __init__(self, name, tags=[], type=None):
        self.name = name
        self.tags = tags
        self.type = type

    def __repr__(self):
        return self.name


class gnocchi(object):
    proteins = [
        ingredient("pre-chopped bacon", tags=["fast", "cheap", "no_dairy"], type="bacon"),
        ingredient("bacon", tags=["cheap", "no_dairy"], type="bacon"),
        ingredient("smoked panchetta", tags=["fancy", "no_dairy"], type="bacon"),
        ingredient("guanciale", tags=["fancy", "no_dairy"], type="bacon"),
        ingredient("pre-chopped mushrooms", tags=["fast", "cheap", "vegetarian", "vegan", "no_dairy"], type="mushroom"),
        ingredient("white button mushrooms", tags=["cheap", "vegetarian", "vegan", "no_dairy"], type="mushroom"),
        ingredient("shiitake mushrooms", tags=["fancy", "vegetarian", "vegan", "no_dairy"], type="mushroom"),
        ingredient("porcini mushrooms", tags=["fancy", "vegetarian", "vegan", "no_dairy"], type="mushroom"),
        ingredient("dried shiitake mushrooms", tags=["fancy", "dried", "vegetarian", "vegan", "no_dairy"], type="mushroom"),
        ingredient("dried porcini mushrooms", tags=["fancy", "dried", "vegetarian", "vegan", "no_dairy"], type="mushroom"),
        ingredient("haloumi", tags=["vegetarian"], type="cheese"),
        ingredient("air", tags=["breatharian"], type="air"),
    ]
    liquids = [
        ingredient("water", tags=["fast", "cheap", "any"]),
        ingredient("stock", tags=["any"]),
        ingredient("home-made stock", tags=["fancy"]),
        ingredient("mushroom liquid", tags=["dried"]),
        ingredient("wine", tags=["fancy"]),
        ingredient("air", tags=["breatharian"]),
    ]
    pastas = [
        ingredient("pre-made gnocchi", tags=["any", "vegetarian"]),
        ingredient("home-made gnocchi", tags=["fancy", "vegetarian"]),
        ingredient("home-made vegan gnocchi", tags=["fancy", "vegetarian", "vegan"]),
        ingredient("pre-made vegan gnocchi", tags=["any", "vegetarian", "vegan"]),
        ingredient("air", tags=["breatharian"]),
    ]

    sauces = [
        ingredient("passata", tags=["any", "vegetarian", "vegan"]),
        ingredient("home-made tomato sauce", tags=["fancy", "vegetarian", "vegan"]),
        ingredient("air", tags=["breatharian"]),
    ]

    def __init__(self, args):
        self.tags = []
        for k, v in vars(args).items():
            setattr(self, f'{k}', v)
            if v and k in ['fast', 'fancy', 'cheap', 'vegetarian', 'vegan', 'breatharian', 'no_dairy']:
                self.tags.append(k)
        self.ingredient = {}
        self.get_ingredients()
        self.get_name()
        self.get_steps()
        self.printout()

    def get_ingredients(self):
        if self.breatharian:
            self.ptype = "air"
        elif self.vegan or (self.vegetarian and self.no_dairy):
            self.ptype = "mushroom"
        elif self.vegetarian and not self.no_dairy:
            self.ptype = random.choice(["mushroom", "mushroom", "cheese"])  # m'biased selection
        else:
            self.ptype = random.choice(["mushroom", "mushroom", "cheese", "bacon", "bacon", "bacon"])  # m'even more biased selection
        self.get_protein()
        self.get_liquid()
        self.get_sauce()
        self.get_pasta()

    def get_name(self):
        self.name = "{} in {} with {}".format(self.pasta, self.sauce, self.protein)

    def get_protein(self):
        candidates = [protein for protein in self.proteins if protein.type == self.ptype]
        # constrain to tags
        if self.tags:
            for tag in self.tags:
                candidates = [protein for protein in candidates if tag in protein.tags or 'any' in protein.tags]
        self.protein = random.choice(candidates)

    def get_liquid(self):
        candidates = [liquid for liquid in self.liquids if 'breatharian' not in liquid.tags]
        if "dried" in self.protein.tags:
            candidates = [liquid for liquid in self.liquids if liquid.name == "mushroom liquid"]
        elif self.tags:
            for tag in self.tags:
                candidates = [liquid for liquid in self.liquids if tag in liquid.tags or 'any' in liquid.tags]
        self.liquid = random.choice(candidates)

    def get_sauce(self):
        candidates = [sauce for sauce in self.sauces if 'breatharian' not in sauce.tags]
        if self.tags:
            for tag in self.tags:
                candidates = [sauce for sauce in self.sauces if tag in sauce.tags or 'any' in sauce.tags]
        self.sauce = random.choice(candidates)

    def get_pasta(self):
        candidates = [pasta for pasta in self.pastas if 'breatharian' not in pasta.tags]
        if self.tags:
            for tag in self.tags:
                candidates = [pasta for pasta in self.pastas if tag in pasta.tags or 'any' in pasta.tags]
        self.pasta = random.choice(candidates)

    def get_steps(self):
        self.steps = []
        if "dried" in self.protein.tags:
            self.steps.append(step.soak(self.protein, self.tags))
        self.steps.append(step.dumpling(self.pasta, self.tags))
        self.steps.append(step.sauce(self.sauce, self.tags))
        self.steps.append(step.assemble(self.protein, self.pasta, self.liquid, self.sauce, self.tags))

    def printout(self):
        # collect all ingredients, methods, etc, in one place. ish.
        ingredient_dict = {}
        method_dict = {}
        requirements_dict = {}

        for bit in self.steps:
            if len(bit.ingredients) > 0:
                ingredient_dict[bit] = bit.ingredients
            if len(bit.method) > 0:
                method_dict[bit] = bit.method
            if len(bit.requirements) > 0:
                requirements_dict[bit] = bit.requirements
        print("# {}".format(self.name))
        print("\n")
        print("## Requirements")
        for bit in self.steps:
            reqs = requirements_dict.get(bit)
            if reqs:
                print("### For the {}".format(bit))
                for req in reqs:
                    print("* {}".format(req))
        print('\n')
        print("## Ingredients")
        for bit in self.steps:
            ingredients = ingredient_dict.get(bit)
            if ingredients:
                print("### For the {}".format(bit))
                for ingredient in ingredients:
                    print("* {}".format(ingredient))
        print('\n')
        print("## Methods")
        for bit in self.steps:
            methods = method_dict.get(bit)
            if methods:
                print("### {}".format(bit))
                for method in methods:
                    print("{}".format(method))
                print('\n')


def main():
    parser = argparse.ArgumentParser()
    ff = parser.add_mutually_exclusive_group()
    ff.add_argument("--fast", help="Fast Mode. Do as little actual cooking as posisble.", action="store_true")
    ff.add_argument("--fancy", help="Fancy Mode. Do as much actual cooking as possible.", action="store_true")
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
    parser.add_argument("--breatharian", action="store_true")
    args = parser.parse_args()

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
