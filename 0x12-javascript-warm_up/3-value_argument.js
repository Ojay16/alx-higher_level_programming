#!/usr/bin/node

//JS script that prints the first argument passed to it.

console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv[2]);
