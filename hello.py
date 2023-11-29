from flask import Flask, render_template,jsonify,request
from flask_socketio import SocketIO
import base64 
import requests
import mediapipe as mp
from mediapipe.tasks import python as mp_tasks
from mediapipe.tasks.python import vision
import cv2
import numpy as np
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')  


# Set up the GestureRecognizer
model_path = 'model/gesture_recognizer.task'  # Update with the actual path
base_options = mp_tasks.BaseOptions(model_asset_path=model_path)
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)

@app.route('/process_gesture', methods=['POST'])
def process_gesture():
    data = request.json
    weather_data = data.get('weather', {})
    image_b64 = data['image'].split(',')[1]
    image_bytes = base64.b64decode(image_b64)
    image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

    # Convert the color space from BGR to RGB as MediaPipe uses RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Create an mp.Image object
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)

    # Process the image with the recognizer
    results = recognizer.recognize(mp_image)
    mode = data.get('mode', {})
    if results.gestures:
        top_gesture = results.gestures[0][0]
        player_gesture = top_gesture.category_name 
        # Implement game logic considering the weather
        

        # Determine the winner
        if mode:
            computer_gesture = decide_computer_move_hard(weather_data)
            winner = determine_winner_hard(player_gesture, computer_gesture,weather_data) # Assuming the first gesture is the most confident
        else:
            computer_gesture= decide_computer_move_normal()
            winner = determine_winner_normal(player_gesture, computer_gesture)
    else:
        return jsonify(message='No gesture detected')


    # Implement the game logic here
    # Randomly select a move for the computer, compare it, and determine the winner

    # Send back the result
    #return jsonify(message=f"Player: {player_gesture}")
    return jsonify(winner = winner, message=f"Player: {player_gesture}, Computer: {computer_gesture}. Winner: {winner}")
def decide_computer_move_normal():
    return np.random.choice(['Rock', 'Paper', 'Scissors'])

def decide_computer_move_hard(weather):
    # Example logic based on weather conditions
    if weather.get('condition') in ['sunny','clear sky']:
        return 'Rock'
    elif weather.get('condition') == 'windy':
        return 'Scissors'
    elif weather.get('condition') in ['rainy', 'cloudy']:
        return 'Paper'
    else:
        # Random move if weather data is not available or doesn't match any condition
        return np.random.choice(['Rock', 'Paper', 'Scissors'])
    
def determine_winner_normal(player_move, computer_move):
    if player_move == "Open_Palm":
        player_move= "Paper"
    elif player_move == "Victory":
        player_move= "Scissors"
    elif player_move == "Closed_Fist":
        player_move= "Rock"
    else:
        player_move=None
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


@app.route('/get_weather')
def get_weather():
    api_key = '87178d3eebbf2b5e7a7d6854f7a6efd4'
    api_url = f'https://api.openweathermap.org/data/2.5/weather?lat=34.06&lon=-118.45&units=imperial&appid={api_key}'
    response = requests.get(api_url)
    weather_data = response.json()

    return jsonify(weather_data)


if __name__ == '__main__':
    Flask.run(app,debug=True)
