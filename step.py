
class step(object):
    method = []
    ingredients = []
    requirements = []
    title = ''
    name = ''

    def __repr__(self):
        return self.name


class soak(step):
    def __init__(self, mushroom, tags):
        self.title = "Prepare the {}".format(mushroom)
        self.name = "{}".format(mushroom)
        self.method = [
            "Rinse the dried mushrooms under cold water briefly, just to get rid of any grit and gunk.",
            "Then put the mushrooms in a little bowl and cover with warm-ish water for anywhere between 15 and 30 minutes.",
            "Mushrooms should be a bit squishy and a lot bigger by the time they're done.",
            "Take the mushrooms out and (gently) squeeze any excess liquid from them into the soaking liquid.",
            "If the stems still feel woody and tough, cut them off, and stick them in a bag in your freezer for next time you make stock (or to throw out in a year when you find a weird brown blob in your freezer and freak out).",
            "Hopefully there's not any remaining grit in the soaking liquid, but if there is, strain it into another container, and keep for the next step.",
            "If you end up with less than about a cup of liquid, add water until you have a cup.",
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
    def __init__(self, dumpling, tags):
        self.name = "{}".format(dumpling)
        if 'fancy' in dumpling.tags:
            self.title = "Make the {}".format(dumpling)
            if 'vegan' in dumpling.tags:
                egg = "unit of vegan egg replacer"
            else:
                egg = "egg"  # egg
            self.ingredients = [
                "4 large potatoes (russets, ideally)",
                "1 {egg}".format(egg=egg),  # egg
                "some plain flour (maybe 2 cups. maybe.)",
                "bitta salt",
            ]
            self.requirements = [
                "like four trays",
                "a big microwave-safe bowl",
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
                "Whisk the {egg} with some salt in a little bowl, using a fork, or a whisk if you're fancy.".format(egg=egg),  # egg
                "Assuming the potatoes are still on a tray, which is where we told to you to leave them, mound them up in a pile, and make a little dent in the middle. Pour in the {egg}, and kind of gently smoosh it all together.".format(egg = egg),  # egg
                "If you are rich in bench space, you can consider flouring a work surface at this time, but if you aren't, because who is, then just put about a cup of flour on top of the potato pile, then knead it all together.",
                "You'll want to knead gently, and only add in as much flour as you absolutely have to. This might be tricky, but you want the dough to be slightly firmer and slightly less sticky. Aim for about a minute and a half? If you knead it too much the gnoccs will be dense and chewy but honestly no-one will call you out on it, because you hand made gnocchi, you lunatic.",
                "Once you've got your dough, grab a chunk of it, and roll it out snake-style with your hands, on a reasonably clean and un-sticky surface (i.e. you'll need another tray, or to clean your bench, probably. sorry.). Cut the snake into little pillows and put them on yet *another* tray. Maybe put some flour down first, or some baking paper.",
                "Repeat the snake-make and snake-kill steps until you no longer have any dough, and do have a lot of little gnocchi.",
                "(optional) If you want to be fancy you can kind of roll a the gnocchi around your thumb with the back of a fork, or just poke them all with your finger so they have a nice dent. But you can also just not do that, and it'll be fine.",
            ]
            if 'vegan' in tags:
                self.method.insert(0, "Disclaimer: I have never made vegan gnocchi. But probably it'll be fine.")
                self.method.append("(optional) If you want, you can fry the gnocchi at this point. In a heavy pan with a bit of oil, over medium or high, put a single layer of gnocchi down, and leave them there until that one side is golden brown and delicious. Take them out and move on with your life.")
            elif 'no_dairy' in tags:
                self.method.append("(optional) If you want, you can fry the gnocchi at this point. In a heavy pan with a bit of oil, over medium or high, put a single layer of gnocchi down, and leave them there until that one side is golden brown and delicious. Take them out and move on with your life.")
            else:
                self.method.append("(optional) If you want, you can fry the gnocchi at this point. In a heavy pan with a bit of oil (or butter), over medium or high, put a single layer of gnocchi down, and leave them there until that one side is golden brown and delicious. Take them out and move on with your life.")
        else:
            self.ingredients = ["{}".format(dumpling)]
            self.requirements = []
            self.method = []
            if 'breatharian' in tags:
                self.requirements = [
                    "The will survive on light and air alone",
                ]
                self.method = [
                    "Much of this journey is a journey of discovery.",
                ]
                self.ingredients = ["just normal air"]


class sauce(step):
    def __init__(self, sauce, tags):
        self.name = "{}".format(sauce)
        if 'fancy' in sauce.tags:
            self.title = "Make a {}".format(sauce)
            self.ingredients = [
                '2 cans of tomatoes, crushed, diced or whole peeled.',
                'some garlic',
                'some basil or rosemary or something',
                'olive oil',
                'bitta salt',
                'black pepper and other spices to taste',
            ]
            self.requirements = [
                "a big heavy pan or pot",
                "a grater or knife",
                "maybe a potato masher",
                "wooden spoon",
            ]
            self.method = [
                "Grate, or finely chop, your garlic, then heat a tablespoon or so of oil (just pour it in until it covers more than half the pot bottom, or a quarter if it's a really wide pan) and throw in the garlic and a bit of salt. Maybe some pepper.",
                "You will note there is no more specific amount than 'some' for garlic here. This is not an error, put in as much garlic as you can be bothered to do. I mean, if you're getting on for a whole head, maybe slow down, there's not that much tomato here, but go with how you feel.",
                "Stir the garlic around in the oil for maybe 20 seconds, until it starts to get super fragrant and delicious, then (carefully, because the oil might spatter) pour in the tomatoes.",
                "If the tomatoes are in big chunks, bash them with the masher until they aren't in big chunks anymore. Otherwise you can crush them in your gripping hands before you pour them in (good thing you read the whole recipe through, right?).",
                "Put in the basil or rosemary or whatever herbs you have.",
                "You can also add any other spices, like chilli flakes or paprika, at this point.",
                "Let the sauce simmer gently (reduce the heat until it is no longer threatening you with napalm death), stirring every 10 minutes or so, until it's reduced by a quarter to a half. Maybe an hour or so?",
                "Take the herbs out at the end - doesn't matter if there's a few bits in there, but don't leave the stems in, you know?",
            ]
        elif 'breatharian' in tags:
            self.ingredients = [
                "a fresh mountain breeze",
            ]
            self.requirements = [
                "The mystical ability to survive on light and air alone",
            ]
            self.method = [
                "You cannot be told the method, you have to receive the gnoccis",
            ]
        else:
            self.ingredients = ["{}".format(sauce)]
            self.requirements = []
            self.method = []


class assemble(step):
    def __init__(self, protein, gnocchi, liquid, sauce, tags):
        self.title = "Make gnocchi"
        self.name = 'final assembly'
        self.ingredients = [
            protein,
            'olive oil',
            'bitta salt',
            'black pepper and other spices to taste',
        ]
        self.requirements = [
            "a big heavy pan or pot",
            "wooden spoon",
        ]
        self.method = [
            "Now is a good time to put in some crushed garlic, fresh cracked black pepper, etc, if you have it. But if you don't: don't worry!",
            "Pour in your {sauce} (carefully, because sauce into oil will splatter) and cook it for about 30 seconds, scraping up any fond that's developed on the bottom of the pan.".format(sauce=sauce),
            "Check the sauce for seasoning - it will get saltier as it cooks down, but if you don't think it'll be salty enough, add more. Your cardiologist isn't watching (probably)."
            "Add your {gnocchi}, stir, then add your {liquid}.".format(gnocchi=gnocchi, liquid=liquid),
            "Stir it again, then cook it for anywhere between three to ten minutes, until the sauce has reduced in volume to about where it was before you put the {liquid} in, and/or the gnocchi are tender.".format(liquid=liquid),
            "Put the gnocchi in some bowls and serve it!",
        ]
        if 'vegan' in tags or 'no_dairy' in tags:
            self.method.append("Add some of that jar of crispy fried shallots you have in the cupboard for some reason, if you're feeling fancy.")
        if protein.type == 'mushroom':
            self.method.insert(0, "Put some oil (like a tablespoon) in the pan, then put your {protein} in the pan and cook it down until it's browned and has lost a lot of liquid.".format(protein=protein))
            self.method.insert(1, "(General mushroom interlude) If you're cooking mushrooms, you can probably cook them for longer. They can take it. Just keep cooking them! No, more - just stop before they actually burn. Ok no not that far, sorry.",)
            if 'vegan' not in tags and 'no_dairy' not in tags:
                self.method.append("Add some parmesan or pecorino on top, or maybe some of that jar of crispy fried shallots you have in the cupboard for some reason, if you're feeling fancy.")
        if protein.type == 'cheese':
            self.method.insert(0, "Cut up your {protein} into cubes about half as wide as your {gnocchi}. If it's been soaking in brine, let it drain for a bit.".format(protein=protein, gnocchi=gnocchi))
            self.method.insert(1, "Put some oil (like a tablespoon) in the pan and heat it up. Then put your {protein} in the pan and cook it until it's browned. Let it sit on each side for a minute or so (or less if your pan is very hot or the {protein} is very small), then flip it to an unbrowned side. Then take it out and put it in a bowl for a bit.".format(protein=protein))
        elif protein.type == 'bacon':
            self.method.insert(0,"Put some oil (like a tablespoon) in the pan, then put your {protein} in the pan and cook it down until it's browned and has released a lot of fat.".format(protein=protein))
            if 'no_dairy' not in tags:
                self.method.append("Add some parmesan or pecorino on top, or maybe some of that jar of crispy fried shallots you have in the cupboard for some reason, if you're feeling fancy.")
        elif protein.type == 'air':
            self.ingredients = ['the breath of the storm']
            self.method = [
                'Clatter the spoon in the pot. Clang! Clang! Breathe deep the breath of the storm! Are you not nourished?',
                'Gently scrape the spoon in the pot. Sip the fresh mountain breeze. Are you not fed?',
                'Weakly tap the spoon on the pot. Gasp feebly at the normal air. Perhaps if you tap harder, they\'ll hear you, and they\'ll come.',
            ]
