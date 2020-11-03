from django.shortcuts import render,redirect
from .forms import AskForm 
from .models import Ask

# Create your views here.
def index(request):
    if request.method == 'POST':
        post_form = AskForm(request.POST)
        
        #모델 폼이 유효 할 경우
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    
    #Get 방식일 경우
    else:
        post_form = AskForm()

    return render(request,'index.html',{'post_form': post_form})