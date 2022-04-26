<?php
$mysqli = new mysqli("mysql.eecs.ku.edu", "u250k480", "EeV9sae4", "u250k480");
$username = $_POST["username"];

/* check connection */
if ($mysqli->connect_errno) {
 printf("Connect failed: %s\n", $mysqli->connect_error);
 exit();
}

echo "<html>";
echo"<body>";
echo "<table border='1' width='400'>";

echo "<tr>";
	echo "<td>Posts for " .$username. "</td>";
echo "</tr>";

$query = 'SELECT USERNAME FROM USER ';

if ($result = $mysqli->query($query)) {
	while ($row = $result->fetch_assoc()) {
		$content = $row['username'];
		echo "<tr>";
			echo "<td>".$content."</td>";
		echo "</tr>";
	}
	$result->free();
}

echo "</table>";
echo "</body>";
echo "</html>";
?>