#!/usr/bin/node
const myArgs = process.argv;
const myMessage = 'C is fun';

if (myArgs[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myArgs[2]; i++) {
    console.log(myMessage);
  }
}
