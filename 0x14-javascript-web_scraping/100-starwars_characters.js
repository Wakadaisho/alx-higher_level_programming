#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2],
  function (error, response, body) {
    if (error) {
      console.error(error);
    } else {
      JSON.parse(body).characters.forEach(person => {
        request(person, function (error, response, body) {
          if (error) {
            console.error(error);
          } else {
            console.log(JSON.parse(body).name);
          }
        });
      });
    }
  });
