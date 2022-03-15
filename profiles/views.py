from django.shortcuts import render

# Create your views here.

def profile_view(request):
    context={
        'title':'profile'
    }
    return render(request,"profile.html",context)
