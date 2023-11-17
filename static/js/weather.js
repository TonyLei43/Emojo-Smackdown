
function fetchWeather() {
    fetch('/get_weather')
        .then(response => response.json())
        .then(data => {
            // Extracting the necessary data from the API response
            var location = data.name; // Location name
            var weatherCondition = data.weather[0].description; // Weather condition description
            var temperature = data.main.temp; // Temperature
            var windSpeed = data.wind.speed; // Wind speed

            // Update the weather block with the information
            document.getElementById('weather-block').innerHTML = `
            📍 <strong>Location:</strong> ${location}<br>
               🌤️ <strong>Weather:</strong> ${weatherCondition}<br>
                🌡️<strong>Temperature:</strong> ${temperature.toFixed(2)} F<br>
               💨 <strong>Wind Speed:</strong> ${windSpeed} mph
            `;
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
            document.getElementById('weather-block').innerHTML = 
                'Weather data is currently unavailable.';
        });
}

fetchWeather(); // Fetch weather when the page loads
setInterval(fetchWeather, 3600000); // Update every hour
