
<html>
  <head><title>Insert Title Here</title></head>
  <body> 
    <?php
	// Open Connection
$con = @mysqli_connect('<host name>', '<username>', '<password>', '<database name>', <port number>);

if (!$con) {
    echo "Error: " . mysqli_connect_error();
	exit();
}

$uname = $_GET['user_name'];
$upin = $_GET['user_pin'];
//var_dump($pname);

// Some Query
$sql 	= "INSERT INTO users (user_id, user_name, user_pin) values (0, '$uname',$upin)";
//var_dump($sql);
$query 	= mysqli_query($con, $sql);

if ($query){

	echo "Success";
}

// Close connection
mysqli_close ($con);
?>
  </body>
</html>
