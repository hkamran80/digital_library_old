#!/usr/bin/python3

# Parse a website then get the title/author for a book using ISBNs, add to database through add.php

from bs4 import BeautifulSoup
import urllib
import requests
import sys

count = 0
totalcount = 0

php_loc = "" # Enter the IP address where the PHP server is located. 
php_port = "" # Enter the port of your PHP server

if php_loc == "" or php_port == "":
    sys.exit("Add your server's location and port!")

with open("isbn.txt", "r") as f:
    txtfile = [l.strip('\n') for l in f.readlines()]
    totalcount = len(txtfile)

for isbn in txtfile:
    count = count + 1

    parsed = BeautifulSoup(urllib.urlopen("https://isbndb.com/search/books/" + isbn), "html.parser")

    try:
        title = parsed.select("h2")[2].a.string.encode("utf-8").strip()
        author = parsed.select("div dl dt a")[0].string.encode("utf-8").strip()
        print("")
    except AttributeError:
        author = "Unable to retrieve title/author"
        print("")

    print(str(count) + "/" + str(totalcount))
    print(title)
    print(author)
    print(isbn)

    r = requests.post("http://" + php_loc + ":" + php_port + "/add.php", data={"title":title, "author":author, "isbn":isbn})

    title = ""
    author = ""
