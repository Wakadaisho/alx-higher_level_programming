#!/usr/bin/node

const slot = 'X';
let size, row, col, square;

if (isFinite(process.argv[2])) {
  size = parseInt(process.argv[2]);
  if (size >= 0) {
    square = '';
    row = 0;
    while (row++ < size) {
      col = 0;
      while (col++ < size) {
        square += slot;
      }
      square += '\n';
    }
    console.log(square.slice(0, -1));
  }
} else {
  console.log('Missing size');
}
