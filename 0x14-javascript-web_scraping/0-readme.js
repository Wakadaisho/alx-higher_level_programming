#!/usr/bin/node

const fs = require('fs');

try {
  console.log(fs.readFileSync(process.argv[2]).toString());
} catch (error) {
  console.log(error);
}
