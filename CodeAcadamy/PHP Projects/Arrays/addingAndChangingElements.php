<?php
namespace Codecademy;

$change_me = [3, 6, 9];
// Write your code below:
$change_me[] = "string";

$change_me[] = 3;

$change_me[1] = "tadpole";

print_r($change_me);

echo implode(", ", $change_me);