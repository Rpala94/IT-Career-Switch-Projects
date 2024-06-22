<html>
<body>
<form method="post">
Favorite Color:
<input type="text" name="color">
<br>
Favorite Food:
<input type="text" name="food">
<br>
<input type="submit" value="Submit">
</form>
<br>
<p>Best food is: <?=$_POST['food'];?><!--Add step 3 code here--></p>
<p>Best color is: <?=$_POST['color'];?><!--Add step 3 code here--></p>
<a href="index.php">Reset</a>
</body>
</html>