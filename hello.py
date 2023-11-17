from flask import Flask, render_template,jsonify
from flask_socketio import SocketIO
import base64 
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')  # Replace with your actual HTML file

@app.route('/get_weather')
def get_weather():
    api_key = '87178d3eebbf2b5e7a7d6854f7a6efd4'
    api_url = f'https://api.openweathermap.org/data/2.5/weather?lat=34.06&lon=-118.45&units=imperial&appid={api_key}'
    response = requests.get(api_url)
    weather_data = response.json()

    return jsonify(weather_data)



@socketio.on('message')
def handle_frame(data):
    image_data = base64.b64decode(data.split(',')[1])
    #pose = your_ml_model.detect_pose(image_data)  # Process frame for fingerpose
    #socketio.emit('pose', pose)  # Send pose data back to client

@socketio.on('connect')
def test_connect():
    # Emit a test message upon new connection
    test_pose_data = {'pose': 'Test Pose'}
    socketio.emit('pose', test_pose_data)

if __name__ == '__main__':
    socketio.run(app,debug=True)
