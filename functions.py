import numpy as np

#Determines computer move at random in Normal Mode
def decide_computer_move_normal():
    return np.random.choice(['Rock', 'Paper', 'Scissors','Spock','Lizard'])

#Determines
def decide_computer_move_hard():
    #implement hard mode
    pass
    
def determine_winner_normal(player_move, computer_move):
    if player_move == "Open_Palm":
        player_move= "Paper"
    elif player_move == "Victory":
        player_move= "Scissors"
    elif player_move == "Closed_Fist":
        player_move= "Rock"

    outcomes = {
        ('Rock', 'Scissors'): 'Player',
        ('Scissors', 'Rock'): 'Computer',
        ('Scissors', 'Paper'): 'Player',
        ('Paper', 'Scissors'): 'Computer',
        ('Paper', 'Rock'): 'Player',
        ('Rock', 'Paper'): 'Computer'
    }

    # Check for tie
    if player_move == computer_move:
        return 'Tie'
    winner = outcomes.get((player_move, computer_move))
    return winner 


def determine_winner_hard(player_move, computer_move, weather):
    """
    Determine the winner of a Rock-Paper-Scissors game with an unpredictable twist based on weather.

    :param player_move: Player's move ('Rock', 'Paper', 'Scissors').
    :param computer_move: Computer's move ('Rock', 'Paper', 'Scissors').
    :param weather: Dictionary containing weather data.
    :return: String indicating the winner ('Player', 'Computer', 'Tie').
    """

    # Basic Rock-Paper-Scissors logic
    if player_move == "Open_Palm":
        player_move= "Paper"
    elif player_move == "Victory":
        player_move= "Scissor"
    elif player_move == "Closed_Fist":
        player_move= "Rock"
    else:
        player_move=None

    basic_outcomes = {
        ('Rock', 'Scissors'): 'Player',
        ('Scissors', 'Rock'): 'Computer',
        ('Scissors', 'Paper'): 'Player',
        ('Paper', 'Scissors'): 'Computer',
        ('Paper', 'Rock'): 'Player',
        ('Rock', 'Paper'): 'Computer'
    }

    # Check for a basic outcome
    if player_move == computer_move:
        return 'Tie'
    basic_winner = basic_outcomes.get((player_move, computer_move))

    # Incorporate weather into the decision
    temperature = weather.get('temperature', 20)  # Default to 20 if no data
    wind_speed = weather.get('windSpeed', 5)  # Default to 5 if no data
    condition = weather.get('condition', 'clear').lower()  # Default to 'clear' if no data

    # Complex logic based on weather
    if condition in ['rainy', 'cloudy'] and random.random() < 0.3:
        # In rainy or cloudy weather, there's a 30% chance the outcome is reversed
        return 'Player' if basic_winner == 'Computer' else 'Computer'
    elif temperature > 30 and wind_speed > 10 and player_move == 'Paper':
        # Hot and windy conditions make 'Paper' less likely to win
        return 'Computer'
    elif condition == 'sunny' and computer_move == 'Scissors':
        # On sunny days, 'Scissors' are slightly more likely to win
        return 'Computer' if random.random() < 0.6 else basic_winner
    else:
        # In all other cases, use the basic game logic
        return 'Player'
