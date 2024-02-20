#!/usr/bin/node
// Display the status code of a GET request
const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) { console.error('error:', error); } // Print the error if one occurred
  console.log('code:', response && response.statusCode); // Print the response status code if a response was received
});
