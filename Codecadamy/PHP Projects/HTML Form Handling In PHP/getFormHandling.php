<html>
<body>
<form method="get">
Country:
<input type="text" name="country">
<br>
Language:
<input type="text" name="language">
<br>
<input type="submit" value="Submit">
</form>
<br>
<p>Your language is: <?=$_GET['language'];?><!--Add step 3 code here--></p>
<p>Your country is: <?=$_GET['country'];?> <!--Add step 3 code here--></p>
<a href="index.php">Reset</a>
</body>
</html>