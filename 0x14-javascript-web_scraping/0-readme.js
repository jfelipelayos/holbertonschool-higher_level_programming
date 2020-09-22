#!/usr/bin/node
const fs = require('fs');
const av = process.argv;
const file = fs.readFileSync(av[2], 'utf8');
console.log(file);
