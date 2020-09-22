#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const API_URL = argv[2];
let cont = 0;
request(API_URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).results;
    for (const i of data) {
      for (const j of i.characters) {
        if (j === 'https://swapi-api.hbtn.io/api/people/18/') {
          cont++;
        }
      }
    }
    console.log(cont);
  }
});
