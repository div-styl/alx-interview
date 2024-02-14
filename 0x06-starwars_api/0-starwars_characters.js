#!/usr/bin/node
// import the requests lib using the const
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (e, res, body) {
  if (e) throw e;
  const actros = JSON.parse(body).characters;
  Orderoutput(actros, 0);
});

const Orderoutput = (actros, x) => {
  if (x === actros.length) return;
  request(actros[x], function (e, res, b) {
    if (e) throw e;
    console.log(JSON.parse(b).name);
    Orderoutput(actros, x + 1);
  });
};
