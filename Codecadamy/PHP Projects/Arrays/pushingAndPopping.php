<?php
namespace Codecademy;

$stack = ["wild success", "failure", "struggle"];
// Write your code below:

array_push($stack, "blocker");
array_push($stack, "impediment\n");


echo implode(", ", $stack); 

array_pop($stack);
array_pop($stack);
array_pop($stack);
array_pop($stack);

print_r($stack); 