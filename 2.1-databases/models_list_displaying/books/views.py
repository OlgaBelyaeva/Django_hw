from django.shortcuts import render
from books.models import Book
import datetime

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('pub_date')
    context = {'books': books}
    return render(request, template, context)


def books_pagi_view(request, pub_date):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('pub_date')
    book_current = books.filter(pub_date=pub_date)
    dates = list(Book.objects.values('pub_date').distinct('pub_date').order_by('pub_date'))
    dates_str = [el['pub_date'].strftime('%Y-%m-%d') for el in dates]
    pub_date_index = dates_str.index(pub_date)

    if pub_date_index == 0:
        previous_date = False
        next_date = dates_str[pub_date_index + 1]
    elif pub_date_index == (len(dates_str) - 1):
        previous_date = dates_str[pub_date_index - 1]
        next_date = False
    else:
        previous_date = dates_str[pub_date_index - 1]
        next_date = dates_str[pub_date_index + 1]

    context = {'books': book_current, 'previous_date': previous_date, 'next_date': next_date}
    return render(request, template, context)

