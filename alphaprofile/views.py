from django.shortcuts import render

class Home:
    def homepage(self,request):
        return render(request,'home.html',{'msg':'this is message from the view'})

    