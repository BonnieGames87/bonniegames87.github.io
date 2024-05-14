<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Class Timer</title>
  <style>
    #timer-container {
      text-align: center;
      margin-top: 50px;
      font-family: Arial, sans-serif;
    }
    #timer {
      font-size: 24px;
      display: inline-block;
      padding: 10px;
      border-radius: 10px;
    }
  </style>
</head>
<body>
  <div id="timer-container">
    <div id="timer">Class Timer</div>
  </div>
  <div id="speed">
    <label for="speed">Select speed:</label>
    <select id="speedSelector">
      <option value="1x">1x</option>
      <option value="20x">20x</option>
      <option value="25x" selected>25x</option>
    </select>
  </div>

  <script>
    // Set initial time durations
    let durations = [600, 1500, 600, 300];
    let colors = ['red', 'green', 'red', 'yellow'];
    let currentDurationIndex = 0;
    let timeLeft = durations[currentDurationIndex];

    // Get the selected speed
    let speedSelector = document.getElementById('speedSelector');
    let selectedSpeed = speedSelector.value;

    // Update the timer every second based on speed
    let timerInterval = setInterval(updateTimer, getSpeedInterval(selectedSpeed));

    // Update the timer based on the selected speed
    function getSpeedInterval(speed) {
      switch (speed) {
        case '1x':
          return 1000; // Update every 1 second
        case '20x':
          return 50; // Update every 0.05 seconds
        case '25x':
          return 40; // Update every 0.04 seconds
        default:
          return 1000; // Default to 1x speed
      }
    }

    // Listen for speed changes
    speedSelector.addEventListener('change', function() {
      // Stop the current interval
      clearInterval(timerInterval);
      // Get the selected speed
      selectedSpeed = speedSelector.value;
      // Start a new interval with the selected speed
      timerInterval = setInterval(updateTimer, getSpeedInterval(selectedSpeed));
    });

    function updateTimer() {
      // Calculate minutes and seconds
      let minutes = Math.floor(timeLeft / 60);
      let seconds = timeLeft % 60;

      // Add leading zero if seconds is less than 10
      seconds = seconds < 10 ? '0' + seconds : seconds;

      // Update the timer display
      let timer = document.getElementById('timer');
      timer.innerText = `Time left: ${minutes}:${seconds}`;

      // Set background color based on current duration
      timer.style.backgroundColor = colors[currentDurationIndex];

      // Decrement time left    
      timeLeft--;

      // Check if the current duration is finished
      if (timeLeft < 0) {
        // Move to the next duration
        currentDurationIndex = (currentDurationIndex + 1) % durations.length;

        // Set time left for the next duration
        timeLeft = durations[currentDurationIndex];
      }
    }
  </script>
</body>
</html>
