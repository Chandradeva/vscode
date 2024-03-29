from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def register(request):
    if(request.method=="POST"):
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            message.success(request,f'account created')
            return redirect('blog-home')
    else:
        form=UserCreationForm()
        return render(request,'users/register.html',{"form":form})


