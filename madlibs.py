#Mini Madlib
#adj = input("Choose an adj ")
#print("It was a " + adj + " day")

#Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
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
        name = input("Enter a name! ")
        names.append(name)
        runtime += 1
#Function asks for adjectives and puts them in a list
def add_adj_list():
    runtime = 0
    while runtime !=3:
        adj = input("Enter an adjective! ")
        adjectives.append(adj)
        runtime += 1
#Function asks for verbs and puts them in a list
def add_verb_list():
    runtime = 0
    while runtime !=3:
        verb = input("Enter a verb! (no ing at end) ")
        verbs.append(verb)
        runtime += 1
#Function asks for places and puts them in a list
def add_place_list():
    runtime = 0
    while runtime !=2:
        place = input("Enter a place! ")
        places.append(place)
        runtime += 1
#Function asks for nouns and puts them in a list
def add_noun_list():
        runtime = 0
        while runtime !=2:
                noun = input("Enter a noun! ")
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
list_all_items()
#The story
print("A long time ago in a " + places[0] + " far, far away... the " + adjectives[0] +  " evil coperation " + nouns[0] + " tech developed a " + nouns[1]
+ ". This " + nouns[1] + " forced the users to repeatedly " + verbs[0] + ". This Angered a user of the product named " + names[0]
+ ", this user was skilled in the art of " + verbs[1] + "(ing) this allowed " + names[0] + " to face the evil coperation's head boss, " + names[1]
+ ". The head boss was also profficent in a skill their hobby is " + verbs[2] + "(ing), ")
#Still needs 2 more adj and 1 more place could use coloring or organization.