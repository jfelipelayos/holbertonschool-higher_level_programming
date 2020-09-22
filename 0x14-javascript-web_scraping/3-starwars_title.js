#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

request(API_URL + argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
