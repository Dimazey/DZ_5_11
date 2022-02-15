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


