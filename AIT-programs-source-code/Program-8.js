// Function to convert single digit input to two digits
const formatDigit = (input) => (input > 9 ? input : `0${input}`);

// Function to convert 24-hour time to 12-hour time
const convertTo12HourFormat = (hour) => {
    if (hour > 12) {
        return hour - 12;
    }
    return hour;
};

// Get current date and time
const currentDate = new Date();

// Format date and time components
const formattedDate = {
    dd: formatDigit(currentDate.getDate()),
    mm: formatDigit(currentDate.getMonth() + 1),
    yyyy: currentDate.getFullYear(),
    HH: formatDigit(currentDate.getHours()),
    hh: formatDigit(convertTo12HourFormat(currentDate.getHours())),
    MM: formatDigit(currentDate.getMinutes()),
    SS: formatDigit(currentDate.getSeconds()),
};

// Function to display time in 24-hour format
const displayTimeIn24HourFormat = ({ dd, mm, yyyy, HH, MM, SS }) => {
    return `${mm}/${dd}/${yyyy} ${HH}:${MM}:${SS}`;
};

// Function to display time in 12-hour format
const displayTimeIn12HourFormat = ({ dd, mm, yyyy, hh, MM, SS }) => {
    return `${mm}/${dd}/${yyyy} ${hh}:${MM}:${SS}`;
};

// Display time in 24-hour format
console.log("Display time in 24-hour format : " + displayTimeIn24HourFormat(formattedDate));
// Display time in 12-hour format
console.log("Display time in 12-hour format : " + displayTimeIn12HourFormat(formattedDate));
