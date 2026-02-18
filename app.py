from flask import Flask, request, jsonify

app = Flask(__name__) # creating the server, will be used as api server

# create a data store 

books_published = []   # A real app would store this persistently

@app.route('/books')
def all_books():
    return jsonify(books_published)


@app.route('/book', methods=['POST'])
def add_book():
    new_book = request.form
    print(new_book)
    name = new_book.get('name')
    new_book_name = new_book.get('name')
    books_published.append(new_book_name)
    return 'Added', 201


if __name__ == '__main__':
    app.run()