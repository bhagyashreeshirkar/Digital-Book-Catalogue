import sqlite3


def connect():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER, description TEXT)')
    conn.commit()
    conn.close()


def add_data(title, author, year, isbn, description):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO book VALUES(NULL,?,?,?,?,?)', (title, author, year, isbn, description))
    # system will auto-increment id of books thus, we pass NULL parameter
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM book')
    rows = cur.fetchall()  # fetches all rows from query result to get a list of rows
    conn.close()
    # since we don't have to commit changes for viewing, we directly close the connection instead of conn.commit()
    return rows


def search(title='', author='', year='', isbn=''):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?', (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    # since there is only one parameter thus, we add a comma(,) after the parameter
    cur.execute('DELETE FROM book WHERE id=?', (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn, description):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('UPDATE book SET title=?, author=?, year=?, isbn=?, description =? WHERE id =?',
                (title, author, year, isbn, description, id))
    conn.commit()
    conn.close()


connect()
add_data('Guiding Souls - Dialogues on the Purpose of Life', 'Arun Tiwari, A. P. J. Abdul Kalam', 2005, 9788188322749, "It deals with the concept of inner experience – thoughts, emotions, feelings, perception, and knowledge among their things.")
add_data('Train To Pakistan', 'Khushwant Singh', 1956, 9780143065882, "It recounts the Partition of India in August 1947 through the perspective of Mano Majra, a fictional border village.")
add_data('Trainspotting', 'Irvine Welsh', 1993, 9780749336509, "The best kind of comedy is based on recognition, and those of us who had grown up in Scotland during the 1980s fell off our barstools reading Irvine Welsh's Trainspotting. The novel has a surreal kind of authenticity, which might sound like a contradiction until you remember what the times were like: times when a feeling of dispossession gave way to a blessed sense of hedonism. All the characters in the book feel totally committed to their own world view in a way that is hilarious and deeply true.")
add_data('The Haunting of Hill House', 'Shirley Jackson', 1959, 9780141191449, "description: The author decided to write 'a ghost story' after reading about a group of nineteenth-century 'psychic researchers' who studied a house and somberly reported their supposedly scientific findings to the Society for Psychic Research.")
add_data('Three Men In A Boat', 'K Jerome', 1889, 9788172344436, "Three wealthy layabouts take a boat trip up the Thames to the amusement of generations of readers. The book was originally intended to be a serious travel guide but, thankfully, it succumbed to the wit of the narrator's anecdotes and remains a warming portrayal of a brilliantly welcoming writer's mind.")

# delete(2)
# update(5, 'Three Men In A Boat', 'John Leo', 1889, 9788172344436,"Three wealthy layabouts take a boat trip up the Thames to the amusement of generations of readers. The book was originally intended to be a serious travel guide but, thankfully, it succumbed to the wit of the narrator's anecdotes and remains a warming portrayal of a brilliantly welcoming writer's mind.")
# print(view())
# print(search(author='Shirley Jackson'))
