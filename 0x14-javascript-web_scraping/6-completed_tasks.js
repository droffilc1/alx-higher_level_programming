#!/usr/bin/node
// Computes the number of tasks completed by user id
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const completed = {};
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (task.completed) {
        completed[task.userId] = (completed[task.userId] || 0) + 1;
      }
    }
    console.log(completed);
  }
});
