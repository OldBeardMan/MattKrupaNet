document.getElementById('subscribe-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevents the default form submission

    // You can simulate a successful subscription here
    // For demonstration purposes, I'll show the message after a delay of 2 seconds
    setTimeout(function() {
        document.getElementById('subscription-message').innerText = "You have subscribed to the newsletter!";
    }, 2000); // 2000 milliseconds (2 seconds) delay
});
