#!/usr/bin/node
const request = require('request');

request('https://swapi-api.hbtn.io/api/people/18/', (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).films.length;
    console.log(data);
  }
});
