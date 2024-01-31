function updateTime() {
    let date = new Date();
    let hours = date.getHours();
    let minutes = date.getMinutes();
    let seconds = date.getSeconds();

    // Pad single digit minutes and seconds with a leading zero
    minutes = minutes < 10 ? '0' + minutes : minutes;
    seconds = seconds < 10 ? '0' + seconds : seconds;

    let time = hours + ':' + minutes + ':' + seconds;

    document.getElementById('clock').textContent = time;

    setTimeout(updateTime, 100); // Update the time every second
}

window.onload = updateTime; // Call updateTime when the page loads
