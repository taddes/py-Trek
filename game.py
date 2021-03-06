from random import randint

"""
    A Star Trek inspired game to pit your Starfleet officers against the enemies of the Federation!
"""

player = {'name': 'Captain Kirk', 'attack': 10, 'heal': 16, 'health': 100}
enemy = {'name': 'Captain Kor', 'attack_min': 10, 'attack_max': 20, 'health': 100}

game_running = True

game_results = []

def calculate_enemy_attack():
    return  randint(enemy['attack_min'], enemy['attack_max'])


while game_running == True:
    counter = 0
    new_round = True
    player = {'name': 'Captain Kirk', 'attack': 10, 'heal': 16, 'health': 100}
    enemy = {'name': 'Captain Kor', 'attack_min': 10, 'attack_max': 20, 'health': 100}

    print('---' * 7)
    print('Enter Player Name: ')
    player['name'] = input()

    print(player['name'] + ' has ' + str(player['health']) + ' health.')
    print(enemy['name'] + ' has ' + str(enemy['health']) + ' health.')

    while new_round == True:
        counter = counter + 1
        player_won = False
        enemy_won = False

        print('---' * 7)
        print('Select an action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')
        print('4) Show Results')
        player_choice = input()

        if player_choice == '1':
            enemy['health'] = enemy['health'] - player['attack']
            if enemy['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - calculate_enemy_attack()
                if player['health'] <= 0:
                    enemy_won = True

        elif player_choice == '2':
            player['health'] += player['heal'] #make sure works later
            
            player['helath'] = player['health'] - calculate_enemy_attack()
            if player['health'] <= 0:
                enemy_won = True
            
        elif player_choice == '3':
            new_round = False
            game_running = False

        elif player_choice == '4':
            print('Game results from rounds')
            for game in game_results:
                print(game)

        else:
            print('Invalid input')
        
        if player_won == False and enemy_won == False:
            print(player['name'] + ' has ' + str(player['health']) + ' health left.')
            print(enemy['name'] + ' has ' + str(enemy['health']) + ' health left.')

        elif player_won:
            print(f"{player['name']} has defeated {enemy['name']}!")
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
            game_results.append(round_result)

            new_round = False

        elif enemy_won:
            print(f"{enemy['name']} has defeated {player['name']}!")
            round_result = {'name': enemy['name'], 'health': enemy['health'], 'rounds': counter}
            game_results.append(round_result)
            new_round = False

        if player_won == True or enemy_won == True:
            new_round = False


def calculate_monster_attack():
    return  randint(enemy['attack_min'], enemy['attack_max'])