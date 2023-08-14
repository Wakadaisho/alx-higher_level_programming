#!/usr/bin/node

function factorial (n) {
  if (!n) {
    return (1);
  }

  return factorial(n - 1) * n;
}

let n;

if (isFinite(process.argv[2])) {
  n = parseInt(process.argv[2]);
} else {
  n = NaN;
}

console.log(factorial(n));
