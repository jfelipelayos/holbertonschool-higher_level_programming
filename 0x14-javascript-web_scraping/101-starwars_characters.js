#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

function getCharacters (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        console.log(error);
      } else {
        resolve(body);
      }
    });
  });
}

async function printCharacters (charactersList) {
  try {
    for (const url of charactersList) {
      const data = await getCharacters(url);
      console.log(JSON.parse(data).name);
    }
  } catch (error) {
    console.log(error);
  }
}

request(API_URL + argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).characters;
    printCharacters(data);
  }
});
