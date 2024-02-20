#!/usr/bin/node
// Writes a string to a file
const fs = require('fs');
const content = process.argv[3];
const filepath = process.argv[2];

fs.writeFile(filepath, content, 'utf-8', err => {
  if (err) {
    console.error(err);
  }
});
