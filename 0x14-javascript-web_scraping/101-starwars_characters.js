#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}`;

request(url, async (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const result = JSON.parse(body);
  for (const character of result.characters) {
    await new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        if (error) {
          reject(error);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
