#!/usr/bin/node

const arg = parseInt(process.argv[2], 10);

function factorial (num) {
  if (num === 0 || num === 1 || isNaN(num)) { return (1); }
  return (num * factorial(num - 1));
}
console.log(factorial(arg));
