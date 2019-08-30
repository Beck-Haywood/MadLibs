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
nouns = list()
verbs = list()
places = list()
#Function asks for nouns and puts them in a list
def add_noun_list():
    runtime = 0
    while runtime !=3:
        adj = input("Enter a noun! ")
        nouns.append(adj)
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
        adj = input("Enter a verb! ")
        verbs.append(adj)
        runtime += 1
#Function asks for places and puts them in a list
def add_place_list():
    runtime = 0
    while runtime !=3:
        adj = input("Enter a place! ")
        places.append(adj)
        runtime += 1
#Funtion lists items to test its working
def list_all_items():
    for list_item in nouns,adjectives,verbs:
        print(list_item)

add_noun_list()
add_adj_list()
add_verb_list()
add_place_list()

list_all_items()

print("A long time ago in a " + places[0] + " far, far away... the " + adjectives[0] +  " evil coperation " + nouns[0] + " tech developed a " + nouns[1]
+ ". This " + nouns[1] + " forced the users to repeatedly " + verbs[0] + ". This Angered a user of the product named " + nouns[2]
+ ", this user was skilled in the art of " + verbs[1] + "(ing) this allowed " + nouns[2] + " to face")