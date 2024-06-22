<?php
namespace Codecademy;

// Write your code below:

function convertToShout($str)
{
  return strtoupper($str) . "!";
}

function tipGenerously($cost){
  return ceil($cost * 1.20);
}

function calculateCircleArea($diameter){

  return pi() * ($diameter/2)**2;
}

echo convertToShout("woah there, buddy");
echo "\n";
echo convertToShout("i just don't know");
echo "\n";
echo convertToShout("oh, ok, that's fine");
echo "\n";
echo convertToShout("it's nice to meet you");
echo "\n";
echo tipGenerously(100.00);
echo "\n";
echo tipGenerously(982.27);
echo "\n";
echo tipGenerously(15.67);
echo "\n";
echo tipGenerously(21.65);
echo "\n";
echo calculateCircleArea(25);
echo "\n";
echo calculateCircleArea(30);
echo "\n";
echo calculateCircleArea(872);
echo "\n";
echo calculateCircleArea(29);

