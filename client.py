import requests

new_book = {'name': 'Example'}
response = requests.post('http://127.0.0.1:5000/book', data=new_book)
print(response.status_code)

response = requests.get('http://127.0.0.1:5000/books')
books = response.json()
print(books)