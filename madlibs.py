#Mini Madlib
#adj = input("Choose an adj ")
#print("It was a " + adj + " day")

#Colors
class colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE  = '\33[37m'
#Lists for different word types
adjectives = list()
names = list()
verbs = list()
places = list()
nouns = list()
#Function asks for names and puts them in a list
def add_name_list():
    runtime = 0
    while runtime !=2:
        name = input(colors.BLUE + "Enter a name! ")
        names.append(name)
        runtime += 1
#Function asks for adjectives and puts them in a list
def add_adj_list():
    runtime = 0
    while runtime !=4:
        adj = input(colors.PURPLE + "Enter an adjective! ")
        adjectives.append(adj)
        runtime += 1
#Function asks for verbs and puts them in a list
def add_verb_list():
    runtime = 0
    while runtime !=3:
        verb = input(colors.RED + "Enter a verb! (no ing at end) ")
        verbs.append(verb)
        runtime += 1
#Function asks for places and puts them in a list
def add_place_list():
    runtime = 0
    while runtime !=2:
        place = input(colors.GREEN + "Enter a place! ")
        places.append(place)
        runtime += 1
#Function asks for nouns and puts them in a list
def add_noun_list():
        runtime = 0
        while runtime !=2:
                noun = input(colors.YELLOW + "Enter a noun! ")
                nouns.append(noun)
                runtime += 1
#Funtion lists items to test its working
def list_all_items():
    for list_item in names,adjectives,verbs,places,nouns:
        print(list_item)
#Asks for inputs by activating my functions
add_name_list()
add_noun_list()
add_adj_list()
add_verb_list()
add_place_list()
#Lists every input
#list_all_items()
#The story
print(colors.WHITE + "A long time ago in a " + colors.GREEN + places[0] + colors.WHITE + " far, far away... the " + colors.PURPLE + adjectives[0] + colors.WHITE +  " evil coperation " + colors.YELLOW + nouns[0] + colors.WHITE + " tech developed a " + colors.YELLOW + nouns[1]
+ colors.WHITE + ". This " + colors.YELLOW + nouns[1] + colors.WHITE + " forced the users to repeatedly " + colors.RED + verbs[0] + colors.WHITE + ". This Angered a user of the product named " + colors.BLUE + names[0]
+ colors.WHITE + ", this user was skilled in the art of " + colors.RED + verbs[1] + colors.WHITE + "(ing) this allowed " + colors.BLUE + names[0] + colors.WHITE + " to face the evil coperation's head boss, " + colors.BLUE + names[1]
+ colors.WHITE + ". The head boss was also profficent in a skill, their hobby is " + colors.RED + verbs[2] + colors.WHITE + "(ing), However " + colors.BLUE + names[0] + colors.WHITE + " was feeling very " + colors.PURPLE + adjectives[1]
+ colors.WHITE + " this day and out skilled the boss, this caused the boss to feel very " + colors.PURPLE + adjectives[2] + colors.WHITE + ", with the evil coperation " + colors.YELLOW + nouns[0]
+ colors.WHITE + " tech defeated, people could return to there normal lives. The one and true saviour " + colors.BLUE + names[0] + colors.WHITE + " returned to his " + colors.PURPLE + adjectives[3] + colors.WHITE + " " + colors.GREEN + places[1]
+ colors.WHITE + " and lived happily ever after.")
