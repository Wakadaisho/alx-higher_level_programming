#!/usr/bin/node

function callMeMoby (n, f) {
  if (n <= 0) {
    return;
  }
  while (n--) {
    f();
  }
}

module.exports = {
  callMeMoby
};
