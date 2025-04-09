from django.contrib import admin
from .models import Author, AuthorProfile, Book, Buyer, Purchase

admin.site.register(Author)
admin.site.register(AuthorProfile)
admin.site.register(Book)
admin.site.register(Buyer)
admin.site.register(Purchase)