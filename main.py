import random
import re


def rock_paper_scissors(matches):
    player_wins = 0
    cpu_wins = 0

    for match in range(matches):
        print_match_intro(match, matches)
        player_input = player_choice()
        cpu_input = cpu_hand_chooser()
        player_wins, cpu_wins = face_off(player_input, cpu_input, player_wins, cpu_wins)
        print_scoreboard(cpu_wins, player_wins)

    print_ending_results(cpu_wins, player_wins)


def print_match_intro(match, matches):
    if match == matches - 1:
        print('It\'s time for the last match')
    else:
        print(f'It\'s time for the match number {match + 1}!')


def print_ending_results(cpu_wins, player_wins):
    if player_wins > cpu_wins:
        print('The human has won!')
    if player_wins < cpu_wins:
        print('The CPU has won!')
    if player_wins == cpu_wins:
        print('We got no winners')


def print_scoreboard(cpu_wins, player_wins):
    print(f'----Scoreboard-----')
    print('  Player  |   CPU   ')
    print('----------|---------')
    print(f'     {player_wins}    |    {cpu_wins}')
    print('--------------------')


def face_off(player_input, cpu_input, player_wins, cpu_wins):
    # compare player and cpu hands, in this specific order
    input_combination_list = ['rr', 'rp', 'rs',
                              'pp', 'ps', 'pr',
                              'ss', 'sr', 'sp']
    output_combination_list = [['draw', 0, 0],
                               ['CPU Won', 0, 1],
                               ['Player Won', 1, 0]]
    results_map = dict(zip(input_combination_list, output_combination_list*3))

    print(results_map[player_input + cpu_input][0])
    return player_wins + results_map[player_input + cpu_input][1], \
           cpu_wins + results_map[player_input + cpu_input][2]


def player_choice():
    # uses RegEx to validade player input
    re_pattern = re.compile('[rpsRPS]')

    while True:
        player_input = input('Choose one: [R]ock - [P]aper - [S]cissor\n')
        is_valid_player_input = re_pattern.fullmatch(player_input)
        if not is_valid_player_input:
            print(f'what the heck is {player_input}???')
        else:
            print(f'Player showed: {player_input}')
            break

    return player_input.lower()


def cpu_hand_chooser():
    # just choose a random hand for CPU
    cpu_choice_number = random.randrange(3)
    hand = ['r', 'p', 's']
    print(f'CPU showed: {hand[cpu_choice_number]}')
    return hand[cpu_choice_number]


rock_paper_scissors(3)
