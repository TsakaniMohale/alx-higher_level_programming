#!/usr/bin/node
const ID = process.argv[2];
const fs = require('request');
fs.get(ID, function (error, polo, body) {
  if (error) throw error;
  else {
    let count = 0;
    const data = JSON.parse(body).results;
    for (let i = 0; i < data.length; i++) {
      for (let j = 0; j < data[i].characters.length; j++) {
        if (data[i].characters[j].includes('/18/')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});
