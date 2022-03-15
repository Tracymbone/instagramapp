from django.shortcuts import render



# Create your views here.

def post_view(request):
    context={
        'title':'Instagram'
    }
    return render(request,"post.html",context)

def create_post(request):
    context={
        'title':'create post'
    }
    return render(request,"createpost.html",context)




