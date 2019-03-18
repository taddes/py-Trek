"""
    A Star Trek inspired game to pit your Starfleet officers against the enemies of the Federation!
"""

player = {'name': 'Captain Kirk', 'attack': 10, 'heal': 16, 'health': 100}

enemy = {'name': 'Captain Kor', 'attack': 12, 'health': 100}

game_running = True

while game_running == True:
    print('Select an action')
    print('1) Attack')
    print('2) Heal')
    player_choice = input()

    if player_choice == '1':
        enemy['health'] = enemy['health'] - player['attack']
        if enemy['health'] <= 0:
            player_won = True
        else:
            player['health'] = player['health'] - enemy['attack']
            if player['health'] <= 0:
                enemy_won = True

        print(enemy['health'])
        print(player['health'])

    elif player_choice == '2':
        print('Heal')
    else:
        print('Invalid input')

    if player_won == True or enemy_won == True:
        game_running = False