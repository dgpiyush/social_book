from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model  
User = get_user_model()

from .models import Books
from .forms import BooksForm




@login_required(login_url='/login/')
def home(request):
    return render(request, "home/index.html")

@login_required(login_url='/login/')
def upload_books(request):
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('my_books')
        else:
            return render(request, "home/upload_books.html",{'form':form})
    

    return render(request, "home/upload_books.html", {'form':BooksForm()})

@login_required(login_url='/login/')
def auther_and_seller(request):

    users=User.objects.all().filter(public_visibility=True)

    return render(request, "home/auther_and_seller.html",{'users':users})

@login_required(login_url='/login/')
def my_books(request):
    books=Books.objects.all().filter(book_author=request.user)

    return render(request, "home/my_books.html",{'books':books})