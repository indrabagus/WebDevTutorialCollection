from django.shortcuts import render

def mainpage(request):
    return render(request,'bstrap/mainpage.html')