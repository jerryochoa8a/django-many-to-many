from django.shortcuts import render, HttpResponse,redirect
from many_app.models import Book, Author

def index(request):
    context = {
        "books": Book.objects.all()
        }		
    return render(request, "index.html", context)

def addbook(request):
    addtitle = request.POST['addtitle']
    adddesc = request.POST['adddesc']
    Book.objects.create(title=f"{addtitle}", desc=f"{adddesc}")
    return redirect('/')

def bookpage(request, book_id):
    context = {
        "this_book": Book.objects.get(id=book_id),
        "books_authors": Book.objects.get(id=book_id).authors.all(),
        "authors": Author.objects.all()
        }
    return render(request, "bookpage.html", context)

def bookauthor(request, book_id):
    author_id = request.POST['author_id']#this is from the <select>value="book_id"
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=book_id)
    author.books.add(book)
    return redirect(f'/books/{book_id}')

def book_delete(request, book_id):
    this_book = Book.objects.get(id=book_id)
    this_book.delete()
    return redirect('/')

###########################
####     AUTHORS      #####
###########################
def author_index(request):
    context = {
        "authors": Author.objects.all()
        }		# we're only sending up all the authors
    return render(request, "author_index.html", context)


def addauthor(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    Author.objects.create(first_name=f"{first_name}", last_name=f"{last_name}")
    return redirect('/author')

def authorpage(request, author_id):
    context = {
        "this_author": Author.objects.get(id=author_id),
        "authors_books": Author.objects.get(id=author_id).books.all(),
        "books": Book.objects.all()
        }
    return render(request,"authorpage.html", context)

def authorbook(request, author_id):
    book_id = request.POST['book_id']#this is from the <select>value="book_id"
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=author_id)
    author.books.add(book)
    return redirect(f'/author/{author_id}')

def author_delete(request, author_id):
    this_author = Author.objects.get(id=author_id)
    this_author.delete()
    return redirect('/author')