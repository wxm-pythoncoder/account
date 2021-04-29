from django.shortcuts import render

# Create your views here.
from book.models import Book
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.core import serializers
import json

# Create your views here.
@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(
                    book_name=request.GET.get('book_name'),
                    money=request.GET.get('money'),
                    phone=request.GET.get('phone'),
                    relation=request.GET.get('relation'),
                    address=request.GET.get('address')
                    )
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def update_book(request):
    response = {}
    try:
        name = request.GET.get('book_name')
        Book.objects.filter(book_name=name).delete()
        book = Book(
                    book_name=request.GET.get('book_name'),
                    money=request.GET.get('money'),
                    phone=request.GET.get('phone'),
                    relation=request.GET.get('relation'),
                    address=request.GET.get('address')
                    )
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def delete_book(request):
    response = {}
    try:
        name = request.GET.get('book_name')
        Book.objects.filter(book_name=name).delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        print(serializers.serialize("json", books))
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
        response['status'] = True
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)