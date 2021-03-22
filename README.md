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

## Files -
###### frontend.py  
Tkinter Graphical User Interface code area. Connects to the backend.py to perform the functionality of the application.

###### backend.py  
The back-end of the Graphical User Interface where the logic exists. Connects and creates database table. Inserts, Views, Updates, Searches, Deletes database entries.

###### data.db  
An SQLite3 database file which stores and retrieves the user entries in the application.

###### rough idea.png  
A basic idea of project structure.

## Output :
Main Screen  
<img width="647" alt="main window" src="https://user-images.githubusercontent.com/67758900/112047079-ce621880-8b72-11eb-84c5-3115d1fdf644.PNG">

Main Screen after clicking on the **View Book List** button  
<img width="647" alt="After clicking on 'View Book List' button" src="https://user-images.githubusercontent.com/67758900/112047239-0b2e0f80-8b73-11eb-9f63-c26eea7c95ac.PNG">

By clicking on any book record details automatically get filled into input boxes  
<img width="648" alt="After clicking on random book record the details automatically gets filled into input boxes" src="https://user-images.githubusercontent.com/67758900/112047421-47617000-8b73-11eb-8efb-b127020ea656.PNG">

Output after clicking on the **Search Entry** button for exploring records for a Book's Title, Year of publication, Author name, ISBN  
<img width="648" alt="after clicking on 'Search Entry' button" src="https://user-images.githubusercontent.com/67758900/112047742-a8894380-8b73-11eb-8af2-5aadbf7c16e8.PNG">

Later adding details of a new book by clicking on **Add Book Details** button  
<img width="648" alt="after adding details of a new book" src="https://user-images.githubusercontent.com/67758900/112048226-32391100-8b74-11eb-90c0-724beaba539c.PNG">

To update the book records, you need to select a book and make changes in input boxes  
<img width="647" alt="for update book records1" src="https://user-images.githubusercontent.com/67758900/112048551-893ee600-8b74-11eb-85ac-7d044dce2e38.PNG">

After clicking on the **Update Details** button  
<img width="645" alt="for update book records2" src="https://user-images.githubusercontent.com/67758900/112048773-c5724680-8b74-11eb-9072-6032215f7dae.PNG">

To delete a book records from a list, you need to select it and click on the **Delete Selected Book** button  
<img width="647" alt="for delete selected book1" src="https://user-images.githubusercontent.com/67758900/112049024-15e9a400-8b75-11eb-8196-032d66cc8ab0.PNG">

Result after deleting a book from the list  
<img width="648" alt="for delete selected book2" src="https://user-images.githubusercontent.com/67758900/112049498-b8098c00-8b75-11eb-8b6e-58a77eb3ed1d.PNG">

functioning Scrollbars  
<img width="648" alt="scorll bars" src="https://user-images.githubusercontent.com/67758900/112049621-e25b4980-8b75-11eb-8c8c-3535787bfaba.PNG">

Lastly, the application gets closed by clicking on **Quit** button.
