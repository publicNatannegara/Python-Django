from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from .serializers import BookSerializer

# Create your views here.
from .models import Book


@api_view(["GET"])
def book_list(request):
    books = Book.objects.all()
    # serializer = BookSerializer(books, many=True)
    # return Response(type(serializer.data), status=201)
    data = list(books.values())
    return HttpResponse(
        JsonResponse(
            {
                "code": 201,
                "message": "success",
                "data": data,
            }
        ),
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
def book_create(request):

    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        book.delete()
        data = {
            "code": 204,
            "message": "success",
        }
        return HttpResponse(JsonResponse(data), status=status.HTTP_204_NO_CONTENT)


from rest_framework.views import APIView


class BookListClsView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookCreateClsView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class BookClsView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except:

            serializer = BookSerializer(book)
