#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const slot = c || 'X';
    let square = '';
    let row = 0;
    let col;
    while (row++ < this.height) {
      col = 0;
      while (col++ < this.width) {
        square += slot;
      }
      square += '\n';
    }
    console.log(square.slice(0, -1));
  }
}

module.exports = Square;
