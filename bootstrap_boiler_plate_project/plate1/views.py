from django.shortcuts import render,redirect
from .forms import AskForm 
from .models import Ask


def index(request):
    if request.method == 'POST':
        post_form = AskForm(request.POST)
        
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    
    else:
        post_form = AskForm()

    return render(request,'index.html',{'post_form': post_form})