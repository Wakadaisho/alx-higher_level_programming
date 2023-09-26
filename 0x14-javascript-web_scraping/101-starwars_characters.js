#!/usr/bin/node

const request = require('request');

function get (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

async function orderedResponses (urls) {
  const responses = [];
  for (const url of urls) {
    const response = await get(url);
    responses.push(response);
  }
  return responses;
}

get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2])
  .then((res) => {
    orderedResponses(JSON.parse(res).characters)
      .then((responses) => {
        responses.forEach((response) => console.log(JSON.parse(response).name));
      })
      .catch((error) => {
        console.error(error);
      });
  });
