#!/usr/bin/node
const av = process.argv;
const fileSyncro = require('fs');
const file1 = fileSyncro.readFileSync(av[2], 'utf8');
const file2 = fileSyncro.readFileSync(av[3], 'utf8');
fileSyncro.writeFileSync(av[4], file1 + file2);
