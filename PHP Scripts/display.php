
<html>
  <head><title>Owned Devices Status:<br></title></head>
  <body> 
    <?php
	// Open Connection
$con = @mysqli_connect('<hostname>', '<user name>', '<password>', '<database name>', <port number>);

if (!$con) {
    echo "Error: " . mysqli_connect_error();
	exit();
}

$uname = $_GET['u_name'];

//var_dump($pname);
$sql = "SELECT user_id FROM users WHERE user_name='$uname'";
$query = mysqli_query($con, $sql);
while ($row = mysqli_fetch_array($query))
{
	$uid = $row['user_id'];
}

$sql2 = "SELECT product_name,product_status FROM products where user_id = '$uid' AND product_type IN ('1','2')";
$query2= mysqli_query($con, $sql2);

while ($row = mysqli_fetch_array($query2))
{
	$go = $row['product_name'] . ': ' . $row ['product_status'] . ' <br>';
	print ($go);
	//var_dump($go);	
}

// Close connection
mysqli_close ($con);
?>
  </body>
</html>
