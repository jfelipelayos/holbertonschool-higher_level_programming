#!/usr/bin/node
const data = require('./101-data').dict;
const dict = {};
for (const key in data) {
  const i = data[key];
  if (dict[i] === undefined) {
    dict[i] = [];
  }
  dict[i].push(key);
}
console.log(dict);
