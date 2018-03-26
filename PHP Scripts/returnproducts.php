
<html>
  <head><title>Insert Title Here</title></head>
  <body> 
    <?php
	// Open Connection
$con = @mysqli_connect('<hostname>', '<user name>', '<password>', '<database name>', <port number>);

if (!$con) {
    echo "Error: " . mysqli_connect_error();
	exit();
}
$ptype = $_GET['p_type'];
$uname = $_GET['u_name'];
$pname = $_GET['p_name'];
//var_dump($pname);
$sql = "SELECT user_id FROM users WHERE user_name='$uname'";
$query = mysqli_query($con, $sql);
while ($row = mysqli_fetch_array($query))
{
	$uid = $row['user_id'];
}

$sql2 = "SELECT product_type FROM products where user_id = '$uid'";
$query2= mysqli_query($con, $sql2);

while ($row = mysqli_fetch_array($query2))
{
	$go = $row['product_type'] . ' ';
	echo $go;
	//var_dump($go);	
}

// Close connection
mysqli_close ($con);
?>
  </body>
</html>
