const video = document.getElementById('player-video');

// Access webcam
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
        video.play();
    });

// Set up WebSocket connection
const socket = new WebSocket('ws://127.0.0.1:5000');

video.onloadedmetadata = () => {
    setInterval(() => {
        const frame = captureFrame();
        socket.send(frame);
    }, 100); // Adjust as needed
};

function captureFrame() {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    return canvas.toDataURL('image/jpeg');
}



socket.onmessage = function(event) {
    const poseData = JSON.parse(event.data);
    console.log(poseData);
};
