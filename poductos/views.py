from django.shortcuts import render

# Create your views here.

def holaMundo(request):
    return render(request, "holamundo.html")
