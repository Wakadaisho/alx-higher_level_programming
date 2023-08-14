#!/usr/bin/node

let count;

if (isFinite(process.argv[2])) {
  count = parseInt(process.argv[2]);
  if (count >= 0) {
    while (count--) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
