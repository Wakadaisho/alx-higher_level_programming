#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = [];
  for (let i = 2; i < process.argv.length; i++) {
    if (isFinite(process.argv[i])) {
      list.push(parseInt(process.argv[i]));
    }
  }
  list.sort((a, b) => a - b);
  console.log(list[list.length - 2]);
}
