
sum_book = 0
for author in Author.objects.all():
    #print(author.full_name)
    author_books = Book.objects.filter(author=author)
    if author_books.count() > 1:
        for book in author_books:
            #print(book.title, book.price, book.copy_count)
            sum_book += book.price * book.copy_count
                
    print(sum_book)
    print('---')

print(sum_book)


sum2 = 0
for author in authors:
    books = Book.objects.filter(author=author)
        for book in books:
            sum2 += book.price * book.copy_count
print(sum2)
