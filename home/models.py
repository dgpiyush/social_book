from django.db import models
from django.contrib.auth import get_user_model  
User = get_user_model()

class Books(models.Model):
    book=models.FileField(upload_to='media/books')
    book_title=models.CharField(max_length=100)
    book_description=models.TextField()
    book_author=models.ForeignKey(User,on_delete=models.CASCADE)
    book_price=models.IntegerField()
    visibility=models.BooleanField(default=True)
    year_of_publish=models.DateField(blank=True)





