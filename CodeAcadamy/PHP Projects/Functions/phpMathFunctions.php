<?php
$initial = '555';
// Convert to decimal from octal
$a = octdec($initial);
echo $a;
echo "\n";

// Convert to radians from degrees
$b = deg2rad($a);
echo $b;
echo "\n";

// Take the cosine of $b
$c = cos($b);
echo $c;
echo "\n";

// Round to three decimal places 
$d = round($c, 3);
echo $d;
echo "\n";

// Take the natural log 
$e = log($d);
echo $e;
echo "\n";

// Take the absolute value
$f = abs($e);
echo $f;
echo "\n";

// Take the inverse cosine 
$g = acos($f);
echo $g;
echo "\n";

// Convert radians to degree
$h = rad2deg($g);
echo $h;
echo "\n";

// Floor the number 
$i = floor($h);
echo $i;
echo "\n";

// Subtract 47 
$j = $i - 47;
echo $j;
echo "\n";