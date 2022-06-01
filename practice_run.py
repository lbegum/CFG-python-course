import random
import requests


# Chooses a random pokemon from pokeapi
def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'], 'id': pokemon['id'],
        'height': pokemon['height'], 'weight': pokemon['weight'],
    }


def run_game():
    my_score = 0
    op_score = 0

    # This code block allows user to choose the number of rounds and the while loop ensures the round will not be
    # inputted incorrectly
    rounds_string = input('How many rounds would you like to play? Choose a number from 1 - 5: ')
    rounds_list = ['1', '2', '3', '4', '5']

    while rounds_string not in rounds_list:
        print("Incorrect entry - please try again...")
        rounds_string = input('How many rounds would you like to play? Choose a number from 1 - 5: ')

    rounds = int(rounds_string)

    # Game will continue looping until my_score or op_score equal the number of rounds chosen
    while (my_score != rounds) and (op_score != rounds):
        my_pokemon_1 = random_pokemon()
        my_pokemon_2 = random_pokemon()
        my_pokemon_3 = random_pokemon()

        # This while loop ensures that all 3 pokemon choices will be unique
        while (my_pokemon_2['id'] == my_pokemon_1['id']) \
                or (my_pokemon_3['id'] == my_pokemon_2['id']) \
                or (my_pokemon_3['id'] == my_pokemon_1['id']):
            my_pokemon_2 = random_pokemon()
            my_pokemon_3 = random_pokemon()

        # The following code block asks user to select a pokemon via its name and then the while loop ensures the name
        # will not be inputted incorrectly
        my_choice = input(f"You have been given the choice of {my_pokemon_1['name']}, {my_pokemon_2['name']} or "
                          f"{my_pokemon_3['name']}, choose one...: ")

        all_cards = (my_pokemon_1['name'], my_pokemon_2['name'], my_pokemon_3['name'])

        while my_choice not in all_cards:
            print('You have entered the incorrect name, try again')
            my_choice = input(f"You have been given the choice of {my_pokemon_1['name']}, {my_pokemon_2['name']} or "
                              f"{my_pokemon_3['name']}, choose one...: ")

        # Converts my_choice from string name to element name so that it can be referenced again when choosing
        # pokemon stat
        if my_choice == my_pokemon_1['name']:
            my_choice = my_pokemon_1
        elif my_choice == my_pokemon_2['name']:
            my_choice = my_pokemon_2
        else:
            my_choice = my_pokemon_3
        print(f"You have selected {my_choice['name']}")

        # Following code block asks user to choose a stat and while loops ensures spelling is correct
        print(f"Your pokemon has an id of {my_choice['id']}, a weight of {my_choice['weight']}, "
              f"and a height of {my_choice['height']}")
        stat_choice = input('Which stat do you want to use? (id, weight, height): ')
        stat = ('id', 'height', 'weight')

        while stat_choice not in stat:
            print('you have entered incorrect information try again')
            stat_choice = input('Which stat do you want to use? (id, weight, height): ')

        # Following code block assigns a random pokemon to opponent and compares user chosen stat to opponent
        # pokeomon stat. Increases my_score or op_score by 1 depending on the higher stat
        opponent_pokemon = random_pokemon()
        print(f"The opponent chose {opponent_pokemon['name']}")
        my_stat = my_choice[stat_choice]
        opponent_stat = opponent_pokemon[stat_choice]
        if my_stat > opponent_stat:
            print(f"You win as the opponent has a {stat_choice} of {opponent_stat}!")
            my_score += 1
        elif my_stat < opponent_stat:
            print(f"You lose as the opponent has a {stat_choice} of {opponent_stat}!")
            op_score += 1
        else:
            print('Draw!')
        print(f"Current scores are: {my_score} to you, {op_score} to your opponent!")

    # This is outside the first while loop signifying the end of the game
    if my_score == rounds:
        print(f"You win against the computer! Final score {my_score} - {op_score} to you!")
    else:
        print(f"You lost against your opponent! Final score {op_score} - {my_score} to your opponent!")


run_game()
