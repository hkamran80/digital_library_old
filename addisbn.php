<?php
	if (isset($_GET["isbn"])) {
		$isbn = htmlspecialchars($_GET["isbn"]) . "\n";
		$file = fopen("isbn.txt", "a") or die("Unable to open isbn.txt");

		fwrite($file, $isbn);

		fclose($file);
	}
?>
