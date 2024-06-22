<?php
namespace Codecademy;

// Write your code below:
$hybrid_array = [1, 56.98, "array", "-int"];

$hybrid_array[8] = "five more";

print_r($hybrid_array);

array_push($hybrid_array, rand());

echo $hybrid_array[9];
