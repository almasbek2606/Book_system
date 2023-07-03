from django.urls import path
from .views import (AllBookView, DetailBookView, CreateBookView,
                    UpdateBookView, DeleteBookView, AllAuthorView, UpdateAuthorView, DeleteAuthorView,
                    DetailAuthorView, CreateAuthorView, GetBookFromAuthorView)

urlpatterns = [
    # book_api
    path('', AllBookView.as_view()),
    path('<int:book_id>', DetailBookView.as_view()),
    path('create/', CreateBookView.as_view()),
    path('update/<int:book_id>/', UpdateBookView.as_view()),
    path('delete/<int:book_id>/', DeleteBookView.as_view()),
    # author_api
    path('all_author/', AllAuthorView.as_view()),
    path('author_data/<int:author_id>', DetailAuthorView.as_view()),
    path('create_author/', CreateAuthorView.as_view()),
    path('update_author/<int:author_id>', UpdateAuthorView.as_view()),
    path('delete_author/<int:author_id>', DeleteAuthorView.as_view()),
    # get_book_from_author_id
    path('from_author/<int:author_id>', GetBookFromAuthorView.as_view())
]
