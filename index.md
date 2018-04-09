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

# How to Install/Use
1. Download the source code, and extract it.
2. Move the files `isbn.txt`, `addisbn.php`, `add.php`, and `books.sql` to the PHP/MySQL server.
   * OPTIONAL: Move the file `scanner.py` to the Android device running [QPython3](https://play.google.com/store/apps/details?id=org.qpython.qpy3) and [Barcode Scanner](https://play.google.com/store/apps/details?id=com.google.zxing.client.android).
3. On your computer (or Server), install (our recommended program) [Sequel Pro](https://sequelpro.com/) for macOS.
   1. Login to your database
   2. Select your database
   3. Press Shift+Command+I to import the `books.sql` file
   4. Rename the table to `books` from `library_books`
4. For each book, you can either:
   - Enter each ISBN manually into `isbn.txt`.
   - Use QPython3 and run `scanner.py`
5. Open a terminal window and run: `pip -r requirements.txt`
6. Run `isbn_reader.py`
