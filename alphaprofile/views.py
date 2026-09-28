from django.shortcuts import render


def homepage(request):
    return render(request,'home.html',{'msg':'this is message from the view'})

    