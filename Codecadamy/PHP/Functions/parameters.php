<?php
// Write your code below:
function increaseEnthusiasm($str){
  return $str . "!";
}


echo increaseEnthusiasm("Oh, Hello!\n");

function repeatThreeTimes($str)
{
  return $str . $str . $str;
}  

echo increaseEnthusiasm("oh");

echo repeatThreeTimes("wow");

echo increaseEnthusiasm(repeatThreeTimes("hai"));