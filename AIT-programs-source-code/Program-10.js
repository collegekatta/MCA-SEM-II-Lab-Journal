
const readline = require('readline-sync');

// Function to convert string to lowercase
function convertToLowercase(str) {
    return str.toLowerCase();
}

// Function to convert string to uppercase
function convertToUppercase(str) {
    return str.toUpperCase();
}

// Main function
function main() {
    console.log("Welcome to String Case Converter!");

    // Prompt user for input
    const inputString = readline.question("Enter a string: ");

    // Ask user for conversion option
    const option = readline.question("Convert to lowercase (l) or uppercase (u)? ");

    let result;

    // Perform conversion based on user input
    switch (option.toLowerCase()) {
        case 'l': result = convertToLowercase(inputString);break;
        case 'u': result = convertToUppercase(inputString);break;
        default:
            console.log("Invalid option. Please choose 'l' for lowercase or 'u' for uppercase.");
            return;
    }

    // Display the converted string
    console.log(`Converted string: ${result}`);
}

// Call the main function to start the program
main();

