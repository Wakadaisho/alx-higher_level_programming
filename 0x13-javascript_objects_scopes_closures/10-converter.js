#!/usr/bin/node

exports.converter = function (base) {
  return function convert (n) {
    return n.toString(base);
  };
};
