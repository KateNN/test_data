import json
from csv import DictReader


# Give books from the books.csv list one by one to every next reader (generator)
def books_borrowing(library_items):
    for book in library_items:
        item = dict()
        item['title'] = book['Title']
        item['author'] = book['Author']
        item['pages'] = book['Pages']
        item['genre'] = book['Genre']
        yield item


with open('users.json', "r", encoding="UTF-8") as users_data:
    with open('books.csv', "r", encoding="UTF-8") as books_data:
        with open('result.json', "w", encoding="UTF-8") as result:
            users = json.load(users_data)
            books = DictReader(books_data)
            readers = []

            # Create list of readers with the required information and an empty list for borrowed books (dict)
            for user in users:
                reader = dict()
                reader['name'] = user['name']
                reader['gender'] = user['gender']
                reader['address'] = user['address']
                reader['age'] = user['age']
                reader['books'] = []
                readers.append(reader)

            # Give a next book to a next reader while no more book left - starting from the 1st reader and the 1st book
            # (the reader who gets the book moves to the end of the queue)
            number_of_readers = len(readers)
            count = 0
            generator = books_borrowing(books)

            for book in generator:
                readers[count % number_of_readers]['books'].append(book)
                count += 1

            json.dump(readers, result, indent=4)
