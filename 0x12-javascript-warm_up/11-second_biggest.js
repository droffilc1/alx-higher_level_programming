#!/usr/bin/node

const _array = process.argv.slice(2);

function secondToMax (_array) {
  if (_array.length < 2) {
    return (0);
  } else {
    _array.sort((x, y) => x - y);
    _array.pop();
    return (_array.pop());
  }
}
console.log(secondToMax(_array));
