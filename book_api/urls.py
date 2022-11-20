"""course URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (
    book_list,
    book_create,
    book,
    BookListClsView,
    BookCreateClsView,
    BookClsView,
)

urlpatterns = [
    # path("list", book_list),
    path("list", BookListClsView.as_view()),  # class view version
    # path("add", book_create),
    path("add", BookCreateClsView.as_view()),  # class view version
    # path("<int:pk>", book),
    path("<int:pk>", BookClsView.as_view()),  # class view version
]
