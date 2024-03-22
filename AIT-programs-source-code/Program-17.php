<?php
$error = "";
$name = $email = $age = "";
$showDetails = false;
if (isset($_POST)) {
    if (empty($_POST["name"])) {$error .= "Name is required.<br>";
    } else {
        $name = test_input($_POST["name"]);
        if (!preg_match("/^[a-zA-Z ]*$/", $name)) {$error .= "Only letters and white space allowed in name.<br>";}
    }
    if (empty($_POST["email"])) {
        $error .= "Email is required.<br>";
    } else {
        $email = test_input($_POST["email"]);
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $error .= "Invalid email format.<br>";
        }
    }
    if (empty($_POST["age"])) {$error .= "Age is required.<br>";} else {
        $age = test_input($_POST["age"]);
        if (!is_numeric($age) || $age < 18 || $age > 100) {$error .= "Age must be a number between 18 and 100.<br>";}}}
// Function to sanitize input data
function test_input($data) {$data = trim($data);$data = stripslashes($data);$data = htmlspecialchars($data);return $data;}
?>

<!DOCTYPE html><html><head><title>Personal Form</title></head><body>

<?php
if($_POST["showDetails"] == "show"){
    echo "<h3>Entered Details : </h3>";
    echo "Name: " . $_POST["name"] . "<br>";echo "Email: " . $_POST["email"] . "<br>";echo "Age: " . $_POST["age"] . "<br>";
} ?>
    <h2>Personal Form</h2>
    <form method="post" action="">
    <input type="hidden" name="showDetails" value="show">
        Name: <input type="text" name="name" value="<?php echo $name; ?>"><br>
        Email: <input type="text" name="email" value="<?php echo $email; ?>"><br>
        Age: <input type="text" name="age" value="<?php echo $age; ?>"><br>
        <input type="submit" name="submit" value="Submit">
    </form>
    <div style="color: red;"><?php echo $error; ?></div>
</body>
</html>