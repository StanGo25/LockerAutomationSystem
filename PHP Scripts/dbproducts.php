
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

// Some Query
$sql 	= "SELECT user_id FROM users WHERE user_name='$uname'";
//var_dump($sql);
$query 	= mysqli_query($con, $sql);

while ($row = mysqli_fetch_array($query))
{
	$go = $row['user_id'];
	//echo $go;
}

$sql2 = "INSERT INTO products (product_id,product_name,product_status,product_type,user_id) VALUES (0,'$pname',0,'$ptype','$go')";
$query2 = mysqli_query($con, $sql2);

if ($query2)
{
	echo "Success";
}
// Close connection
mysqli_close ($con);
?>
  </body>
</html>
