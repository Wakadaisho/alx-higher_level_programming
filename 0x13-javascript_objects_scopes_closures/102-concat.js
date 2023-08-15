#!/usr/bin/node

const fs = require('fs');

const r = fs.readFileSync;
const w = fs.writeFileSync;
const file = process.argv;

w(file[4], r(file[2]) + r(file[3]));
