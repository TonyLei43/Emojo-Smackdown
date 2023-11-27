let currentWeatherData = {};

function fetchWeather() {
    fetch('/get_weather')
        .then(response => response.json())
        .then(data => {
            // Extracting the necessary data from the API response
            currentWeatherData = {
                location: data.name,
                condition: data.weather[0].description,
                temperature: data.main.temp,
                windSpeed: data.wind.speed
            };
            var location = currentWeatherData.location;
            var weatherCondition = currentWeatherData.condition;
            var temperature = currentWeatherData.temperature;
            var windSpeed = currentWeatherData.windSpeed;
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
