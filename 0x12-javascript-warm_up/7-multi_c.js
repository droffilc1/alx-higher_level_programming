#!/usr/bin/node

const x = parseInt(process.argv[2], 10);
let count = 0;
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (;x > count; count++) {
    console.log('C is fun');
  }
}
