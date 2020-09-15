#!/usr/bin/node
const myArgs = process.argv;
const myMessage = 'X';

if (myArgs[2] === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myArgs[2]; i++) {
    console.log(myMessage.repeat(myArgs[2]));
  }
}
