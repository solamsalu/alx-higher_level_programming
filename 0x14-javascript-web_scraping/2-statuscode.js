#!/usr/bin/node
const request = require("request");
request.get(process.argv[2], (err, res, body) => {
    if (err) {
      console.error(err);
    } else {
      console.log(`code: ${res.statusCode}`);
    }
  });
