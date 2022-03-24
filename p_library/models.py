from django.db import models
import uuid

# Create your models here.

class Author(models.Model):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)
    def __str__(self):
        return f"{self.full_name}"

class PublishingHouse(models.Model):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.TextField()
    city = models.TextField()
    def __str__(self):
        return f"{self.company_name}"

class Book(models.Model):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE,
                                related_name="book_publisher",
                                null=True, blank=True)
    copy_count = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.title}"

class Friend(models.Model):
    name = models.TextField(max_length=256, verbose_name='friend_name', null=True, blank=True)
    books = models.ManyToManyField(Book, verbose_name='friend_books', through='BooksIssued', null=True, blank=True)
    def __str__(self):
        return f"{self.name}"

class BooksIssued(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    date_delivery = models.DateField(null=True)
    date_return = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.books}"

