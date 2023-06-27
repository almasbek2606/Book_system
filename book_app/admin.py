from django.contrib import admin
from .models import AuthorModel, BookModel, BookCategoryModel
# Register your models here.

admin.site.register(AuthorModel)
admin.site.register(BookModel)
admin.site.register(BookCategoryModel)
