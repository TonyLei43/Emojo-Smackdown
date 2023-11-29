const videoElement = document.getElementById('player-video');
const captureButton = document.getElementById('capture-btn');
const messageElement = document.getElementById('message'); 
let playerScore = 0;
let computerScore = 0;
let isHardMode = false;

// Initialize webcam
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        videoElement.srcObject = stream;
        videoElement.play();
    });


document.getElementById('capture-btn').addEventListener('click', async function() {
    this.disabled = true;
    const canvas = document.createElement('canvas');
    canvas.width = videoElement.videoWidth;
    canvas.height = videoElement.videoHeight;
    const context = canvas.getContext('2d');
    context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
    const dataURL = canvas.toDataURL('image/jpeg');

    // Sending the image to the Flask server
    const response = await fetch('/process_gesture', {
        method: 'POST',
        body: JSON.stringify({ image: dataURL , weather: currentWeatherData,mode:isHardMode}),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const result = await response.json();
    
    updateScores(result.winner)
    // Update the frontend based on the response
    // e.g., display the game result
    messageElement.innerText = result.message; // assuming result contains a message
    setTimeout(function() {
        messageElement.innerText = '';
    }, 3000);
    setTimeout(() => {
        this.disabled = false;
    }, 3000);
});

function updateScores(winner) {
    // Increment the score based on the winner
    if (winner === 'Player') {
        playerScore++;
    } else if (winner === 'Computer') {
        computerScore++;
    }
    // No score change for a tie

    // Update the HTML elements with the new scores
    document.getElementById('score1').innerText = playerScore;
    document.getElementById('score2').innerText = computerScore;
}

document.addEventListener('DOMContentLoaded', (event) => {

    // Get the button element
    const modeToggleButton = document.getElementById('mode-toggle');

    // Add a click event listener to the button
    modeToggleButton.addEventListener('click', function() {
        // Toggle the mode
        isHardMode = !isHardMode;

        // Update the button text based on the current mode
        this.textContent = isHardMode ? 'Hard Mode' : 'Normal Mode';

        // Additional logic to change the game mode can be added here
    });
});


document.addEventListener('DOMContentLoaded', (event) => {
    const audio = document.getElementById('background-music');
    const audioControlBtn = document.getElementById('audio-control-btn');

    audioControlBtn.addEventListener('click', function() {
        if (audio.paused) {
            audio.play();
            this.textContent = '🔈'; // Change button text to 'Pause Music'
        } else {
            audio.pause();
            this.textContent = '🔇'; // Change button text to 'Play Music'
        }
    });
});
