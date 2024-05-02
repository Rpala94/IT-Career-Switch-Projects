<?php
$contacts = ["Susan" => "55512366666", "Alex" => "77799917177", "Lily" => "81811177777"];  
$message = "";
$validation_error = "* Please enter a 11-digit British phone number.";
$name = "";
$number = "";

 if ($_SERVER["REQUEST_METHOD"] == "POST") {
   $name = $_POST["name"];
   $number  = $_POST["number"];
   // Write your code here:
   if (strlen($number)<30){
     $formatted_number = preg_replace("/[^0-9]/", "", $number);
     if (strlen($formatted_number)===11){
       $contacts[$name] = $formatted_number;
       $message = "Thanks ${name}, we'll be in touch.";
     } else {
       $message = $validation_error;
     } 
   } else {
     $message = $validation_error;
  
   }
  
};
?>
<html>
	<body>
  <h3>Contact Form:</h3>
		<form method="post" action="">
			Name:
			<br>
  		<input type="text" name="name" value="<?= $name;?>">
 			<br><br>
  		Phone Number:
  		<br>
  		<input type="text" name="number" value="<?= $number;?>">
  		<br><br> 
  		<input type="submit" value="Submit">
		</form>
		<div id="form-output">
			<p id="response"><?= $message?></p>
    </div>
	</body>
</html>
    