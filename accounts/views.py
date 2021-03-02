from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # creates a server side form object with the POST data
        if form.is_valid():  # validates the form
            form.save()  # stores the data
            
            return redirect('articles:list')  # redirects the user to the 'list' url in the articles namespace
            
    elif request.method == 'GET':
        form = UserCreationForm()  # creates a new form object to pass to the template
    
    return render(request, 'accounts/signup.html', {'form':form})  # if form.is_valid == FALSE, its POST data gets reloaded in the form