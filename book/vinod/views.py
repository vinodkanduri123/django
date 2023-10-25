from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *

# Create your views here.
@csrf_exempt
def createAuthor(request):
    try:
        requestBodyToDict = json.loads(request.body)

        nameFromPostmanBody = requestBodyToDict['name']

        savingNameToDb = Author(name = nameFromPostmanBody)
        savingNameToDb.save()

        return JsonResponse({
            "message":f"{nameFromPostmanBody} added to Author table"
        })
    except json.JSONDecodeError as e:
        return JsonResponse({
            "error": "Invalid JSON data in the request body"
        }, status=400)
    except Exception as e:
        return JsonResponse({
            "error": str(e)
        }, status=500)

@csrf_exempt
def createBooks(request):
    try:
        requestBodyToDict = json.loads(request.body)

        authorId = requestBodyToDict['author_id']
        authorName = Author.objects.get(id = authorId).name

        Books = requestBodyToDict['title']

        bookLists = []

        for  book in Books:
            bookLists.append(book)
            newBook = Book.objects.create(title = book, author_id = authorId)


        return JsonResponse({
            "message": f"{bookLists} of {authorName} added successfully"
        })
    except json.JSONDecodeError as e:
        return JsonResponse({
            "error": "Invalid JSON data in the request body"
        }, status=400)
    except Exception as e:
        return JsonResponse({
            "error": str(e)
        }, status=500)


def getBooknamesFromAuthor(request):
    try:

        authId = (json.loads(request.body))['authorId']

        authorName = Author.objects.get(id = authId).name

        booksQuerySet = Book.objects.filter(author_id = authId)

        bookLists = []

        for  book in booksQuerySet:
            bookLists.append(book.title)
            newBook = Book.objects.create(title = book, author_id = authId)

        return JsonResponse({
            "message": f"{bookLists} of {authorName} retrieved successfully"
        })
    except json.JSONDecodeError as e:
        return JsonResponse({
            "error": "Invalid JSON data in the request body"
        }, status=400)
    except Exception as e:
        return JsonResponse({
            "error": str(e)
        }, status=500)
