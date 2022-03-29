from django.shortcuts import render

# Las funciones deben de llamarse segun sea lo que regresan,
# 

# Create your views here.
def myLinks(request):
    return render(request,'index.html')

# Funcion que regresa la vista de "acerca" de   
def about(request):
    return render(request,'about.html')