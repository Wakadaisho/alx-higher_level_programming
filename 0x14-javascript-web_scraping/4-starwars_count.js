#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(body.match(/people\/18/g)?.length || 0);
  }
});
