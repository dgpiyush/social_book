from django.forms import ModelForm


from .models import Books

class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ['book','book_title','book_description','book_author','book_price','visibility','year_of_publish']