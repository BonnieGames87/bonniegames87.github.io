document.querySelector('.login-container').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from being submitted

    var uname = document.querySelector('input[name="uname"]').value;
    var psw = document.querySelector('input[name="psw"]').value;

    console.log('Username: ' + uname);
    console.log('Password: ' + psw);

    // You can add your own logic here to handle the login
});
