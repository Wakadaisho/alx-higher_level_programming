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

  rotate () {
    this.width = this.width + this.height;
    this.height = this.width - this.height;
    this.width = this.width - this.height;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
