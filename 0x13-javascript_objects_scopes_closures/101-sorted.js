#!/usr/bin/node

const { dict } = require('./101-data.js');

const occurences = Object.keys(dict).reduce((acc, v) => {
  const k = dict[v].toString();
  if (!(k in acc)) {
    acc[k] = [];
  }
  acc[k].push(v);
  return acc;
}, {});

console.log(occurences);
