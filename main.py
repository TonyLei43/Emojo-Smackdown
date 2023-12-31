from flask import Flask, render_template,jsonify,request
import base64 
import requests
import mediapipe as mp
from mediapipe.tasks import python as mp_tasks
from mediapipe.tasks.python import vision
import cv2
import numpy as np
import random
from functions import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  

# Set up the GestureRecognizer
model_path = 'model/spockitydoo.task'  
base_options = mp_tasks.BaseOptions(model_asset_path=model_path)
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)



transition_matrix = np.full((5, 5), 1/5)
state_dict = {'Rock': 0, 'Paper': 1, 'Scissors': 2, 'Lizard': 3, 'Spock': 4}
total_choices = {'Rock': [0, 0, 0, 0, 0], 'Paper': [0, 0, 0, 0, 0], 'Scissors': [0, 0, 0, 0, 0],
                    'Lizard': [0, 0, 0, 0, 0], 'Spock': [0, 0, 0, 0, 0]}
previous_move = None


@app.route('/process_gesture', methods=['POST'])
def process_gesture():
    data = request.json
    image_b64 = data['image'].split(',')[1]
    image_bytes = base64.b64decode(image_b64)
    image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

    # Convert the color space from BGR to RGB as MediaPipe uses RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Create an mp.Image object
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)

    # Process the image with the recognizer
    results = recognizer.recognize(mp_image)

    # Check if Normal or Hard mode (Hard: True, Normal: False)
    mode = data.get('mode', {})

    global transition_matrix
    global state_dict
    global total_choices
    global previous_move

    #If the model detects a gesture 
    if results.gestures:
        top_gesture = results.gestures[0][0] #Takes the top one with highest probability
        player_gesture = top_gesture.category_name #Gesture of the Player
        if player_gesture=='':
            return jsonify(message='Try Again')
        # Determine the winner
        if mode:
            computer_gesture = decide_computer_move_hard(previous_move, transition_matrix, state_dict, total_choices)
            winner = determine_winner(player_gesture, computer_gesture)
        else:
            computer_gesture= decide_computer_move_normal()
            winner = determine_winner(player_gesture, computer_gesture)
            
        # Updating transition matrix and previous move
        transition_matrix = update_transition_matrix(previous_move, player_gesture, total_choices, transition_matrix, state_dict)
        print(transition_matrix)
        previous_move = player_gesture
    else:
        return jsonify(message='No hand gesture detected')

    return jsonify(winner = winner, message=f"Player: {player_gesture}, Computer: {computer_gesture}. Winner: {winner}")



@app.route('/get_weather')
def get_weather():
    api_key = '87178d3eebbf2b5e7a7d6854f7a6efd4'
    api_url = f'https://api.openweathermap.org/data/2.5/weather?lat=34.06&lon=-118.45&units=imperial&appid={api_key}'
    response = requests.get(api_url)
    weather_data = response.json()

    return jsonify(weather_data)


if __name__ == '__main__':
    Flask.run(app,debug=True)