#!/usr/bin/node

let x = parseInt(process.argv[2], 10);
let y = parseInt(process.argv[3], 10);

function add(a, b) {
    return a + b;
}
console.log(add(x, y));
