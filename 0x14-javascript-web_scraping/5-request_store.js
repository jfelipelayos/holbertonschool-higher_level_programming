#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const argv = process.argv;
const API_URL = argv[2];

request(API_URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(argv[3], body, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
