
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
$pstat = $_GET['p_stat'];
$uname = $_GET['u_name'];


//var_dump($pname);
$sql = "SELECT user_id FROM users WHERE user_name='$uname'";
$query = mysqli_query($con, $sql);
while ($row = mysqli_fetch_array($query))
{
	$uid = $row['user_id'];
}

$sql2 = "UPDATE products SET product_status = $pstat WHERE user_id = $uid AND product_type = '2'";

var_dump($sql2);

$query2= mysqli_query($con, $sql2);

// Close connection
mysqli_close ($con);
?>
  </body>
</html>
