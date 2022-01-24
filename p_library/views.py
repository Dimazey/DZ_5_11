from django.shortcuts import render, redirect
from p_library.models import Book, Author, PublishingHouse
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def books_list(request):
    books=Book.objects.all()
    book_names=[]
    for book in books:
        book_names.append(book.title)
    return HttpResponse(book_names)

def index(request):
    template=loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data={
    "title":"мою библиотеку", 
    "books":books,
#    "my_list": [1,2,3,4,5],
    }
    return HttpResponse(template.render(biblio_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
        if not book:
            return redirect('/index/')
        if book.copy_count < 1:
            book.copy_count = 0
        else: 
            book.copy_count -= 1
        book.save()
        return redirect('/index/')
    else: 
        return redirect('/index/')

def publishers(request):
    template = loader.get_template('publishers.html')
    publishers = PublishingHouse.objects.all().order_by('company_name')
    books_by_publisher = {}
    for publish_comp in publishers:
        books_by_publisher[publish_comp.company_name] = Book.objects.filter(publisher=publish_comp).order_by('title')

    publisher_books_data = {
            "title": "СПИСОК КНИГ ПО ИЗДАТЕЛЬСТВАМ",
            "books": books_by_publisher,
        }
    return HttpResponse(template.render(publisher_books_data, request))
