import json

with open('lists.json', 'r') as file:
    lists = json.load(file)

points = {}

for book_list in lists.values():
    for rank, book in enumerate(book_list):
        book = book.lower()
        points[book] = points.get(book, 0) + (100 - rank)

combined_list = sorted(points.items(), key=lambda item: item[1], reverse=True)

top_100_books = combined_list[:]

with open('top_100_books.txt', 'w') as output_file:
    for rank, (book, score) in enumerate(top_100_books, start=1):
        output_file.write(f"{rank}. {book} - {score} points\n")
