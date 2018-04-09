# Welcome to Digital Library
This Digital Library project was founded by and for [H. Kamran](twitter.com/@hkamran80). This project uses two to three devices.
- Android (barcode scanner, optional)
- Server (runs PHP, MySQL, and Python 3 (OPTIONAL!))
- Personal computer (Python 3, use if not on the Server)

# Files
There are five different files.
- `scanner.py`: Barcode scanner, runs on the Android device. Optional.
- `isbn_reader.py`: ISBN reader/adder, runs on Server or Personal Computer. Not Optional.
- `isbn.txt`: Text file containing all of the ISBNs. Not Optional.
- `addisbn.php`: Adds ISBNs to `isbn.txt` using `?isbn={ISBN}`. Not Optional.
- `add.php`: The page that adds the parsed books to the database. Optional, IF you rework the code to have the MySQL adding code in the `isbn_reader.py` file.
- `books.sql`: The table that was used in the creation of the code.
