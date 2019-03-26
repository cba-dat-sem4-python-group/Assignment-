# Assignment 7
This assignment requires you to work with selenium, BeautifullSoup and possibly regular expressions

Hand-in:
- All the code in a .py file
## Part 1: Preparing data
- Use selenium to go to dba.dk with any search phrase
- Find all products added today
- Find only those from 'København og omegn'
- create a .py file containing above function as a module that will return the browser page source.
## Part 2: Extracting the data
- Use BeautifulSoup to extract all the products in a different function in the module (see selenium_krak.py for example)
- Make a list with tuples of description, year (if available), price, image url and url to details page.
- Sort the products by price
- Return an html table with all the data
## Part 3:
- Add functionality to get the phone number for each product.
