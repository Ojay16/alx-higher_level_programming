#!/usr/bin/node

//script prints a message depending of the number of arguments passed.

const count = process.argv.length;
console.log(count < 1 ? 'No argument' : count >= 3 ? 'Argument found' : 'Arguments found');
