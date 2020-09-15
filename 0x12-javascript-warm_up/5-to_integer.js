#!/usr/bin/node
const myArgs = process.argv;

myArgs[2] = parseInt(myArgs[2]);
if (isNaN(myArgs[2])) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myArgs[2]}`);
}
