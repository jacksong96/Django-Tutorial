from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, "book_outline/index.html",{
        "books" : books
    })
    
def book_detail(request,slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outline/book_detail.html",{
        "title": book.title,
        "author": book.author,
        "is_bestselling": book.is_bestselling,
        "rating": book.rating,
    })