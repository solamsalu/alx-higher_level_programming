#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/${id}';

request.get(url, (err, res, body) => {
    if (err) {
      console.error(err);
    } else {
      let data = JSON.parse(body);
      if (data.title) {
        console.log(data.title);
      } else {
        console.log("Invalid movie ID");
      }
    }
  });
