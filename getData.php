<?php
$id = $_GET['id'];
// SQLite database file path
$dbPath = 'images.db';

// Connect to the SQLite database
$db = new SQLite3($dbPath);

// Query to retrieve the first link
$query = "SELECT dataID, dataURL, dataExtension FROM data WHERE dataID =" . $id;

// Execute the query
$result = $db->query($query);

// Fetch the first row
$row = $result->fetchArray(SQLITE3_ASSOC);

if($row){
	$dataResponse = [
		'dataID' => $row['dataID'],
		'dataURL' => $row['dataURL'],
		'dataExtension' => $row['dataExtension']
	];
}else{
	$dataResponse = null;
}


// Close the database connection
$db->close();

header('Content-Type: application/json');

// Output the link
echo json_encode($dataResponse);
?>
