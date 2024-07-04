from django.db import models

class LibraryBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    available = models.BooleanField(default=True)
    publication_date = models.DateField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['author']
# Create your models here.
