from django.shortcuts import render

# Create your views here.

def dashboard(request):
    user = request.user
    data = {
        "user": user
    }
    return render(request,"dashboard/home.html",data)
