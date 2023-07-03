from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BookModel, AuthorModel
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import status

# Create your views here.

""""""""""""""""""""""""""""""""""THIS IS BOOK API VIEW"""""""""""""""""""""""""""""""""


class AllBookView(APIView):
    def get(self, request, *args, **kwargs):
        all_book = BookModel.objects.all()
        serializer = BookSerializer(all_book, many=True)
        return Response(serializer.data)


class DetailBookView(APIView):
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(BookModel, pk=kwargs['book_id'])
        serializer = BookSerializer(book)
        return Response(serializer.data)


class CreateBookView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class UpdateBookView(APIView):
    def patch(self, request, *args, **kwargs):
        instance = get_object_or_404(BookModel, pk=kwargs['book_id'])
        serializer = BookSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteBookView(APIView):
    def delete(self, request, *args, **kwargs):
        instance = get_object_or_404(BookModel, pk=kwargs['book_id'])
        instance.delete()
        return Response({'m': 'success'}, status=status.HTTP_204_NO_CONTENT)


"""""""""""""""""""""""""""""""""""THIS IS AUTHOR API VIEW"""""""""""""""""""""""""""""""""""""""""""""""""""


class AllAuthorView(APIView):
    def get(self, request, *args, **kwargs):
        all_author = AuthorModel.objects.all()
        auth_serializer = AuthorSerializer(all_author)
        return Response(auth_serializer.data)


class DetailAuthorView(APIView):
    def get(self, request, *args, **kwargs):
        author = get_object_or_404(AuthorModel, pk=kwargs['author_id'])
        author_serializer = AuthorSerializer(author)
        return Response(author_serializer.data)


class UpdateAuthorView(APIView):
    def patch(self, request, *args, **kwargs):
        instance = get_object_or_404(AuthorModel, pk=kwargs['author_id'])
        serializer = AuthorSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateAuthorView(APIView):
    def post(self, request, *args, **kwargs):
        create_serializer = AuthorSerializer(data=request.data)
        if create_serializer.is_valid():
            create_serializer.save()
            return Response(create_serializer.data)


class DeleteAuthorView(APIView):
    def delete(self, request, *args, **kwargs):
        delete_author = get_object_or_404(AuthorModel, pk=kwargs['author_id'])
        delete_author.delete()
        return Response({'message': 'author successfully deleted'}, status=status.HTTP_204_NO_CONTENT)


class GetBookFromAuthorView(APIView):
    def get(self, request, *args, **kwargs):
        if get_object_or_404(AuthorModel, pk=kwargs['author_id']):
            all_book = BookModel.objects.all()
            serializer = BookSerializer(all_book, many=True)
            return Response(serializer.data)

