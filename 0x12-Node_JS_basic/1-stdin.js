process.stdin.resume();
console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('data', (name) => {
  process.stdout.write(`Your name is: ${name}`);
});

process.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
