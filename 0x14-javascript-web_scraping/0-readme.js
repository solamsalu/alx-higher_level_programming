#!/usr/bin/node

// Import the fs module to access the file system
const fs = require("fs");

// Check if the file path is given as the first argument
if (process.argv.length > 2) {
  // Assign the file path to a variable
  let filePath = process.argv[2];
  // Try to read the file in utf-8 encoding
  fs.readFile(filePath, "utf8", (err, data) => {
    // Check for errors
    if (err) {
      // Print the error object
      console.error(err);
    } else {
      // Print the file content
      console.log(data);
    }
  });
} else {
  // Print a message
  console.log("Please provide a file path as the first argument.");
}
