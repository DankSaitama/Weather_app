document.addEventListener("DOMContentLoaded", function () {
    const bodyElement = document.body;
    const weatherConditionInput = document.getElementById("weather-condition");

    // Function to update the body class based on weather condition
    function updateBackground() {
        const weatherCondition = weatherConditionInput.value;
        bodyElement.className = `weather-${weatherCondition.toLowerCase()}`;
    }

    // Initial background update
    updateBackground();

    // You can also call updateBackground() whenever the weather condition changes.
    // Example: In your AJAX success callback when fetching weather data.
});
