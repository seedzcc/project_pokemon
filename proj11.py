"""
    SOURCE HEADER GOES HERE!
"""
import csv
from random import randint
from random import seed
from copy import deepcopy

from pokemon import Pokemon
from pokemon import Move

seed(1)  # Set the seed so that the same events always happen

# DO NOT CHANGE THIS!!!
# =============================================================================
element_id_list = [None, "normal", "fighting", "flying", "poison", "ground", "rock",
                   "bug", "ghost", "steel", "fire", "water", "grass", "electric",
                   "psychic", "ice", "dragon", "dark", "fairy"]


# Element list to work specifically with the moves.csv file.
#   The element column from the moves.csv files gives the elements as integers.
#   This list returns the actual element when given an index
# =============================================================================

def read_file_moves(fp):
    '''
        WRITE DOCSTRING HERE!!!
    '''
    moves = []
    #while True:
    file_name = input("Player {}, choose a pokemon by name or index: ")
    try:
        fp = open(file_name, "r")
        read = csv.reader(fp)
        next(read, None)  # skip the header
        for line in read:  # get the data out
            move_name = line[1]
            generation_id = line[2]
            element_id = line[3]
            attack_type_id = line[9]
            power = line[4]
            accuracy = line[6]
            if generation_id != 1 or attack_type_id == 1 or power == '' or accuracy == '':
                continue
            else:
                move = Move(move_name, element_id_list[element_id], int(power), int(accuracy), attack_type_id)
                moves.append(move)
    except IOError:
        print("read found error {}", file_name)
    return moves

def read_file_pokemon(fp):
    '''
        WRITE DOCSTRING HERE!!!
    '''
    dict= {}
    pokemon_list=[]
    fp=open("pokemon.csv","r")
    read = csv.reader(fp)
    next(read, None)  # skip the header
    for line in read:  # get the data out
        generation=line[11]
        id=line[0]
        element1=line[2].lower()
        element2=line[3].lower()
        hp=int(line[5])
        patt=int(line[6])
        pdef=int(line[7])
        satt=int(line[8])
        sdef=int(line[9])
        name=line[1].lower()
        if generation!=1:
            if dict.get(id) is None:
                pokemon = Pokemon(name, element1, element2, None, hp, patt, pdef, satt, sdef)
                dict[id]=1
                pokemon_list.append(pokemon)


    return pokemon_list


def choose_pokemon(choice, pokemon_list):
    '''
        WRITE DOCSTRING HERE!!!
    '''
    pkm =None
    if type(choice).__name__== 'int':
        if choice>len(pokemon_list):
            return None
        pkm=deepcopy(pokemon_list[choice-1])
    if type(choice).__name__== 'str':
        for i,item in enumerate(pokemon_list):
            if choice==item[1]:
                pkm=deepcopy(item)
    return pkm

# fixme
def add_moves(pokemon, moves_list):
    '''
        WRITE DOCSTRING HERE!!!
    '''
    num=randint(0,len(moves_list)-1)
    _move=moves_list[num]
    pokemon.add_move(_move)

    element1=pokemon.get_element1()
    element2=pokemon.get_element2()

    index=0 # num of add to moves_list
    for item in moves_list:
        if item.element== element1 or item.element ==element2 and ~_move.__eq__(item):
            pokemon.add_move(item)
    return pokemon.get_number_moves()==4


def turn(player_num, player_pokemon, opponent_pokemon):
    '''
        WRITE DOCSTRING HERE!!!
    '''
    pass


def main():
    # read file
    pokemon = Pokemon()
    # read moves file
    moves = read_file_moves(None)
    add_moves(pokemon, moves)
    # read pokemon file
    read_file_pokemon(None)

    usr_inp = input("Would you like to have a pokemon battle?").lower()
    while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':
        usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q:").lower()

    if usr_inp != 'y':
        print("Well that's a shame, goodbye")
        return

    # else:



if __name__ == "__main__":
    main()

"Would you like to have a pokemon battle? "
"Invalid option! Please enter a valid choice: Y/y, N/n or Q/q: "

"pokemon{}:\n"
"Insufficient moves; choose a different pokemon."
"Invalid option, choose a pokemon by name or index: "
"Select an attack between {} and {}: "
"Invalid input"
"Battle over, would you like to have another? "
"Invalid option! Please enter a valid choice: "
"{} {} {} {} {} {}\n"
"Number out of index range"
"selected move:"
"{} hp before:{}"
"{} hp after:{}"
"Player {}'s pokemon fainted, Player {} has won the pokemon battle!"
"Player {}'s turn"
"Player {} quits, Player {} has won the pokemon battle!"
"P{} hp after:"
"Show options: 'show ele', 'show pow', 'show acc'"
"Select an attack between 1 and {} or show option or 'q': "
"Well that's a shame, goodbye"
