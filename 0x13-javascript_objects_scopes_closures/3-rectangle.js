#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const slot = 'X';
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

module.exports = Rectangle;
