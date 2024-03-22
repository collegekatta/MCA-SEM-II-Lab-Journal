<?php
// Starting the session
session_start();

echo "<h3>Session example in php</h3>";

// Technique 1: Setting session variables
$_SESSION['username'] = 'JohnDoe';
$_SESSION['email'] = 'johndoe@example.com';

// Technique 2: Accessing session variables
$username = $_SESSION['username'];
$email = $_SESSION['email'];

// Technique 3: Checking if a session variable is set
if (isset($_SESSION['username'])) {
    echo "Username is set. <br />";
} else {
    echo "Username is not set. <br />";
}

// Technique 4: Removing a session variable
unset($_SESSION['email']);

// Technique 5: Destroying the session
session_destroy();

// Displaying session data
echo "Username: $username<br>";
echo "Email: $email<br>";
echo "<br />";
echo "After destroy <br/>";
echo "Email : " . $_SESSION['email'];
?>
