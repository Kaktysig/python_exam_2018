from django.http import HttpResponse
# from django.shortcuts import render


def base_view(request):
    return HttpResponse("All ok!")
