#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const stats = JSON.parse(body).reduce((acc, curr) => {
      if (curr.completed) { acc[curr.userId] = (acc[curr.userId] || 0) + curr.completed; }
      return acc;
    }, {});
    console.log(stats);
  }
});
