
const readline = require('readline-sync');

// Function to perform addition
function add(a, b) {
    return a + b;
}

// Function to perform subtraction
function subtract(a, b) {
    return a - b;
}

// Function to perform multiplication
function multiply(a, b) {
    return a * b;
}

// Function to perform division
function divide(a, b) {
    if (b === 0) {
        return "Error! Division by zero.";
    }
    return a / b;
}

// Main function
function main() {
    console.log("Welcome to Node.js Calculator!");

    // Menu
    console.log("1. Addition");
    console.log("2. Subtraction");
    console.log("3. Multiplication");
    console.log("4. Division");

    // Ask user for operation choice
    const choice = parseInt(readline.question("Enter your choice: "));

    let num1 = parseFloat(readline.question("Enter first number: "));
    let num2 = parseFloat(readline.question("Enter second number: "));

    let result;

    // Perform operation based on user choice
    switch (choice) {
        case 1:
            result = add(num1, num2);
            break;
        case 2:
            result = subtract(num1, num2);
            break;
        case 3:
            result = multiply(num1, num2);
            break;
        case 4:
            result = divide(num1, num2);
            break;
        default:
            console.log("Invalid choice.");
            return;
    }

    // Display the result
    console.log("Result: ", result);
}

// Call the main function to start the program
main();
