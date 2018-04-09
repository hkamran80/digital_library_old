# Digital Library
Welcome to the Digital Library repository. Please feel free to make forks & pull requests!

# Requirements
- Android Device with [QPython3](https://play.google.com/store/apps/details?id=org.qpython.qpy3) installed. (For barcode scanning)
- Server with PHP, MySQL, and Python 3 installed (receiving codes, parsing codes, adding to database)
- The contents of this repository

# Files
- `scanner.py`: Barcode scanner, requires [QPython3](https://play.google.com/store/apps/details?id=org.qpython.qpy3) and [Barcode Scanner](https://play.google.com/store/apps/details?id=com.google.zxing.client.android) installed.
- `isbn_reader.py`: Parses ISBNs with data from [ISBNdb.com](https://isbndb.com), requires `Requests` (Python module)
- `add.php`: The page that adds to the database
- `isbn.txt`: Text file containing all of the ISBNs
