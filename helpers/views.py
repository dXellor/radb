from django.shortcuts import render

def handleNotFound(request, exception):
    return render(request, '404.html')

def handleServerError(request):
    return render(request, '500.html')