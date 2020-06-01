import argparse
import sys
import random
import copy


substitutions = {
    "bacon": "Bacon, ham, salami, whatever cured meat that's still food you can find in your fridge. Or mushrooms, or any of the substitutions for mushrooms.",
    "mushroom": "Any other kind of mushroom you can find, or textured vegetable protein. Maybe sliced zucchini or eggplant. Conceivably you could also use tofu, beans or chickpeas, but you'll need to figure out how to cook those yourself, and they're probably an odd texture with gnocchi.",
    "onion": "Any onion, leeks, shallots, eschalots, spring onion or chives (add green stuff much closer to the end than the standard onion adding time). Or nothing.",
    "garlic": "Garlic powder, garlic granules, any onion type object, hing (tiny amounts! With the tomatoes! Be careful!). Or nothing.",
    "gnocchi": "Any pasta, but try to keep to similar size/shape to the gnocchi.  Think bow ties or seashells, not so much spaghetti. Cook for half to three quarters as long as the package suggests and add after the tomato sauce is cooked down, with a bit of the pasta water, and finish in the sauce. Alternatively, chickpeas or large beans like gigantes or butter beans (fresh or dried but obviously you'll have to cook the dried ones and it'll take a lot longer).",
    "tomato": "Any kind of tomato-based pasta sauce, canned tomatoes of any kind (you'll need to cook them down longer), tomato paste/dried tomato paste and water if you're desperate, fresh tomatoes (grate them on a box grater and cook them down for a long, long time), or yr classic heinz tomato sauce (do not do this).",
    "air": "You can use any non-toxic gas, but stick to noble gases, or at least those that don't react explosively to heat when air is around, until you're more confident. You should be able to source some air in most circumstances, though.",
}





steps = {
    "soak": step(),
    "pasta": {},
    "sauce": {},
    "assemble": {},
}

class step(object):
    method = []
    ingredients = []
    requirements = []

    def __repr__(self):
        # pretty print
        return repr(self.method)

class soak(step):
    def __init__(self, mushroom):
        self.method = [
            "Rinse the dried mushrooms under cold water briefly, just to get rid of any grit and gunk.",
            "Then put the mushrooms in a little bowl and cover with warm-ish water for anywhere between 15 and 30 minutes.",
            "Mushrooms should be a bit squishy and a lot bigger by the time they're done.",
            "Take the mushrooms out and (gently) squeeze any excess liquid from them into the soaking liquid.",
            "If the stems still feel woody and tough, cut them off, and stick them in a bag in your freezer for next time you make stock (or to throw out in a year when you find a weird brown blob in your freezer and freak out).",
            "Hopefully there's not any remaining grit in the soaking liquid, but if there is, strain it into another container, and keep for the next step.",
            "If you end up with less than about a cup of water, add water until you have a cup.",
        ]
        self.ingredients = [
            mushroom,
            "water"
        ]
        self.requirements = [
            "A bowl",
            "Maybe a strainer"
        ]

class dumpling(step):
    # namespace issues tbh
    def __init__(self, dumpling):
        if 'vegan' in dumpling:
            egg = "egg replacer"
        else:
            egg = "egg"  # egg
        self.ingredients = [
            "4 large potatoes (russets, ideally)",
            "1 {egg}".format(egg = egg),  # egg
            "some plain flour (maybe 2 cups. maybe.)",
            "bitta salt",
        ]
        self.requirements = [
            "like four trays",
            "a big microwave-safe bowl"
            "a little bowl",
            "plastic wrap",
            "a potato ricer/grater/masher",
            "a fork",
        ]
        self.method = [
            "Peel your potatoes, then chop them into 8ths (you can do this, it's in half, then in half again, then in half again. I'm sure you're familiar with the progression).",
            "Chuck them in a bowl, cover with plastic wrap, and poke a hole in the wrap for steam to escape.",
            "Then nuke them in the microwave until they're pretty tender (I know this is 'fancy' but the other option is bake them for an hour then peel them. It is too much work).",
            "The time it takes will depend on your microwave. Start at maybe three minutes, then go by minute intervals. Poke the potatoes with a sharpish knife, it should slide in without much resistance, then the potato should fall off again.",
            "The potatoes will be hot as hell at this point, so spread them on a tray and put them somewhere out of the way until they're just warm.",
            "Once they're not made of lava, put them in a potato ricer and rice 'em. Or, if you don't have a ricer, grate them on the small holes on your grater. If you don't have a ricer or a grater, why are you reading fancy recipes? I can't help you. Well, I guess just mash them. Whatever, there's no wrong answers, just gummy gnocchi.",
            "Whisk the {egg} with some salt in a little bowl, using a fork, or a whisk if you're fancy.".format(egg = egg),  # egg
            "Assuming the potatoes are still on a tray, which is where we told to you to leave them, mound them up in a pile, and make a little dent in the middle. Pour in the {egg}, and kind of gently smoosh it all together.".format(egg = egg),  # egg
            "If you are rich in bench space, you can consider flouring a work surface at this time, but if you aren't, because who is, then just put about a cup of flour on top of the potato pile, then knead it all together.",
            "You'll want to knead gently, and only add in as much flour as you absolutely have to. This might be tricky, but you want the dough to be slightly firmer and slightly less sticky. Aim for about a minute and a half? If you knead it too much the gnoccs will be dense and chewy but honestly no-one will call you out on it, because you hand made gnocchi, you lunatic.",
            "Once you've got your dough, grab a chunk of it, and roll it out snake-style with your hands, on a reasonably clean and un-sticky surface (i.e. you'll need another tray, or to clean your bench, probably. sorry.). Cut the snake into little pillows and put them on yet *another* tray. Maybe put some flour down first, or some baking paper.",
            "Repeat the snake-make and snake-kill steps until you no longer have any dough, and do have a lot of little gnocchi.",
            "(optional) If you want to be fancy you can kind of roll a the gnocchi around your thumb with the back of a fork, or just poke them all with your finger so they have a nice dent. But you can also just not do that, and it'll be fine.",
            "(optional) If you want, you can fry the gnocchi at this point. In a heavy pan with a bit of oil (or butter), over medium or high, put a single layer of gnocchi down, and leave them there until that one side is golden brown and delicious. Take them out and move on with your life.",
        ]

            
        


class ingredient(object):
    def __init__(self, name, tags=[], type=None):
        self.name = name
        self.tags = tags
        self.type = type

    def __repr__(self):
        return repr(self.name)


class gnocchi(object):
    proteins = [
        ingredient("pre-chopped bacon", tags=["fast", "cheap"], type="bacon"),
        ingredient("bacon", tags=["cheap"], type="bacon"),
        ingredient("smoked panchetta", tags=["fancy"], type="bacon"),
        ingredient("guanciale", tags=["fancy"], type="bacon"),
        ingredient("pre-chopped mushrooms", tags=["fast", "cheap", "vegetarian", "vegan"], type="mushroom"),
        ingredient("white button mushrooms", tags=["cheap", "vegetarian", "vegan"], type="mushroom"),
        ingredient("shiitake mushrooms", tags=["fancy", "vegetarian", "vegan"], type="mushroom"),
        ingredient("porcini mushrooms", tags=["fancy", "vegetarian", "vegan"], type="mushroom"),
        ingredient("dried shiitake mushrooms", tags=["fancy", "dried", "vegetarian", "vegan"], type="mushroom"),
        ingredient("dried porcini mushrooms", tags=["fancy", "dried", "vegetarian", "vegan"], type="mushroom"),
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
            print(k,v)
            if v and k in ['fast', 'fancy', 'cheap', 'vegetarian', 'vegan', 'breatharian']:
                self.tags.append(k)
        self.ingredient = {}
        self.ingredients()

    def ingredients(self):
        if self.breatharian:
            self.ptype = "air"
        elif self.vegetarian or self.vegan:
            self.ptype = "mushroom"
        else:
            self.ptype = "bacon"
        self.get_protein()
        self.get_liquid()
        self.get_sauce()
        self.get_pasta()
        print(self.pasta)
        print(self.liquid)
        print(self.protein)
        print(self.sauce)
        self.get_steps()


    def get_protein(self):
        candidates = [protein for protein in self.proteins if protein.type==self.ptype]
        # constrain to tags
        if self.tags:
            for tag in self.tags:
                candidates = [protein for protein in candidates if tag in protein.tags or 'any' in protein.tags]
        self.protein = random.choice(candidates)

    def get_liquid(self):
        candidates = [liquid for liquid in self.liquids if 'breatharian' not in liquid.tags]
        if "dried" in self.protein.tags:
            candidates = [liquid for liquid in self.liquids if liquid.name=="mushroom liquid"]
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
        self.steps=[]
        if "dried" in self.protein.tags:
            self.steps.append('soak')
        if "fancy" in self.pasta.tags:
            self.steps.append('gnocchi')
        if "fancy" in self.sauce.tags:
            self.steps.append('sauce')
        self.steps.append('assemble')
        print(self.steps)


    def methods(self):
        pass

    def printout(self):
        pass


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
    # print(dir(args))
    # print(vars(args))
    # secret args
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