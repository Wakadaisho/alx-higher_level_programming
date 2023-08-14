#!/usr/bin/node

const output = ['No argument', 'Argument found', 'Arguments found'];

console.log(output[Math.min(process.argv.length - 2, 2)]);
