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
#Funtion lists items to test its working
def list_all_items():
    for list_item in nouns,adjectives,verbs:
        print(list_item)

add_noun_list()
add_adj_list()
add_verb_list()

list_all_items()
