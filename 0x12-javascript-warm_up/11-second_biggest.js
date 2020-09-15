#!/usr/bin/node
const myArgs = process.argv.slice(2);

function secondBigger (array) {
  if (array[0] === undefined || array.length < 2) {
    console.log(0);
  } else {
    let biggerNumber;
    let secondBiggerNumber;

    for (let i = 1; i < array.length; i++) {
      if (i === 1) {
        if (array[0] > array[1]) {
          biggerNumber = array[0];
          secondBiggerNumber = array[1];
        } else {
          biggerNumber = array[1];
          secondBiggerNumber = array[0];
        }
      } else {
        if (biggerNumber < array[i]) {
          secondBiggerNumber = biggerNumber;
          biggerNumber = array[i];
        }
      }
    }
    console.log(secondBiggerNumber);
  }
}
secondBigger(myArgs);
