#!/usr/bin/node

function add (a, b) {
  return a + b;
}

let a, b;

if (isFinite(process.argv[2])) {
  a = parseInt(process.argv[2]);
} else {
  a = undefined;
}

if (isFinite(process.argv[3])) {
  b = parseInt(process.argv[3]);
} else {
  b = undefined;
}

console.log(add(a, b));
