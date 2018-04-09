# Scans ISBNs (barcodes). Requires an Android device and QPython3 (app) to be installed.

import android
import urllib.request

droid = android.Android()

php_ip = "http://" + "{YOUR_PHP_IP_ADDRESS}" # Enter the IP address where the PHP server is located. 
php_port = "" # Enter the port of your PHP server

while True:
	code = droid.scanBarcode()

	isbn = code[1]["extras"]["SCAN_RESULT"]
	url = php_ip + ":" + php_port + "/data?isbn=" + isbn

	#droid.startActivity("android.intent.action.VIEW", "10.90.100.188:8888/index.php?isbn=" + int(code[‘result’][‘SCAN_RESULT’]))
	urllib.request.urlopen(url)
