# Digital Book Catalogue
Digital Book Catalogue is a book information storing management application using Python and the sqlite3 library.

## This program has features of -
1. Viewing a list of books
2. Searching for a book by its Title, Year of publication , Author name or ISBN
3. Adding a new book details
4. Updating a book record
5. Deleting a book record
6. Quit program

The records consist of Book's Title, Year of publication, Author name, ISBN and Description of a Book are stored in 'data.db' database file.

## Files: 
-- frontend.py --
Tkinter Graphical User Interface code area. Connects to the backend.py to perform the functionality of the application.

-- backend.py --
The back-end of the Graphical User Interface where the logic exists. Connects and creates database table. Inserts, Views, Updates, Searches, Deletes database entries.

-- data.db --
An SQLite3 database file which stores and retrieves the user entries in the application.

-- rough idea.png --
A basic idea of project structure.

## Output :
