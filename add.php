<?php
	$servername = ""; // MySQL IP/location
	$username = ""; // MySQL username
	$password = ""; // MySQL password
	$dbname = ""; // MySQL Database

	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname);
	// Check connection
	if ($conn->connect_error) {
	    die("Connection failed: " . $conn->connect_error);
	}

	$sql = "INSERT INTO books (title, author, isbn)
	VALUES ('" . $_POST["title"] . "', '" . $_POST["author"] . "', '" . $_POST["isbn"] . "')";

	if ($conn->query($sql) === TRUE) {
	    echo "New record created successfully";
	} else {
	    echo "Error: " . $sql . "<br>" . $conn->error;
	}

	$conn->close();
?> 
