#!/usr/bin/node
const myArgs = process.argv;

function factorial (n) {
  let total = 1;
  for (let i = 1; i <= n; i++) {
    total = total * i;
  }
  console.log(total);
}
factorial(parseInt(myArgs[2]));
