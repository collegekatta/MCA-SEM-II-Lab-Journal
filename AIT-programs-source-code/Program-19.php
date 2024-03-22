<?php
// Function to read users from file
function readUsersFromFile($filename) {
    $users = [];
    if (file_exists($filename)) {
        $data = file_get_contents($filename);
        $users = json_decode($data, true);
    }
    return $users;
}

// Function to write users to file
function writeUsersToFile($filename, $users) {
    $data = json_encode($users);
    file_put_contents($filename, $data);
}

// File name to store user data
$filename = "users.json";

// Perform CRUD operations based on request
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Create operation
    if ($_POST["action"] == "create") {
        $name = $_POST["name"];
        $email = $_POST["email"];
        $users = readUsersFromFile($filename);
        $users[] = ["name" => $name, "email" => $email];
        writeUsersToFile($filename, $users);
        echo "User created successfully.";
    }
    // Update operation
    elseif ($_POST["action"] == "update") {
        $id = $_POST["id"];
        $name = $_POST["name"];
        $email = $_POST["email"];
        $users = readUsersFromFile($filename);
        $users[$id] = ["name" => $name, "email" => $email];
        writeUsersToFile($filename, $users);
        echo "User updated successfully.";
    }
    // Delete operation
    elseif ($_POST["action"] == "delete") {
        $id = $_POST["id"];
        $users = readUsersFromFile($filename);
        if (isset($users[$id])) {
            unset($users[$id]);
            writeUsersToFile($filename, $users);
            echo "User deleted successfully.";
        } else {
            echo "User not found.";
        }
    }
} elseif ($_SERVER["REQUEST_METHOD"] == "GET") {
    // Read operation
    if ($_GET["action"] == "read") {
        $users = readUsersFromFile($filename);
        echo json_encode($users);
    }
}
?>
