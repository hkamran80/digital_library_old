# Scans ISBNs (barcodes). Requires an Android device and QPython3 (app) to be installed.

import android
import urllib.request

droid = android.Android()

php_ip = "http://" + "{YOUR_PHP_IP_ADDRESS}" # Enter the IP address where the PHP server is located. 
php_port = "" # Enter the port of your PHP server

while True:
	code = droid.scanBarcode()

	isbn = code[1]["extras"]["SCAN_RESULT"]
	url = php_ip + ":" + php_port + "/addisbn.php?isbn=" + isbn

	urllib.request.urlopen(url)
