#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const occurrence of list) {
    if (occurrence === searchElement) {
      count++;
    }
  }
  return (count);
};
