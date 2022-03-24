from django.contrib import admin
from p_library.models import Book, Author, PublishingHouse

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name
    list_filter = ("title",)
    list_display = ('title', 'author_full_name')
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'publisher')
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("full_name",)
    pass

class BookInline(admin.TabularInline):
    model = Book
    fields = ('ISBN', 'title', 'year_release', 'author')
    extra = 0

@admin.register(PublishingHouse)
class PublisherAdmin(admin.ModelAdmin):
    list_filter = ("company_name",)
    list_display = ('company_name', 'city')
    inlines = [
        BookInline,
    ]
    pass


