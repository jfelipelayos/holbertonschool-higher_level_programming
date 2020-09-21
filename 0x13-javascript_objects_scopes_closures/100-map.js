#!/usr/bin/node
const arr = require('./100-data').list;

const newArr = arr.map((value, index) => {
  return value * index;
});
console.log(arr);
console.log(newArr);
