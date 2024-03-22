// Importing the built-in 'url' module
const url = require('url');

// Sample query string
const queryString = 'https://www.example.com/search?q=nodejs&lang=en';

// Parsing the query string using the 'url' module
const parsedUrl = url.parse(queryString, true);

// Extracting the readable parts from the parsed query string
const protocol = parsedUrl.protocol;
const hostname = parsedUrl.hostname;
const pathname = parsedUrl.pathname;
const queryParameters = parsedUrl.query;

// Displaying the readable parts
console.log('Protocol:', protocol);
console.log('Hostname:', hostname);
console.log('Pathname:', pathname);
console.log('Query Parameters:');
for (const [key, value] of Object.entries(queryParameters)) {
    console.log(`\t${key}: ${value}`);
}
