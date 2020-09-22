#!/usr/bin/node
const request = require('request');
const argv = process.argv;
request(argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response && response.statusCode);
  }
});
