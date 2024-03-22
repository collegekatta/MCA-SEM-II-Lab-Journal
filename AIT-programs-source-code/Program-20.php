<?php
// Check if the email argument is provided
if ($argc < 2) {
    echo "Usage: php send_email.php <recipient_email>\n";
    exit(1);
}

$to = $argv[1];
$subject = 'Test Email';
$message = 'This is a test email sent from the command line.';
$headers = 'From: amar@ourlib.in' . "\r\n" .
    'Reply-To: amar@ourlib.in' . "\r\n" .
    'X-Mailer: PHP/' . phpversion();

echo "Sending email to : $to\n";
echo "...........\n";
echo "\n";

if (mail($to, $subject, $message, $headers)) {
    echo "Email sent successfully to $to\n";
} else {
    echo "Failed to send email\n";
}
