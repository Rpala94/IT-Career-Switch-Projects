<?php
namespace Codecademy;
function agreeOrDisagree($first, $second){
  if($first === $second){
    return "You agree!";
  } else{
    return "You disagree!";
  }
}

echo agreeOrDisagree("left", "right"); 
echo "\n\n";
echo agreeOrDisagree("ok", "ok"); 
echo "\n\n";

$current_month = date("F");
echo checkRenewalMonth($current_month);

echo "\n\n";
echo checkRenewalMonth("July");


function checkRenewalMonth($renewal_month){
  $current_month = date("F");
  if ($renewal_month !== $current_month) {
    return "Welcome!";
  } else {
    return "Time to renew";
  }
}