import numpy as np

#Determines computer move at random in Normal Mode
def decide_computer_move_normal():
    return np.random.choice(['Rock', 'Paper', 'Scissors','Spock','Lizard'])

#Determines
def decide_computer_move_hard(previous_input, transition_matrix, state_dict, total_choices):
    opposite_dict = {'Rock': ['Paper', 'Spock'], 'Paper': ['Scissors', 'Lizard'], 'Scissors': ['Rock', 'Spock'], 
                    'Lizard': ['Rock', 'Scissors'], 'Spock': ['Lizard','Paper']}
    if previous_input is None:
        chosen_state = np.random.choice(np.array(['Rock', 'Paper', 'Scissors','Lizard', 'Spock']))
    else: 
        probabilities = transition_matrix[state_dict[previous_input]]
        chosen_state = np.random.choice(np.array(['Rock', 'Paper', 'Scissors','Lizard', 'Spock']), p=probabilities)
    
    opposite_choices = opposite_dict[chosen_state]
    predicted_value = np.random.choice(opposite_choices)
    return chosen_state, predicted_value
    
def determine_winner(player_choice, computer_choice):
    rules = {'Rock': ['Scissors', 'Lizard'],
             'Paper': ['Rock', 'Spock'],
             'Scissors': ['Paper', 'Lizard'],
             'Lizard': ['Spock', 'Paper'],
             'Spock': ['Rock', 'Scissors']}

    if player_choice == computer_choice:
        return "Tie"
    elif computer_choice in rules[player_choice]:
        return "Player"
    else:
        return "Computer"

def update_transition_matrix(prev_choice, new_choice, total_choices, transition_matrix, state_dict):
    if prev_choice is not None:
        total_choices[prev_choice][state_dict[new_choice]] += 1
        transition_matrix[state_dict[prev_choice]] = total_choices[prev_choice] / np.full(5, sum(total_choices[prev_choice]))

    return transition_matrix
