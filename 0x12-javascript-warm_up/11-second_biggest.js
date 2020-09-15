#!/usr/bin/node
const myArgs = process.argv.slice(2);

function compareNum (a, b) {
  return a - b;
}

const size = myArgs.length;
if (size === 0 || size === 1) {
  console.log(0);
} else {
  console.log(myArgs.sort(compareNum)[size - 2]);
}
