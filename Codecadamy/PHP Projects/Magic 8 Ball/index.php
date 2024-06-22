<?php
function magic8Ball(){
  echo "Tell me... What is your question?\n";

  $question = readline(">");

  echo "\nHmm I see... Your question is $question... i understand why this weights on you... I have consulted the spirit world.\n Here is your answer: ";

  $choice = rand(0,19);
  

  if ($choice === 0) {
    echo "It is certain.\n";
  } elseif ($choice === 1){
    echo "It is decidedly so.";
  } elseif ($choice === 2) {
    echo "Without a doubt.\n";
  } elseif($choice === 3){
    echo "Yes - definitely.\n";
  } elseif($choice === 4){
    echo "You may rely on it.\n";
  } elseif($choice === 5){
    echo "As I see it, yes.\n";
  } elseif($choice === 6){
    echo "Most likely.\n";
  } elseif($choice === 7){
    echo "Outlook good.\n";
  } elseif($choice === 8){
    echo "Yes.\n";
  } elseif($choice === 9){
    echo "Signs point to yes.\n";
  } elseif($choice === 10){
    echo "Reply hazy, try again.\n";
  } elseif($choice === 11){
    echo "Ask again later.\n";
  } elseif($choice === 12){
    echo "Better not tell you now.\n";
  } elseif($choice === 13){
    echo "Cannot predict now.\n";
  } elseif($choice === 14){
    echo "Concentrate and ask again.\n";
  } elseif($choice === 15){
    echo "Don't count on it.\n";
  } elseif($choice === 16){
    echo "My reply is no.\n";
  } elseif($choice === 17){
    echo "My sources day no.\n";
  } elseif($choice === 18){
    echo "Outlook not so good.\n";
  } else {
    echo "Very doubtful.\n";
  }
/* switch statement alternantive 
  switch ($choice) {
    case 0:
     echo "It is certain.\n";
     break;
    case 1:
    echo "It is decidedly so.";
     break;
  case 2:
    echo "Without a doubt.\n";
     break;
  case 3:
     echo "Yes - definitely.\n";
     break;
  case 4:
     echo "You may rely on it.\n";
     break;
  case 5:
     echo "As I see it, yes.\n";
     break;
  case 6:
     echo "Most likely.\n";
     break;
  case 7:
     echo "Outlook good.\n";
     break;
  case 8:
     echo "Yes.\n";
     break;
  case 9:
     echo "Signs point to yes.\n";
     break;
  case 10:
     echo "Reply hazy, try again.\n";
     break;
  case 11:
     echo "Ask again later.\n";
     break;
  case 12:
     echo "Better not tell you now.\n";
     break;
  case 13:
     echo "Cannot predict now.\n";
     break;
  case 14:
     echo "Concentrate and ask again.\n";
     break;
  case 15:
     echo "Don't count on it.\n";
     break;
  case 16:
     echo "My reply is no.\n";
     break;
  case 17:
     echo "My sources day no.\n";
     break;
  case 18:
     echo "Outlook not so good.\n";
     break;
  default:
    echo "Very doubtful.\n";
  } 
*/
}

 magic8Ball();