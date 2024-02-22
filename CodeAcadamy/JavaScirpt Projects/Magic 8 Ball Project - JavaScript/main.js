let userName = 'Ruben';

userName ? console.log(`Hello, ${userName}`) : console.log('Hello');

let userQuestion =' Will I adopt a new puppy soon?';

console.log(`${userName} has asked - ${userQuestion}`);

let randomNumber = Math.floor(Math.random() * 8);

console.log(randomNumber);

let eightBall = '';

switch(randomNumber) {
  case 0:
  eightBall = 'Its Not Looking good... BRUV';
  break
  case 1:
  eightBall = 'My Sources Say No';
  break
  case 2:
  eightBall = 'Yeah do it.. What You Waiting For';
  break
  case 3:
  eightBall = 'Ermm No...';
  break
  case 4:
  eightBall = 'Yeah sure!';
  break
  case 5:
  eightBall = 'Outlook not so good';
  break
  case 6:
  eightBall = 'Nope';
  break
  case 7:
  eightBall = 'Ask again later';
  break 
  case 8:
  eightBall = 'Cannot Predict now';
}

console.log(`The Magic 8 Ball Says ${eightBall}.`);