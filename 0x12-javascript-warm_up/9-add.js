#!/usr/bin/node
const myArgs = process.argv;

function add (a, b) {
  let add = 0;

  if (a === undefined || b === undefined) {
    add = NaN;
  } else {
    add = a + b;
  }
  console.log(add);
}

add(parseInt(myArgs[2]), parseInt(myArgs[3]));
