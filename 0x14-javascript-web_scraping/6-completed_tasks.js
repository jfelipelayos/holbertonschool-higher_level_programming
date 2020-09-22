#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const API_URL = argv[2];
const todoCompleted = {};
request(API_URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);

    for (const i of data) {
      if (i.completed === true) {
        if (i.userId in todoCompleted) {
          todoCompleted[i.userId]++;
        } else {
          todoCompleted[i.userId] = 1;
        }
      }
    }
    console.log(todoCompleted);
  }
});
